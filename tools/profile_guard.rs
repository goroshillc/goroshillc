//! goroshi-profile-guard - keep the public profile informative without leaking the private estate.
#![forbid(unsafe_code)]
#![deny(warnings)]

use std::fs;
use std::path::Path;

const HERO_PICTURE: &str = "<picture>\n  <source media=\"(prefers-color-scheme: dark)\" srcset=\"assets/hero.svg\">\n  <source media=\"(prefers-color-scheme: light)\" srcset=\"assets/hero-light.svg\">\n  <img src=\"assets/hero-light.svg\" alt=\"Goroshi LLC: systems with roots. Original architectural tree with branching systems and grounded roots. Built to be understood. Designed to hold up.\">\n</picture>";

fn check(readme: &str, artwork: &str) -> Result<(), String> {
    // Permit only the reviewed local theme switch; other image HTML stays forbidden.
    let lower = readme.replace(HERO_PICTURE, "").to_ascii_lowercase();
    for forbidden in [
        "/users/",
        "/private/",
        "file://",
        "ssh://",
        "http://",
        "<script",
        "<iframe",
        "<img",
        "<picture",
        "<source",
        "127.0.0.1",
        "localhost:",
        "192.168.",
        "10.0.",
        ".env",
        "begin private key",
        "shields.io",
        "readme-stats",
        "waka-readme",
        "visitor-badge",
    ] {
        if lower.contains(forbidden) {
            return Err(format!(
                "public README contains forbidden marker: {forbidden}"
            ));
        }
    }
    for key in ["api_key", "token", "password"] {
        let assignment = format!("{key}=");
        if lower.contains(&assignment) {
            return Err(format!("public README contains an assignment to: {key}"));
        }
    }

    for line in readme.lines().filter(|line| line.contains("![")) {
        if !line.contains("](assets/hero.svg)") {
            return Err("profile image must be the reviewed local artwork".into());
        }
    }
    for required in [
        "# Stefano Theofanous",
        "## Selected work",
        "## Public proof",
        "## How I build",
        "## Connect",
        "https://github.com/goroshillc/local-data-exporter",
        "not claims that every component is public, deployed",
    ] {
        if !readme.contains(required) {
            return Err(format!(
                "public README missing required context: {required}"
            ));
        }
    }
    if readme.len() > 16_384 || artwork.len() > 32_768 {
        return Err("profile asset exceeds bounded publication size".into());
    }

    let svg = artwork
        .replace("http://www.w3.org/2000/svg", "")
        .to_ascii_lowercase();
    for forbidden in [
        "<script",
        "<foreignobject",
        "<iframe",
        "<image",
        "<style",
        "<use",
        "<!entity",
        "<?xml-stylesheet",
        "style=",
        "onload=",
        "onclick=",
        "onerror=",
        "onfocus=",
        "onmouseover=",
        "onbegin=",
        "href=",
        "http://",
        "https://",
        "data:",
        "@import",
        "<animate",
        "<set",
    ] {
        if svg.contains(forbidden) {
            return Err(format!(
                "artwork contains active or external content: {forbidden}"
            ));
        }
    }
    for reference in svg.match_indices("url(") {
        if !svg[reference.0..].starts_with("url(#") {
            return Err("artwork references a nonlocal resource".into());
        }
    }
    if !artwork.starts_with("<svg xmlns=\"http://www.w3.org/2000/svg\"")
        || !artwork.contains("<title")
        || !artwork.contains("<desc")
    {
        return Err("artwork lacks a local SVG root or accessible description".into());
    }
    Ok(())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let readme = fs::read_to_string(Path::new("README.md"))?;
    let artwork = fs::read_to_string(Path::new("assets/hero.svg"))?;
    let light_artwork = fs::read_to_string(Path::new("assets/hero-light.svg"))?;
    if readme.matches(HERO_PICTURE).count() != 1 {
        return Err("README must contain exactly one reviewed light/dark hero".into());
    }
    check(&readme, &artwork)?;
    check(&readme, &light_artwork)?;
    println!("PROFILE PUBLICATION GUARD PASS");
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::{HERO_PICTURE, check};

    const VALID: &str = "# Stefano Theofanous\n## Selected work\n## Public proof\n## How I build\n## Connect\nhttps://github.com/goroshillc/local-data-exporter\nnot claims that every component is public, deployed\n![Art](assets/hero.svg)";
    const SVG: &str = "<svg xmlns=\"http://www.w3.org/2000/svg\"><title>Art</title><desc>Art description</desc></svg>";

    #[test]
    fn accepts_a_local_accessible_public_profile() {
        assert!(check(VALID, SVG).is_ok());
    }

    #[test]
    fn accepts_only_the_exact_local_theme_switch() {
        assert!(check(&format!("{VALID}\n{HERO_PICTURE}"), SVG).is_ok());
        for replacement in ["https://tracker.example/x.svg", "assets/unreviewed.svg"] {
            let changed = HERO_PICTURE.replace("assets/hero-light.svg", replacement);
            assert!(check(&format!("{VALID}\n{changed}"), SVG).is_err());
        }
        assert!(check(&format!("{VALID}\n<img src=\"assets/hero.svg\">"), SVG).is_err());
    }

    #[test]
    fn refuses_local_paths_and_private_network_addresses() {
        for marker in ["/Users/name/secret", "10.0.0.1", "127.0.0.1", "file://data"] {
            assert!(check(&format!("{VALID}{marker}"), SVG).is_err());
        }
    }

    #[test]
    fn refuses_external_images_and_active_svg() {
        assert!(
            check(
                &format!("{VALID}\n![x](https://tracker.example/x.svg)"),
                SVG
            )
            .is_err()
        );
        assert!(
            check(
                VALID,
                &SVG.replace("</svg>", "<script>alert(1)</script></svg>")
            )
            .is_err()
        );
        assert!(check(VALID, &SVG.replace("</svg>", "<image href=\"x\"/></svg>")).is_err());
        assert!(check(VALID, &SVG.replace("</svg>", "<path style=\"x\"/></svg>")).is_err());
    }

    #[test]
    fn refuses_broken_evidence_context_and_widget_services() {
        assert!(
            check(
                &VALID.replace("not claims that every component is public, deployed", ""),
                SVG
            )
            .is_err()
        );
        assert!(check(&format!("{VALID} shields.io"), SVG).is_err());
    }
}

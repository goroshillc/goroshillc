<div align="center">

![Goroshi LLC. Build with proof. A ring surrounds a precise architectural grid.](assets/hero.svg)

# Stefano Theofanous

**Founder, Goroshi LLC** · Software engineering · Business automation · AI developer tooling

[Explore the work](#selected-work) · [How I build](#how-i-build) · [Public proof](#public-proof) · [Connect](#connect)

</div>

---

I turn messy operational work into software that people can inspect, use, and trust.
My focus is the connection between **source data**, **explicit business rules**, and **clear interfaces**.
Rust, APIs, and AI-assisted development are tools in that work; a passing build is only one part of proving a system behaves as intended.

## Selected work

| Domain | The problem | My engineering focus |
| :--- | :--- | :--- |
| **Business operations** | Restaurant and property workflows begin with records from different sources. | Traceable inputs, exact allocation, typed money, and reviewable outputs. |
| **Developer platforms** | AI-assisted work can lose context, duplicate ownership, or report completion too early. | Isolated workspaces, explicit task ownership, bounded context, and evidence tied to each claim. |
| **Geospatial decisions** | A nearby feature on a map can look more certain than the source permits. | Provenance, exclusions, and visible unknowns in energy-site screening. |

<details>
<summary><strong>What these terms mean</strong></summary>

**Typed money** means amounts are represented as integer cents with operations designed to preserve accounting invariants.
**Provenance** means a conclusion retains a path back to the source and method that produced it.
**Evidence of completion** separates source review and tests from integration, installation, and observed behavior.

</details>

These are architectural descriptions of private work at different stages.
They are not claims that every component is public, deployed, or available to run.

## Public proof

**[Local Data Exporter](https://github.com/goroshillc/local-data-exporter)** is a RuneLite plugin that writes local account snapshots to JSON for personal tracking and analysis.
Its public repository documents the exported data and files.
The plugin is a concrete example of making state inspectable while keeping the resulting account data local.

The [profile repository](https://github.com/goroshillc/goroshillc) contains this page and its original artwork.
Its publication check rejects local paths, private network addresses, external image hosts, and active SVG content before changes land.

## How I build

```text
Understand the source
        ↓
State the invariant
        ↓
Build a bounded path
        ↓
Test failure as carefully as success
        ↓
Verify the behavior people actually see
```

I prefer explicit failure to a result that only looks complete.
I keep a distinction between an idea, a source change, a passing test, and a working product.
For operational and financial work, uncertainty stays visible until the evidence resolves it.

<details>
<summary><strong>Engineering boundaries I care about</strong></summary>

- **Correctness:** checked arithmetic, validated input, and errors that identify a failed boundary.
- **Privacy:** public explanations do not expose private records, credentials, internal endpoints, or unreleased implementation details.
- **Reviewability:** small changes, clear ownership, reproducible checks, and honest acceptance limits.
- **Usability:** the interface should help someone understand the next decision without knowing the entire system first.

</details>

## Connect

I am open to **fully remote** software roles involving backend systems, business automation, internal tools, and applied AI.
You can reach me through [LinkedIn](https://www.linkedin.com/in/stefano-theofanous-a418a4426/).
I can discuss the architecture and engineering decisions behind private work without exposing customer, family, or business records.

---

<sub>© 2026 Goroshi LLC. All rights reserved. Public overview only.</sub>

<sub>By the grace of God, I give all glory to Jesus Christ.</sub>

<h1 align="center">Stefano Theofanous</h1>

<p align="center">
  <strong>Founder, Goroshi LLC</strong><br>
  Software engineering · Business automation · AI developer tooling
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Rust-18181B?style=for-the-badge&amp;logo=rust&amp;logoColor=white" alt="Technical focus: Rust">
  <img src="https://img.shields.io/badge/HTTP_APIs-27272A?style=for-the-badge" alt="Technical focus: HTTP APIs">
  <img src="https://img.shields.io/badge/Data_Validation-3F3F46?style=for-the-badge" alt="Technical focus: data validation">
  <img src="https://img.shields.io/badge/AI_Tooling-52525B?style=for-the-badge" alt="Technical focus: AI tooling">
</p>

<p align="center">
  <strong>Fully remote opportunities</strong> · <a href="https://www.linkedin.com/in/stefano-theofanous-a418a4426/">LinkedIn</a><br>
  <a href="#selected-engineering-work">Selected work</a> · <a href="#engineering-approach">Engineering approach</a> · <a href="#opportunities">Opportunities</a>
</p>

---

I build software for restaurant and property operations, and tooling for controlled AI-assisted development.
My work connects source data, business rules, and usable interfaces, with particular attention to correctness, traceability, and failure handling.

## Selected engineering work

**Business operations and financial data**<br>
Sales reconciliation, statement packages, document extraction, and property labor and invoice workflows.
The engineering emphasizes typed money, exact allocation, and traceable source records.

**AI-assisted development platforms**<br>
Isolated workspaces, task ownership, context retrieval, and evidence-driven review.
Validation distinguishes a consistent record of work from a verified running system.

**Geospatial decision support**<br>
Battery energy storage site screening that relates land-use observations to substation locations and voltage information.
Source provenance, exclusions, and explicit unknowns accompany the results.

<details>
<summary><strong>Engineering detail: data invariants, validation boundaries, and uncertainty</strong></summary>

- **Financial correctness:** a Rust money type represents integer cents, exposes checked arithmetic, and preserves remainders during allocation so the parts reconcile to the original amount.
- **Evidence contracts:** an offline Rust validator checks relationships between requirements, project decisions, and review, test, integration, and runtime evidence; malformed inputs are rejected, and reference consistency is explicitly separate from independent verification.
- **Geospatial uncertainty:** straight-line proximity is a screening input, not proof of interconnection capacity; land-use observations remain distinct from legal parcel boundaries.

</details>

*These are private projects at different stages of development and validation; this overview does not imply that every component is deployed.*

## Technical focus

Rust · HTTP APIs · Backend services · Command-line tools · Data validation · Workflow automation

## Engineering approach

- **Correctness:** typed inputs, bounded operations, and explicit failure states.
- **Integration:** direct APIs and existing components where they fit the problem.
- **Verification:** failure-case tests, reproducible checks, and separate deployment evidence.
- **Maintainability:** focused changes, documented tradeoffs, and durable handoffs.
- **Accountability:** AI assists implementation; review and verification remain my responsibility.

## Opportunities

I am interested in **fully remote** roles in backend development, business automation, internal tools, and applied AI.
Business source code and operational records remain private; I can discuss the architecture and engineering decisions behind the work.

---

By the grace of God, I give all glory to Jesus Christ.

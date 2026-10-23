<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.webp">
    <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.webp">
    <img src="assets/banner-light.png" width="100%" alt="GOROSHI. Stefano Theofanous, platform and systems engineer, AI-native.">
  </picture>
</p>

<div align="center">

### `PLATFORM & SYSTEMS ENGINEER // GOROSHI LLC`
**`AI-NATIVE` · `NEOVIM` · `ARCH LINUX` · `METAL TO BROWSER` · `SHIPS DAILY`**

</div>

```text
ID        :: goroshillc
ORG       :: Goroshi LLC · Founder & Systems Engineer
EDITOR    :: Neovim. hands on home row.
OS        :: Arch Linux (Omarchy, Hyprland) · macOS
AIM       :: theosis.
AGENTS    :: 8,200+ AI agent sessions run · 5,600+ orchestrated subagents
          :: 210 sessions in a single day · 117 agents in one workflow
TOKENS    :: 147B+ tokens processed across Claude, Codex, Copilot, Antigravity, OpenCode and local models (measured Oct 23 2026)
FLEET     :: CLI: Claude Code · Codex · Gemini CLI · GitHub Copilot · OpenCode
          :: IDE & apps: Cursor · Antigravity · Claude · ChatGPT · Gemini
          :: local: Ollama · Qwen3.8 27B · Flash-Next
METAL     :: hand-written GPU compute kernels in Rust on Apple Metal
          :: measured: 294 GB/s memory bandwidth · 2.8 TFLOP/s FP32 · ridge 9.6 FLOP/byte
COMPUTE   :: Apple M5 Max · 18-core CPU · 40-core GPU · 128 GB unified · 8 TB SSD · +
          :: GPUs: NVIDIA RTX 5080 · RTX 5070 (Blackwell) · RTX 4090 · RTX 4080 (Ada) · RTX 3080 · +
          :: 80+ TB storage & backup, local + cloud
          :: private Tailscale mesh across every node · +
          :: expanding.
SCALE     :: 467+ Rust crates in one workspace · 279+ repositories
OUTPUT    :: 3,886+ contributions in the last year across 261+ repositories
SOURCE    :: private. architecture reviews and live walkthroughs on request.
STATUS    :: ACTIVE PRODUCTION // OPEN TO ENGINEERING ROLES & PLATFORM ENGAGEMENTS
```

### `01 // STACK`

<div align="center">

`LANGUAGES`

![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/Go-000000?style=for-the-badge&logo=go&logoColor=00ADD8)
![TypeScript](https://img.shields.io/badge/TypeScript-000000?style=for-the-badge&logo=typescript&logoColor=3178C6)
![JavaScript](https://img.shields.io/badge/JavaScript-000000?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Python](https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=3776AB)
![C](https://img.shields.io/badge/C-000000?style=for-the-badge&logo=c&logoColor=A8B9CC)
![SQL](https://img.shields.io/badge/SQL-000000?style=for-the-badge&logo=sqlite&logoColor=white)
![Lean 4](https://img.shields.io/badge/Lean_4-000000?style=for-the-badge)

`INFRASTRUCTURE`

![Docker](https://img.shields.io/badge/Docker-000000?style=for-the-badge&logo=docker&logoColor=2496ED)
![Kubernetes](https://img.shields.io/badge/Kubernetes-000000?style=for-the-badge&logo=kubernetes&logoColor=326CE5)
![AWS](https://img.shields.io/badge/AWS_S3_·_CloudFront-000000?style=for-the-badge&logo=amazonwebservices&logoColor=FF9900)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-000000?style=for-the-badge&logo=githubactions&logoColor=2088FF)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-000000?style=for-the-badge&logo=rabbitmq&logoColor=FF6600)
![Linux](https://img.shields.io/badge/Arch_Linux-000000?style=for-the-badge&logo=archlinux&logoColor=1793D1)
![Git](https://img.shields.io/badge/Git-000000?style=for-the-badge&logo=git&logoColor=F05032)
![Neovim](https://img.shields.io/badge/Neovim-000000?style=for-the-badge&logo=neovim&logoColor=57A143)

`DATA & AI`

![DataFusion](https://img.shields.io/badge/Apache_DataFusion-000000?style=for-the-badge&logo=apache&logoColor=white)
![Arrow](https://img.shields.io/badge/Apache_Arrow-000000?style=for-the-badge&logo=apache&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-000000?style=for-the-badge&logo=pandas&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-000000?style=for-the-badge&logo=nvidia&logoColor=76B900)
![Metal](https://img.shields.io/badge/Metal-000000?style=for-the-badge&logo=apple&logoColor=white)

`AI FLEET`

![Claude Code](https://img.shields.io/badge/Claude_Code-000000?style=for-the-badge&logo=anthropic&logoColor=white)
![Codex](https://img.shields.io/badge/OpenAI_Codex-000000?style=for-the-badge&logo=openai&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_CLI-000000?style=for-the-badge&logo=googlegemini&logoColor=8E75B2)
![Cursor](https://img.shields.io/badge/Cursor-000000?style=for-the-badge&logo=cursor&logoColor=white)
![Copilot](https://img.shields.io/badge/GitHub_Copilot-000000?style=for-the-badge&logo=githubcopilot&logoColor=white)
![Antigravity](https://img.shields.io/badge/Antigravity-000000?style=for-the-badge&logo=google&logoColor=white)
![OpenCode](https://img.shields.io/badge/OpenCode-000000?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama_·_Qwen3.8_27B_·_Flash--Next-000000?style=for-the-badge&logo=ollama&logoColor=white)
![ChatGPT](https://img.shields.io/badge/ChatGPT-000000?style=for-the-badge&logo=openai&logoColor=white)

</div>


### `02 // PRODUCTION SYSTEMS` (private repositories)

| SYSTEM | ARCHITECTURE & SCOPE | STACK |
| :--- | :--- | :--- |
| **Multi-Agent Engineering Harness** | Parallel AI coding agents on isolated lanes across WezTerm. Cross-family review: the model family that writes a change does not approve it. Every commit passes `cargo fmt`, `clippy::pedantic -D warnings`, the test suite and a secret and personal-data scan before it lands. | `Rust` · `Git` · `WezTerm` |
| **Financial & OCR Reconciliation Engine** | Monthly sales packets, statement and receipt OCR, reconciled to the exact cent in `i64` with zero floating-point drift; every number traces back to its source page. | `Rust` · `DataFusion` · `redb` · `OCR` |
| **Bare-Metal Performance Lab** | Roofline measurement on our own hardware: streaming bandwidth, FMA throughput and the ridge point, used to pick quantization (q4/q8/fp16) and kernel fusion for local model inference. | `Rust` · `Metal` |
| **Proven Money** | `Lean 4` specification of the currency core: cents conserved across N-way splits, half-up rounding bounds, no `i64` overflow. Machine-checked proofs underway; target year-end 2026. | `Lean 4` · `Rust` |
| **Field Operations & Property Platform** | Rental property operations: work orders, labor-hour ledgers, receipts and expenses on embedded ACID transactional storage. | `Rust` · `redb` |

### `03 // DOCTRINE`

```text
01. MEASURE BEFORE CLAIMING   :: working code and a verified result are different states.
                                 done means it ran and was checked against ground truth.
02. ADVERSARIAL VERIFICATION  :: the model family that writes a change never approves it.
                                 compiler, lint and privacy gates fail closed.
03. ZERO-FLOAT LEDGERS        :: money is i64 integer cents, being proven in Lean 4.
                                 floating point is forbidden on financial paths.
04. SCAR-DRIVEN AUTOMATION    :: every bug becomes a regression test.
                                 every repeated failure becomes a permanent gate.
05. SHIP DAILY                :: small verified increments, every day, no unverified merges.
```

---

<div align="center">

**[goroshillc.com](https://goroshillc.com/) · [LinkedIn](https://www.linkedin.com/in/stefano-theofanous) · contact@goroshillc.com**

<sub>Colossians 3:23 · Α ☧ Ω · ICXC NIKA</sub>

</div>

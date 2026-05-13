# Autonomous-RedAgent

[![CI](https://github.com/Popoo2020/Autonomous-RedAgent/actions/workflows/ci.yml/badge.svg)](https://github.com/Popoo2020/Autonomous-RedAgent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Autonomous-RedAgent** is a safety-first red-team automation lab for **authorised reconnaissance planning**.  
The current implementation deliberately focuses on **scope enforcement**, **allowlist validation**, and **non-destructive recon plan generation** rather than exploitation logic.

> **Status:** working safety-oriented baseline / active expansion.  
> This repository is designed for ethical research, authorised testing, and portfolio demonstration.

## What is implemented

| Capability | Status |
|---|---|
| Exact target allowlist matching | ✅ Implemented |
| Wildcard scope matching | ✅ Implemented |
| Out-of-scope target blocking | ✅ Implemented |
| Safe recon plan generation | ✅ Implemented |
| Deterministic pytest coverage | ✅ Implemented |
| CI that enforces safety/scope tests | ✅ Implemented |
| Actual recon execution runners | 🟡 Planned |
| Plugin registry and module interface | 🟡 Planned |
| Structured findings report | 🟡 Planned |
| CVE enrichment layer | 🟡 Planned |

## Design philosophy

The repository is intentionally built around a simple principle:

> **Automation should not act before scope is verified.**

For that reason, the first implemented layer is not exploitation, scanning volume, or payload generation.  It is the **safety gate** that determines whether a target is authorised and whether a safe recon plan may even be prepared.

## Repository structure

```text
src/
  scope.py                    # Allowlist and target scope decisions
  recon.py                    # Safe recon-plan builder

tests/
  test_scope_and_recon.py     # Scope enforcement and safe-mode tests

requirements.txt
.github/workflows/ci.yml
```

## Implemented modules

### `src/scope.py`
Provides:

- hostname normalisation
- exact allowlist matching
- wildcard matching such as `*.lab.example.com`
- deterministic `ScopeDecision` objects

### `src/recon.py`
Provides:

- `build_recon_plan()`
- explicit allowlist gate before any action planning
- safe, non-destructive action list placeholders:
  - `dns_lookup`
  - `http_head_request`
  - `tls_metadata_review`

The function currently **prepares** an auditable plan; it does **not** execute network activity.

## Quickstart

```bash
git clone https://github.com/Popoo2020/Autonomous-RedAgent.git
cd Autonomous-RedAgent

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pytest -q
```

## Example

```python
from src.recon import build_recon_plan

plan = build_recon_plan(
    target="lab.example.com",
    allowlist=["lab.example.com", "*.lab.example.com"],
    safe_mode=True,
)

print(plan)
```

## Safety guarantees in the current baseline

- targets outside the allowlist are rejected
- empty allowlists fail closed
- current code generates plans only; it does not conduct active scanning
- CI validates that out-of-scope targets are blocked

## Roadmap

1. Add a formal plugin interface for authorised recon modules
2. Add read-only execution runners for DNS/HTTP/TLS metadata collection
3. Produce structured JSON findings reports
4. Add rules-of-engagement configuration files
5. Add CVE enrichment only for explicitly authorised and identified services
6. Add audit-log examples and clearer operator prompts

## Limitations

- This is not a finished autonomous red-team platform
- It does not yet execute recon actions against targets
- It does not generate payloads or perform exploitation
- The present value is in demonstrating **safe automation architecture**, **scope control**, and a responsible implementation path

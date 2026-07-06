# Threat Model

## Scope

This threat model covers the current safety-first implementation: target normalisation, allowlist evaluation, non-destructive reconnaissance plan generation, tests and CI validation. It does not cover future active network execution modules.

## Assets

- Authorised target allowlists.
- Target input and normalised hostnames.
- Recon plan outputs.
- Safety and scope tests.
- CI workflows and dependency manifests.

## Trust boundaries

1. User-supplied target input to target normalisation.
2. Allowlist configuration to scope decision.
3. Scope decision to recon plan generation.
4. Future plan output to any execution layer.
5. Repository changes to CI and security checks.

## Primary risks and controls

| Risk | Impact | Existing control | Additional note |
|---|---|---|---|
| Out-of-scope target planning | Unauthorised recon preparation | Allowlist gate and fail-closed tests | Future execution must re-check scope. |
| Empty or malformed allowlist | Accidental broad access | Empty allowlists fail closed | Add validation for future config formats. |
| Wildcard overreach | Broader target scope than intended | Wildcard tests cover intended subdomain matching | Add more edge-case tests as patterns expand. |
| Active execution added later without approval | Unauthorised scanning | Current code does not execute network activity | Future runners need rules-of-engagement checks. |
| False safety claims | Misuse of portfolio demo | README and SECURITY.md state limitations | Keep documentation conservative. |
| Dependency or CI regression | Broken safety validation | ruff, pytest, pip-audit and CodeQL | Keep checks required before merging. |

## Security invariants

- Out-of-scope targets must not receive recon actions.
- Empty allowlists must fail closed.
- Current implementation must not perform active network activity.
- Future execution modules must re-check scope before running.
- Tests must cover allow, deny and fail-closed paths.

## Out of scope

- Real target authorisation verification.
- Active scanning, exploitation or payload generation.
- Durable operator approval workflows.
- Production red-team orchestration.

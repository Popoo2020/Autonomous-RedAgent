# Security Policy

## Purpose

Autonomous-RedAgent is a safety-first red-team automation lab for authorised reconnaissance planning. The current implementation is intentionally limited to scope validation and non-destructive plan generation.

## Supported use

Use this repository only for:

- educational review,
- authorised security research,
- local demonstrations,
- portfolio evaluation,
- controlled internal experiments.

It is not a production red-team platform and must not be used for unauthorised scanning, exploitation, persistence, evasion or payload delivery.

## Safety posture

The project is designed around conservative controls:

- targets must pass an allowlist gate before any plan is generated,
- out-of-scope targets fail closed,
- empty allowlists fail closed,
- current code generates plans only and does not execute network activity,
- CI validates safety and scope behaviour,
- CodeQL and dependency checks should remain enabled.

## Reporting security issues

If you find a security-relevant issue, open a GitHub issue with:

1. the affected file or behaviour,
2. why the behaviour could create risk,
3. a minimal reproduction case,
4. whether the issue affects tests, documentation or runtime logic.

Do not include real credentials, private targets, customer data, exploit payloads or sensitive third-party information.

## Known limitations

- This is not a complete autonomous red-team platform.
- It does not currently execute recon actions.
- It does not include a durable rules-of-engagement workflow.
- It does not perform external authorisation verification.
- Future active modules must preserve the allowlist and approval gates before execution.

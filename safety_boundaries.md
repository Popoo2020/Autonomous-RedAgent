# Safety Boundaries

This document defines the safety boundaries and rules of engagement for running **Autonomous‑RedAgent** in a controlled environment. The goal is to prevent misuse and ensure that all activities are authorized and ethical.

## Scope & Rules of Engagement

1. **Authorized Targets Only:** The agent must operate exclusively against systems and networks for which explicit permission has been granted. Targets should be defined via an allowlist configuration.
2. **Safe Mode by Default:** The default mode of operation is reconnaissance‑only. Exploitation or payload delivery functions must be explicitly enabled by a user with appropriate authority.
3. **Data Handling:** Collected data (service banners, CVEs, screenshots) must be stored securely and deleted after the engagement. Sensitive data discovered inadvertently should be reported and purged.
4. **No Persistence:** The agent shall not attempt to establish persistence on targets or deploy long‑lived agents.
5. **Audit Logging:** All actions taken by the agent—including targets, timestamps and modules used—must be logged for post‑engagement review.
6. **Legal Compliance:** Users of this tool are responsible for ensuring compliance with applicable laws and regulations in their jurisdiction.
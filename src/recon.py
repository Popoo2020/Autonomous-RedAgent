"""Safe, non-destructive reconnaissance helpers for Autonomous-RedAgent.

The implementation deliberately avoids exploitation logic.  It only produces
normalised recon plans after a target passes the allowlist check.
"""
from __future__ import annotations

from dataclasses import asdict
from typing import Any

from .scope import ScopeDecision, is_target_allowed


SAFE_RECON_ACTIONS = (
    "dns_lookup",
    "http_head_request",
    "tls_metadata_review",
)


def build_recon_plan(target: str, allowlist: list[str], safe_mode: bool = True) -> dict[str, Any]:
    """Build a constrained recon plan for an authorised target.

    This function does not execute network activity.  It prepares a validated,
    auditable plan that a future runner can consume under explicit rules of
    engagement.
    """
    decision: ScopeDecision = is_target_allowed(target, allowlist)
    if not decision.allowed:
        return {
            "target": decision.target,
            "allowed": False,
            "safe_mode": safe_mode,
            "reason": decision.reason,
            "actions": [],
        }

    actions = list(SAFE_RECON_ACTIONS) if safe_mode else list(SAFE_RECON_ACTIONS)
    return {
        "target": decision.target,
        "allowed": True,
        "safe_mode": safe_mode,
        "reason": decision.reason,
        "actions": actions,
        "scope_decision": asdict(decision),
    }

"""Scope validation primitives for the Autonomous-RedAgent lab.

This module provides a deterministic allowlist gate for targets.  It is
intentionally conservative and suitable for educational / authorised demo use.
"""
from __future__ import annotations

from dataclasses import dataclass
from fnmatch import fnmatch
from urllib.parse import urlparse


@dataclass(frozen=True)
class ScopeDecision:
    target: str
    allowed: bool
    reason: str


def _normalise_target(target: str) -> str:
    candidate = target.strip()
    if not candidate:
        raise ValueError("target must not be empty")
    parsed = urlparse(candidate if "://" in candidate else f"https://{candidate}")
    host = parsed.hostname or candidate
    return host.lower().strip(".")


def is_target_allowed(target: str, allowlist: list[str]) -> ScopeDecision:
    """Return whether a host is inside the configured allowlist.

    Supports exact hostnames and wildcard patterns such as `*.example.com`.
    """
    host = _normalise_target(target)
    patterns = [entry.lower().strip() for entry in allowlist if entry.strip()]
    if not patterns:
        return ScopeDecision(target=host, allowed=False, reason="allowlist_empty")

    for pattern in patterns:
        if fnmatch(host, pattern):
            return ScopeDecision(target=host, allowed=True, reason=f"matched:{pattern}")
    return ScopeDecision(target=host, allowed=False, reason="outside_allowlist")

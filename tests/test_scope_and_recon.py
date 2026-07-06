from src.recon import build_recon_plan
from src.scope import is_target_allowed


def test_exact_allowlist_match_is_allowed() -> None:
    decision = is_target_allowed("https://lab.example.com", ["lab.example.com"])
    assert decision.allowed is True
    assert decision.reason == "matched:lab.example.com"


def test_wildcard_allowlist_match_is_allowed() -> None:
    decision = is_target_allowed("api.lab.example.com", ["*.lab.example.com"])
    assert decision.allowed is True


def test_out_of_scope_target_is_blocked() -> None:
    decision = is_target_allowed("outside.example.net", ["lab.example.com"])
    assert decision.allowed is False
    assert decision.reason == "outside_allowlist"


def test_empty_allowlist_fails_closed() -> None:
    decision = is_target_allowed("lab.example.com", [])
    assert decision.allowed is False
    assert decision.reason == "allowlist_empty"


def test_recon_plan_is_empty_when_target_is_out_of_scope() -> None:
    plan = build_recon_plan("outside.example.net", ["lab.example.com"])
    assert plan["allowed"] is False
    assert plan["actions"] == []


def test_safe_recon_plan_contains_only_safe_actions() -> None:
    plan = build_recon_plan("lab.example.com", ["lab.example.com"], safe_mode=True)
    assert plan["allowed"] is True
    assert plan["safe_mode"] is True
    assert plan["actions"] == [
        "dns_lookup",
        "http_head_request",
        "tls_metadata_review",
    ]

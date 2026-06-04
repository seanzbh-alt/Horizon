from src.ai.prompts import CONTENT_ANALYSIS_SYSTEM


def test_analysis_prompt_targets_used_car_industry() -> None:
    prompt = CONTENT_ANALYSIS_SYSTEM.lower()

    assert "used-car" in prompt
    assert "software engineering, ai/ml, and systems research" not in prompt


def test_analysis_prompt_limits_general_auto_news_without_used_car_impact() -> None:
    prompt = CONTENT_ANALYSIS_SYSTEM.lower()

    assert "general auto" in prompt
    assert "cannot score above 5" in prompt
    assert "used-car or auto-retail impact" in prompt


def test_analysis_prompt_caps_context_only_auto_news_below_direct_used_car_items() -> None:
    prompt = CONTENT_ANALYSIS_SYSTEM.lower()

    assert "direct used-car" in prompt
    assert "context-only auto news" in prompt
    assert "cap it at 6" in prompt

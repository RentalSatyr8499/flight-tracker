"""test price rules and duplicate alert behavior."""


def test_absolute_price_threshold() -> None:
    """match offers at or below the configured price."""
    raise NotImplementedError


def test_price_drop_threshold() -> None:
    """match a drop relative to the previous comparable observation."""
    raise NotImplementedError


def test_alert_key_is_stable() -> None:
    """produce the same key for the same offer and rule."""
    raise NotImplementedError

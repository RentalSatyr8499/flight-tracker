"""evaluate configured price rules independently of discord."""

from flight_tracker.history import PriceHistory
from flight_tracker.models import AlertEvent, FlightOffer


def evaluate_thresholds(
    offers: list[FlightOffer],
    rules: list[dict],
    history: PriceHistory,
) -> list[AlertEvent]:
    """return offers that meet absolute-price or price-drop rules."""
    raise NotImplementedError


def build_alert_key(event: AlertEvent) -> str:
    """build a stable key for duplicate-alert suppression."""
    raise NotImplementedError

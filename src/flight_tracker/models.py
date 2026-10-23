"""define provider-independent flight and price records."""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(frozen=True)
class FlightQuery:
    """describe one origin, destination, and travel date pair."""

    origin: str
    destination: str
    departure_date: str
    return_date: str
    adults: int = 1
    cabin: str = "economy"
    currency: str = "USD"


@dataclass(frozen=True)
class FlightOffer:
    """normalize an itinerary and its observed price."""

    offer_id: str
    query: FlightQuery
    price: Decimal
    currency: str
    booking_url: str | None = None
    stops: int | None = None
    airline_names: tuple[str, ...] = ()


@dataclass(frozen=True)
class PriceObservation:
    """represent one timestamped offer observation."""

    offer: FlightOffer
    observed_at: datetime


@dataclass(frozen=True)
class AlertEvent:
    """describe a threshold match that may need a discord mention."""

    rule_name: str
    offer: FlightOffer
    reason: str

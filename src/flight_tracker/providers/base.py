from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class FlightOffer:
    origin: str
    destination: str
    departure_date: str
    return_date: str
    price: float
    currency: str
    booking_url: str = ""
    airline_summary: str = ""


class FlightProvider(Protocol):
    def search(self, origin: str, destination: str, departure_date: str,
               return_date: str, currency: str) -> list[FlightOffer]:
        """Return normalized round-trip offers for a route and date pair."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Listing:
    id: int
    name: str
    host_id: int
    host_name: str
    neighbourhood_group: str
    neighbourhood: str
    latitude: float
    longitude: float
    room_type: str
    price: Optional[float]
    minimum_nights: int
    number_of_reviews: int
    last_review: Optional[str]
    reviews_per_month: Optional[float]
    calculated_host_listings_count: int
    availability_365: int
    number_of_reviews_ltm: str
    license: Optional[str]


@dataclass
class Neighbourhood:
    neighbourhood_group: str
    neighbourhood: str


@dataclass
class Review:
    listing_id: int
    date: str

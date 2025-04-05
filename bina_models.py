from dataclasses import dataclass
from typing import Optional


@dataclass
class Listing:
    id: int
    name: str
    host_id: int
    host_name: str
    neighbourhood_group_cleansed: str
    neighbourhood_cleansed: str
    latitude: float
    longitude: float
    property_type: str
    room_type: str
    accommodates: int
    bathrooms: Optional[float]
    bathrooms_text: Optional[str]
    bedrooms: Optional[int]
    beds: Optional[int]
    price: Optional[float]
    minimum_nights: int
    number_of_reviews: int
    last_review: Optional[str]
    review_scores_rating: Optional[float]
    reviews_per_month: Optional[float]
    calculated_host_listings_count: int
    availability_365: int
    number_of_reviews_ltm: str
    license: Optional[str]

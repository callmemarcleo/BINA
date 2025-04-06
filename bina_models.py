from dataclasses import dataclass
from typing import Optional


@dataclass
class Listing:
    id: int
    listing_url: str
    scrape_id: int
    last_scraped: str
    source: str
    name: str
    description: str
    neighborhood_overview: str
    picture_url: str
    host_id: int
    host_url: str
    host_name: str
    host_since: str
    host_location: str
    host_about: str
    host_response_time: str
    host_response_rate: str
    host_acceptance_rate: str
    host_is_superhost: str
    host_thumbnail_url: str
    host_picture_url: str
    host_neighbourhood: str
    host_listings_count: int
    host_total_listings_count: int
    host_verifications: str
    host_has_profile_pic: str
    host_identity_verified: str
    neighbourhood: str
    neighbourhood_cleansed: str
    neighbourhood_group_cleansed: str
    latitude: float
    longitude: float
    property_type: str
    room_type: str
    accommodates: int
    bathrooms: str
    bathrooms_text: str
    bedrooms: str
    beds: str
    amenities: list[str]
    price: str
    minimum_nights: int
    maximum_nights: int
    minimum_minimum_nights: int
    maximum_minimum_nights: int
    minimum_maximum_nights: int
    maximum_maximum_nights: int
    minimum_nights_avg_ntm: float
    maximum_nights_avg_ntm: str
    calendar_updated: str
    has_availability: str
    availability_30: str
    availability_60: str
    availability_90: str
    availability_365: str
    calendar_last_scraped: str
    number_of_reviews: str
    number_of_reviews_ltm: str
    number_of_reviews_l30d: str
    first_review: str
    last_review: str
    review_scores_rating: str
    review_scores_accuracy: str
    review_scores_cleanliness: str
    review_scores_checkin: str
    review_scores_communication: str
    review_scores_location: str
    review_scores_value: str
    license: str
    instant_bookable: str
    calculated_host_listings_count: int
    calculated_host_listings_count_entire_homes: str
    calculated_host_listings_count_private_rooms: str
    calculated_host_listings_count_shared_rooms: str
    reviews_per_month: str
    missing_data_flag: bool




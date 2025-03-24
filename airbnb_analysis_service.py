from bina_models import Listing, Review, Neighbourhood
from db_client_handler import SupabaseClient


class AirbnbAnalysisService:
    def __init__(self):
        """
            Initialises the FastAPI application with CORS (for Angular) and API routes
        """
        self.supabase_client = SupabaseClient().get_client()

    def get_listings(self):
        raw_listings = self.supabase_client.table("listings").select("*").execute().data
        listings: list[Listing] = [Listing(**item) for item in raw_listings]

        return listings

    def get_neighbourhoods(self):
        raw_neighbourhoods = self.supabase_client.table("neighbourhoods").select("*").execute().data
        neighbourhoods: list[Neighbourhood] = [Neighbourhood(**item) for item in raw_neighbourhoods]

        return neighbourhoods

    def get_reviews(self):
        raw_reviews = self.supabase_client.table("reviews").select("*").execute().data
        reviews: list[Review] = [Review(**item) for item in raw_reviews]

        return reviews

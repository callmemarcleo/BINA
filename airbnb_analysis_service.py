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

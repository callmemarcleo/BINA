from bina_models import Listing, SellingPrices
from db_client_handler import SupabaseClient


class AirbnbAnalysisService:
    def __init__(self):
        """
            Initialises the FastAPI application with CORS (for Angular) and API routes
        """
        self.supabase_client = SupabaseClient().get_client()

    def get_listings(self):
        raw_listings = self.supabase_client.table("cleaned_listings").select("*").execute().data
        listings: list[Listing] = [Listing(**item) for item in raw_listings]

        return listings

    def get_selling_prices(self):
        raw_selling_prices = self.supabase_client.table("cleaned_selling_prices").select("*").execute().data
        selling_prices: list[SellingPrices] = [SellingPrices(**item) for item in raw_selling_prices]

        return selling_prices

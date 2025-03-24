import json

from db_client_handler import SupabaseClient


class AirbnbAnalysisBINA:
    def __init__(self):
        """
            Initialises the FastAPI application with CORS (for Angular) and API routes
        """
        self.supabase_client = SupabaseClient().get_client()


if __name__ == "__main__":
    airbnbBina = AirbnbAnalysisBINA()
    listings = airbnbBina.supabase_client.table("listings").select("*").execute()

    print(listings)


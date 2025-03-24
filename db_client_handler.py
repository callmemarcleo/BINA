import os
from supabase import create_client
from dotenv import load_dotenv


class SupabaseClient:
    def __init__(self):
        """
            Initialises the connection to Supabase by loading the environment variables
        """
        load_dotenv()
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        self.client = create_client(self.url, self.key)

    def get_client(self):
        return self.client

from supabase import create_client, Client
import config


supabase_client: Client = create_client(
    config.SUPABASE_API_URL, config.SUPABASE_API_KEY
)


def get_supabase_client():
    return supabase_client

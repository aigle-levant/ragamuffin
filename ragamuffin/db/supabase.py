
# file imports
from ragamuffin.config.secrets import SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY
# module imports
from supabase import create_client, Client

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
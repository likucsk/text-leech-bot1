import os

API_ID    = os.environ.get("API_ID", "24981915")
API_HASH  = os.environ.get("API_HASH", "bbafb67e1e87fc1ad1ab339b9c3077f9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6108800540:AAEbjlRpsoVtY6eIWVn0a550JwRLfZmvN0o") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 6969))  # Default to 8000 if not set

import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "24731191"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "ca156f58ad03bb5e350c855bb82e9991")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "5435086550"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs

#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "37166634"))
API_HASH = environ.get("API_HASH", "36ffee547af7f9eca0a24be19aa7ad30")
BOT_TOKEN = environ.get("BOT_TOKEN", "8433913568:AAFRPshrSIBhgmHKgFoXv4F7ZKjOtTWNzpc")
OWNER = int(environ.get("OWNER", "5799395577"))
CREDIT = environ.get("CREDIT", "💫『 @OHITGOAT 』💫")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5799395577').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5799395577').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set













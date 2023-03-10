from os import environ
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(environ.get("APP_ID", "7784110")),
    api_hash= environ.get("API_HASH", "f81b6478f985c1283fa8c4847d1860ec"),
    bot_token= environ.get("TOKEN", "6269625401:AAGhbFsMTmwFWfQdW7LWDtjWodrTF9rOdwg")
)

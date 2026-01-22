
import requests
from requests.auth import HTTPBasicAuth
import os


EXOTEL_SID = os.getenv("EXOTEL_SID")
EXOTEL_TOKEN = os.getenv("EXOTEL_TOKEN")
EXOTEL_NUMBER = os.getenv("EXOTEL_NUMBER")

def make_call(to_number):
    url = f"https://api.exotel.com/v1/Accounts/{EXOTEL_SID}/Calls/connect.json"

    data = {
        "From": EXOTEL_NUMBER,
        "To": to_number,
        "CallerId": EXOTEL_NUMBER,
        "Url": "https://ai-telecaller.onrender.com/voice"
    }

    response = requests.post(
        url,
        data=data,
        auth=HTTPBasicAuth(EXOTEL_SID, EXOTEL_TOKEN),
        timeout=20
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)

# 👉 CALL HERE

make_call("6204529785")   # test local number

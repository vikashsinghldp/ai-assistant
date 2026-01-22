
import requests
from requests.auth import HTTPBasicAuth

EXOTEL_SID = "visionsoftcloud1"
EXOTEL_TOKEN = "273b377b26b7ccdf26e9e24d1c4c752f707cfe294de9add9"
EXOTEL_NUMBER = "09513886363"   # your Exotel virtual number

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
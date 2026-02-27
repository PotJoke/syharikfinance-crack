import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth = "" #YOUR TOKEN
cookie = "" #YOUR COOKIE

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0",
    "Cookie": str({cookie}),
    "Authorization": str({auth})
}

amount = {
    "amount":"15"
}

url = "XXX/api/me/gems" #URL HIDDEN

try:
    while True:
        response = requests.post(url, headers=headers, json=amount, verify=False)
        print(f"RESPONSE: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"ERROR OCCURED: {e}")
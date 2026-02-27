import requests
from config import auth_token, url

headers = {
    "Authorization": auth_token
}

amount = {
    "amount":10
}

r= requests.get(r'http://jsonip.com')
print('Your IP is {}'.format(r.json()['ip']))

try:
    while True:
            counter = 12

            for urls in {"/api/runs/start", "/api/runs/finish", "/api/runs/unlock"}:
                for code in {"bike_dream", "money_quiz", "lemonade_business", "investment_race"}:
                    resp = requests.post(url+urls, headers=headers, json={"scenarioCode": code})
                    print("Requests left: " + str(counter))
                    counter-=1

            print("CASH OUT: " + requests.post(url+"/api/me/gems", headers=headers, json=amount).text + "\n")

except Exception as e:
    print(f"ERROR OCCURED: {e}")
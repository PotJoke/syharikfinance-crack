import requests
from tor_proxy import tor_proxy
import random
from config import url, auth_token, amount, tor_mode, proxies


def web_init():
    url_check_ip="https://httpbin.org/ip"
    print("REAL IP: " + str(requests.get(url_check_ip).json()))
    if (tor_mode):
        #port=tor_proxy()
        port = 9150
        http_proxy  = f"socks5h://127.0.0.1:{port}"
        https_proxy = f"socks5h://127.0.0.1:{port}"

        proxies = { 
            "http"  : http_proxy, 
            "https" : https_proxy, 
        }

        print("TOR IP: " + str(requests.get(url_check_ip,proxies=proxies).json()))

def register():
    global auth_token

    login = str(random.choice(["user", "finger", "tester"])) + str(random.randint(1,1000000))
    email = login + "@example.com"
    password = "123456"

    print(f"REGISTERING NEW ACCOUNT: {login}:{password}")
    
    resp = requests.post(url+"/api/auth/register", 
                         json={"login":login,"name":login,"email":email,"password":password},
                         proxies=proxies if tor_mode else None)
    code = str(resp.json().get("devCode"))

    resp = requests.post(url+"/api/auth/verify", 
                         json={"email": email, "code": code},
                         proxies=proxies if tor_mode else None)

    resp = requests.post(url+"/api/auth/login", 
                         json={"loginOrEmail":login,"password":password},
                         proxies=proxies if tor_mode else None)
    
    auth_token = str("Bearer " + resp.json().get("token"))

def farm():
    try:
        counter = 12

        for urls in {"/api/runs/start", "/api/runs/finish", "/api/runs/unlock"}:
            for code in {"bike_dream", "money_quiz", "lemonade_business", "investment_race"}:  
                resp = requests.post(url+urls, 
                                     headers={"Authorization": auth_token}, 
                                     json={"scenarioCode": code}, 
                                     proxies=proxies if tor_mode else None)

                print("Requests left: " + str(counter))
                counter-=1

        resp = requests.post(url+"/api/me/gems", 
                             headers={"Authorization": auth_token}, 
                             json=amount,
                             proxies=proxies if tor_mode else None)
        
        if resp.text == "{\"message\":\"Unauthorized\"}":
            print("UNAUTHORIZED!")
            register()
            
        print("CASH OUT: " + resp.text + "\n")

    except Exception as e:
        print(f"ERROR OCCURED: {e}")


while True:
    web_init()
    farm()
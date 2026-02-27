import requests
from tor_proxy import tor_proxy
from stem.control import Controller

import threading

import random

from config import url, auth_token, amount 
from config import tor_mode, tor_password, proxies
from config import max_hydras

someshit = 0
hydra_semaphore = threading.Semaphore(max_hydras)

def web_init():
    url_check_ip="https://httpbin.org/ip"
    #print("REAL IP: " + str(requests.get(url_check_ip).json()))
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

def change_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password=tor_password)
            controller.signal('NEWNYM')
            print("Запрос на смену IP отправлен.")
    except Exception as e:
        print(f"Ошибка при смене IP через Tor: {e}")

def check_ban():
    if requests.post(url+"/api/health").status_code == 403:
        change_tor_ip()

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
    while True:
        for urls in {"/api/runs/start", "/api/runs/finish", "/api/runs/unlock"}:
            for code in {"bike_dream", "money_quiz", "lemonade_business", "investment_race"}:  
                resp = requests.post(url+urls, 
                                    headers={"Authorization": auth_token}, 
                                    json={"scenarioCode": code}, 
                                    proxies=proxies if tor_mode else None)


        resp = requests.post(url+"/api/me/gems", 
                            headers={"Authorization": auth_token}, 
                            json=amount,
                            proxies=proxies if tor_mode else None)
            
        if resp.text == "{\"message\":\"Unauthorized\"}":
            print("UNAUTHORIZED!")
            if is_hydra:
                return False
            else:
                register()

        print("CASH OUT: " + resp.text + "\n")
        check_ban()

def counter():
    global someshit
    someshit+=1
    print(someshit)
    return False

def hydra():
    if not hydra_semaphore.acquire(blocking=False):
        hydra_semaphore.acquire()
    try:
        register()
        success = farm()
        if not success:
            t1 = threading.Thread(target=hydra)
            t2 = threading.Thread(target=hydra)
            t1.start()
            t2.start()
    finally:
        hydra_semaphore.release()

if __name__ == "__main__":
    web_init()
    is_hydra = str(input("Run in Hydra? (y/n): ")).lower() == "y"
    if is_hydra:
        threading.Thread(target=hydra).start()
    else:
        while True:
            farm()
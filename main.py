import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0",
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://admin107.fvds.ru/admin",
    "Content-Type": "application/json",
    "Authorization": "..." #YOUR TOKEN
}

restart_url = "https://admin107.fvds.ru/api/runs/restart"
finish_url = "https://admin107.fvds.ru/api/runs/finish"

restart_data = {
    "scenarioCode": "bike_dream"
}

finish_data = {
    "scenarioCode": "bike_dream",
    "status": "passed",
    "finalBudget": 5001,
    "earned": 4001,
    "spent": 0
}

finish_data2 = {
    "scenarioCode": "bike_dream",
    "status": "failed",
    "finalBudget": 4999,
    "earned": 3999,
    "spent": 0
}

try:
    while True:
        response_restart = requests.post(restart_url, headers=headers, json=restart_data, verify=False)
        print(f"RESPONSE: {response_restart.status_code}")
        print(response_restart.text)

        response_finish = requests.post(finish_url, headers=headers, json=finish_data, verify=False)
        print(f"RESPONSE: {response_finish.status_code}")
        print(response_finish.text)

        response_restart = requests.post(restart_url, headers=headers, json=restart_data, verify=False)
        print(f"RESPONSE: {response_restart.status_code}")
        print(response_restart.text)

        response_finish = requests.post(finish_url, headers=headers, json=finish_data2, verify=False)
        print(f"RESPONSE: {response_finish.status_code}")
        print(response_finish.text)

except Exception as e:
    print(f"ERROR OCCURED: {e}")
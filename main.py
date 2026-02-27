import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth = "" #YOUR AUTH TOKEN HERE
cookie = "" #YOUR COOKIE HERE

headers = {
    "Cookie": str({cookie}),
    "Authorization": str({auth})
}

url = "" #URL HIDDEN DUE TO COMPETITION RULES

restart_url = f"{url}/api/runs/restart"
finish_url = f"{url}/api/runs/finish"

scenarioCode = "bike_dream"

restart_data = {
    "scenarioCode": f"{scenarioCode}"
}

finish_data = {
    "scenarioCode": f"{scenarioCode}",
    "status": "passed",
    "finalBudget": 5001,
    "earned": 4001,
    "spent": 0
}

finish_data2 = {
    "scenarioCode": f"{scenarioCode}",
    "status": "failed",
    "finalBudget": 4999,
    "earned": 3999,
    "spent": 0
}

try:
    while True:
        response_restart = requests.post(restart_url, headers=headers, json=restart_data, verify=False)
        print(f"RESPONSE: {response_restart.status_code}")
        #print(response_restart.text)

        response_finish = requests.post(finish_url, headers=headers, json=finish_data, verify=False)
        print(f"RESPONSE: {response_finish.status_code}")
        #print(response_finish.text)

        response_restart = requests.post(restart_url, headers=headers, json=restart_data, verify=False)
        print(f"RESPONSE: {response_restart.status_code}")
        print(response_restart.text)

        response_finish = requests.post(finish_url, headers=headers, json=finish_data2, verify=False)
        print(f"RESPONSE: {response_finish.status_code}")
        print(response_finish.text)

except Exception as e:
    print(f"ERROR OCCURED: {e}")
import requests
import json



def fetch_launches_data():
    url = "https://ll.thespacedevs.com/2.2.0/launch/"
    params = {
        "ordering": "-net",
        "format": "json"
    }

    r =requests.get(url, params=params)


    if r.status_code == 200:
        data = r.json()
        with open("../data/bronze/raw_data.json", "w",) as file:
            json.dump(data, file, indent=4)
        print("data saved")
    else:
        raise Exception(f"Error: : : {r.status_code} : {r.text}")









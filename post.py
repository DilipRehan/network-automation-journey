import requests

url = "https://httpbin.org/post"

payload = {
    "device": "R1",
    "ip": "192.168.1.1",
    "action": "backup",
}


response = requests.post(url, json=payload)


data = response.json()

print(f"Status Code : {response.status_code}")
print(f"Data Send   : {data['json']}")
import requests

url = "https://httpbin.org/put"

payload = {
    "device":"R1",
    "ip":"192.168.1.100",
    "action":"update"
}

response = requests.put(url, json=payload)
data = response.json()

print(f"Status Code : {response.status_code}")
print(f"Data Sent {data['json']}")
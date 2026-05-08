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
print(f"data Sent   : {data['json']}")


response = requests.delete(url, json=payload)
print(f"data deleted: {data['json']}")

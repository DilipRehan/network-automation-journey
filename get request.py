import requests

response = requests.get("https://ipinfo.io/json")

data = response.json()

print(f"Status Code  : {response.status_code}")
print(f"IP Address   : {data['ip']}")
print(f"City         : {data['city']}")
print(f"Country      : {data['country']}")
print(f"ISP          : {data['org']}")

if data['country'] == "GB":
    print("The country is London")
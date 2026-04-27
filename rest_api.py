import requests

response = requests.get("https://ipinfo.io/json")

print(f"Satus Code: {response.status_code}")
print(f"Raw Data  : {response.text}")
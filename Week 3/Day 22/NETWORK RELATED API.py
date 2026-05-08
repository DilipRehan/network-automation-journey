import requests

ip = "8.8.8.8"

response = requests.get(f"http://ip-api.com/json/{ip}")
data = response.json()

print("=" * 40)
print(f"IP LOOKUP — {ip}")
print("=" * 40)
print(f"IP        : {data['query']}")
print(f"City      : {data['city']}")
print(f"Country   : {data['country']}")
print(f"ISP       : {data['isp']}")
print(f"Timezone  : {data['timezone']}")
print("=" * 40)
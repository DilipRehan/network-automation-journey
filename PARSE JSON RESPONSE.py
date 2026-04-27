import requests

response = requests.get("https://ipinfo.io/json")
data = response.json()

print("=" * 40)
print("MY NETWORK INFO")
print("=" * 40)
print(f"IP Address : {data['ip']}")
print(f"City       : {data['city']}")
print(f"Region     : {data['region']}")
print(f"Country    : {data['country']}")   # ← country
print(f"ISP        : {data['org']}")       # ← org
print(f"Timezone   : {data['timezone']}") # ← timezone
print("=" *40)
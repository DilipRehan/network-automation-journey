import requests
import urllib3

urllib3.disable_warnings()

# Get token
auth_url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
token = requests.post(auth_url, auth=("devnetuser", "Cisco123!"), verify=False).json()['Token']
print("Token received ✅")

headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

# Device ID from Task 1
device_id = "aa754801-8895-41e8-8ca5-27ee415c9c42"

# Get interfaces
url = f"https://sandboxdnac.cisco.com/dna/intent/api/v1/interface/network-device/{device_id}"
response = requests.get(url, headers=headers, verify=False)
interfaces = response.json()['response']

print(f"\nTotal Interfaces: {len(interfaces)}")
print("=" * 45)

for intf in interfaces[:5]:  # first 5 only
    print(f"Interface : {intf['portName']}")
    print(f"Status    : {intf['status']}")
    print(f"Speed     : {intf['speed']}")
    print("-" * 30)
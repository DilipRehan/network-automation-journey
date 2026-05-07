import requests
import urllib3

urllib3.disable_warnings()

# Get token
auth_url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
token = requests.post(auth_url, auth=("devnetuser", "Cisco123!"), verify=False).json()['Token']
print("Token received ✅ ")

# Get device list
devices_url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
headers = {"X-Auth-Token":token, "Content-Type":"application/json"}


response = requests.get(devices_url, headers=headers, verify=False)
devices = response.json()['response']

# Print first device full details
device = devices[0]
print("\n" + "=" * 45)
print("DEVICE DETAILS")
print("=" * 45)
for key, value in device.items():
    print(f"{key:35} : {value}")
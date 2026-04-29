import requests
import urllib3

urllib3.disable_warnings()

# Step 1 — Get token
auth_url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
auth_response = requests.post(
    auth_url,
    auth=("devnetuser", "Cisco123!"),
    verify=False
)
token = auth_response.json()['Token']
print(f"Token received ✅")


devices_url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
header = {
    "X-Auth-Token":token,
    "Content-Type":"application/json"
}




response = requests.get(devices_url, headers=header,verify=False )
data = response.json()


print(f"Status Code: {response.status_code} ✅")
print(f" Totlal Devices: {len(data['response'])}")
print("=" * 30)

for device in data['response']:
    print(f"Hostname  : {device['hostname']}")
    print(f"IP       : {device['managementIpAddress']}")
    print(f"Type     : {device['type']}")
    print("=" *30)
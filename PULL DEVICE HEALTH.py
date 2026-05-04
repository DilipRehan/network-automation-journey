import requests
import urllib3
from datetime import datetime

urllib3.disable_warnings()

# Get token
auth_url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
token = requests.post(auth_url, auth=("devnetuser", "Cisco123!"), verify=False).json()['Token']
print("Token received ✅")

headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

# Get devices
devices_url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
devices = requests.get(devices_url, headers=headers, verify=False).json()['response']

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("\n" + "=" * 50)
print("       NETWORK INVENTORY REPORT")
print(f"       Generated: {timestamp}")
print("=" * 50)

for device in devices:
    print(f"\nHostname  : {device['hostname']}")
    print(f"IP        : {device['managementIpAddress']}")
    print(f"Type      : {device['type']}")
    print(f"Version   : {device['softwareVersion']}")
    print(f"Status    : {device['reachabilityStatus']}")
    print(f"Uptime    : {device['upTime']}")
    print("-" * 40)

print(f"\nTotal Devices : {len(devices)}")
print("=" * 50)

# Save to file
filename = f"inventory_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
with open(filename, "w") as f:
    f.write(f"Network Inventory Report - {timestamp}\n")
    f.write("=" * 50 + "\n")
    for device in devices:
        f.write(f"Hostname : {device['hostname']}\n")
        f.write(f"IP       : {device['managementIpAddress']}\n")
        f.write(f"Status   : {device['reachabilityStatus']}\n")
        f.write("-" * 40 + "\n")

print(f"\nReport saved to {filename} ✅")
import requests
import urllib3

urllib3.disable_warnings()

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

response = requests.post(
    url,
    auth=("devnetuser","Cisco123!"),
    verify = False
)


print(f"Status Code : {response.status_code}")
data = response.json()
token = data['Token']
print(f"Token  : {token[:30]}...")
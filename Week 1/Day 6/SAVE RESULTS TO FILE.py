import subprocess
from  datetime import datetime
def ping_devices(ips):
    results = subprocess.run(["ping", "-n", "2", ips], capture_output=True, text=True)
    if "Destination host unreachable" in results.stdout or "Request timed out" in results.stdout:
        return False
    else:
        return True
    
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

output =open("ping_results.txt", "w", encoding="utf-8")
output.write(f"Network Scan Results - {timestamp}\n")
output.write("=" * 40 + "\n")

# Load IPs from file
file = open("ip_list.txt", "r")
ips = file.read().splitlines()
file.close()


for ip in ips:
    if ping_devices(ip):
        line = f"✅ {ip} - REACHABLE"
    else:
        line = f"❕ {ip} - UNREACHABLE"
    print(line)
    output.write(line + "\n")

output.write("=" * 40 + "\n")
output.close()

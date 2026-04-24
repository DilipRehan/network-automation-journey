import subprocess
from datetime import datetime

# ping_device function — checks if an IP is reachable
def ping_device(ip):
    result = subprocess.run(
        ["ping", "-n", "1", ip],
        capture_output=True,
        text=True
    )
    # check for unreachable or timeout in output
    if "Destination host unreachable" in result.stdout or "Request timed out" in result.stdout:
        return False
    else:
        return True

# Load IPs from ip_list.txt
file = open("ip_list.txt", "r")
ips = file.read().splitlines()
file.close()

# Get current timestamp for the report
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Open output file to save results
output = open("ping_results.txt", "w", encoding="utf-8")
output.write(f"Network Scan Results - {timestamp}\n")
output.write("=" * 40 + "\n")

# Ping each IP and save result
for ip in ips:
    if ping_device(ip):
        line = f"✅ {ip} - REACHABLE"
    else:
        line = f"❕ {ip} - UNREACHABLE"
    print(line)
    output.write(line + "\n")

output.write("=" * 40 + "\n")
output.close()

print("\nResults saved to ping_results.txt")
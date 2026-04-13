import subprocess
import time

ips = ["8.8.8.8", "192.168.1.1", "1.1.1.1", "192.168.1.2", "8.8.4.4"]

def ping_device(ip):
    results = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
    if "Destination host unreachable" in results.stdout or "Request timed out" in results.stdout:
        return False
    else:
        return True

print("=" * 40)
print("Starting scan...\n")

total = len(ips)

results_list = []

for index, ip in enumerate(ips, start=1):
    status = ping_device(ip)
    results_list.append((ip, status))

    # Calculate percentage
    percent = int((index / total) * 100)

    # Show loading progress
    print(f"Progress: {percent}% completed")
    time.sleep(0.3)  # small delay so user can see progress

print("\n" + "=" * 40)
print("FINAL RESULTS:\n")

for ip, status in results_list:
    if status:
        print(f"{ip} - REACHABLE ✅")
    else:
        print(f"{ip} - UNREACHABLE ❕")
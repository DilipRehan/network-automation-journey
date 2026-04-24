import subprocess

def ping_device(ip):
    result = subprocess.run(
        ["ping", "-n", "1", ip],
        capture_output=True,
        text=True
    )
    if "Destination host unreachable" in result.stdout or "Request timed out" in result.stdout:
        return False
    else:
        return True

def scan_network(ip_list):
    reachable = []
    unreachable = []

    for ip in ip_list:
        if ping_device(ip):
            reachable.append(ip)
        else:
            unreachable.append(ip)

    return reachable, unreachable

# Main
ips = ["8.8.8.8", "1.1.1.1", "192.168.1.1", "192.168.1.2", "8.8.4.4"]

reachable, unreachable = scan_network(ips)

print("=" * 40)
print("NETWORK SCAN RESULTS")
print("=" * 40)
print(f"\nREACHABLE ({len(reachable)}):")
for ip in reachable:
    print(f"  ✅ {ip}")

print(f"\nUNREACHABLE ({len(unreachable)}):")
for ip in unreachable:
    print(f"  ❕ {ip}")

print(f"\nTotal scanned: {len(ips)}")
print("=" * 40)
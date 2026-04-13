
ips = ["192.168.1.1", "8.8.8.8", "192.168.1.2", "8.8.4.4"]

def is_reachable(ip):
    if ip.startswith("8."):
        return True
    else:
        return False

for ip in ips:
    if is_reachable(ip):
        print(f"{ip}- REACHABLE ✅")
    else:
        print(f"{ip}- REACHABLE ❕")

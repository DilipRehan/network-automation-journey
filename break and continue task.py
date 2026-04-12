ips = ["192.168.1.1", "192.168.1.2", "UNREACHABLE", "192.168.1.4", "192.168.1.5"]

for ip in ips:
    if ip == "UNREACHABLE": 
        print(f"Skipping bad IP...")
        continue
    print(f"Connecintg to {ip}...")

hostname = ["R1", "R2", "R3", "R4", "R5"]
ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]

print(f"Total routers: {len(hostname)}")
print(f"First router : {hostname[0]} - {ips[0]}")
print(f"Last router: {hostname[4]} - {ips[4]}")

hostname = ["R1", "R2", "R3", "R4", "R5"]
ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]

for i in range (len(hostname)):
    print(f"Router: {hostname[i]} - IP: {ips[i]}")
    
file = open("ip_list.txt", "r")
ips = file.read().splitlines()
file.close()


print(f"Loaded IPs: {len(ips)} IPs")
for ip in ips:
    print(f" - {ip}")

ips = ["192.168.1.1", "1.1.1.1", "192.168.1.2", "8.8.4.4"]

file = open("ip_list.txt", "w+")
for ip in ips:
    file.write(ip + "\n")
file.close()

print("IP_list.text create successfully")
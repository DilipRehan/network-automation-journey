router_Info = ("R1", "192.168.1.1", "Cisco", "IOS 15.4")

print(f"Hostname: {router_Info[0]}")
print(f"IP: {router_Info[1]}")
print(f"Vendor: {router_Info[2]}")
print(f"OS: {router_Info[3]}")

#always remember tupples cannot be changed, they are immutable. If you want to change the value of a tuple, you need to create a new tuple with the desired values.
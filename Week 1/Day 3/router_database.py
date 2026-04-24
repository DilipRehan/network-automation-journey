routers = [
    {"hostname": "R1", "ip": "192.168.1.1", "location": "Colombo", "vendor": "Cisco"},
    {"hostname": "R2", "ip": "192.168.1.2", "location": "Kandy", "vendor": "Cisco"},
    {"hostname": "R3", "ip": "192.168.1.3", "location": "Galle", "vendor": "Juniper"},
    {"hostname": "R4", "ip": "192.168.1.4", "location": "Jaffna", "vendor": "Cisco"},
    {"hostname": "R5", "ip": "192.168.1.5", "location": "Negombo", "vendor": "Fortinet"},
]

print ("=" * 40)
label = "network devices database"
print(label.upper().center(40))
print ("=" * 40)

for router in routers: 
    print(f"\nHostname : {router['hostname']}")
    print(f"IP       : {router['ip']}")
    print(f"Location : {router['location']}")
    print(f"Vendor   : {router['vendor']}")

print ("\n" + "=" *40)
print (f"Total devices: {len(routers)}".center(40))
print ("=" * 40)
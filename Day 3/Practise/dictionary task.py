routers = [
    {"hostname": "R1", "ip": "192.168.1.1", "location": "Colombo"},
    {"hostname": "R2", "ip": "192.168.1.2", "location": "Kandy"},
    {"hostname": "R3", "ip": "192.168.1.3", "location": "Galle"},
    {"hostname": "R4", "ip": "192.168.1.4", "location": "Jaffna"},
    {"hostname": "R5", "ip": "192.168.1.5", "location": "Negombo"},
]

for router in routers: 
    print (f"{router["hostname"]} - {router["ip"]} - {router["location"]}")
    
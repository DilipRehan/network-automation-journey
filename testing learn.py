from netmiko import ConnectHandler
from datetime import datetime


router = [
    {"device_type":"cisco_ios","host":"192.168.138.130","username":"admin","password":"cisco123","secret":"cisco123"},
    {"device_type":"cisco_ios","host":"192.168.138.130","username":"admin","password":"cisco123","secret":"cisco123"},
]

try:
    connection = ConnectHandler(**router)
    connection.enable()

    for rout in router:
        output = connection.send_command("show version")
        output1 = connection.send_config_set("hostname R1")
        print(output)

except Exception as e: 
    print("Something went wrong!")
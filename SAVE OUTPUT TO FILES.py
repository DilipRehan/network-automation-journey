from netmiko import ConnectHandler
from datetime import datetime

router = [
    {"device_type":"cisco_ios", "host":"192.168.138.130", "username":"admin", "password":"cisco123"}, 
    {"device_type":"cisco_ios", "host":"192.168.138.135", "username":"admin", "password":"cisco123"}, 
    {"device_type":"cisco_ios", "host":"192.168.138.136", "username":"admin", "password":"cisco123"}
]


for ip in router:
    try:
        connection = ConnectHandler(**ip)
        print(f"Connected to the {ip['host']} sucessfully")
        line = connection.send_command("show version")
        print(line)



    except Exception as e:
        print(f"\nThere is issue connecting to the {ip['host']} : {e}")
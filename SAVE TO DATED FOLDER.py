from netmiko import ConnectHandler
from datetime import datetime
import os

routers = [
    {"device_type": "cisco_ios", "host": "192.168.138.130", "username": "admin", "password": "cisco123", "secret": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.135", "username": "admin", "password": "cisco123", "secret": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.136", "username": "admin", "password": "cisco123", "secret": "cisco123"},
]

timestamp = datetime.now().strftime("%Y-%m-%d")
folder = f"backup/{timestamp}"
os.makedirs(folder,exist_ok=True)

for router in routers:
    try: 
        connection = ConnectHandler(**router)
        connection.enable()
        output = connection.send_command("show running-config")

        filename = f"{folder}/config_{router['host']}_{timestamp}.txt"

        with open (filename, "w") as f:
            f.write(output)
        
        print(f"{router['host']} - saved to {filename}")
        connection.disconnect()
    

    except Exception as e:
        print(f"! {router['host']} - Failed: {e}")



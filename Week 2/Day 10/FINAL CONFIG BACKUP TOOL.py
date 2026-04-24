from netmiko import ConnectHandler
from datetime import datetime
import os

routers = [
    {"device_type": "cisco_ios", "host": "192.168.138.130", "username": "admin", "password": "cisco123", "secret": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.135", "username": "admin", "password": "cisco123", "secret": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.136", "username": "admin", "password": "cisco123", "secret": "cisco123"},
]

date = datetime.now().strftime("%Y-%m-%d")
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
folder = f"Day 10/ backup/{timestamp}"
os.makedirs(folder, exist_ok=True)

success =[]
failed =[]

print("=" * 45)
print("       NETWORK CONFIG BACKUP TOOL")
print("=" * 45)

for route in routers:
    try:
        connection = ConnectHandler(**route)
        connection.enable()
        output = connection.send_command("show running-config")

        file = f"{folder}/config_{route['host']}_{timestamp}.txt"
        with open(file,"w") as f:
            f.write(f"Device   : {route['host']}\n")
            f.write(f"Backup   : {timestamp}\n")
            f.write("=" * 45 +"\n")
            f.write(output)

        success.append(route['host'])
        print(f" {route['host']} - Backed up! ✅")
        connection.disconnect()

    except Exception as e:
        failed.append(route['host'])
        print(f"There is a issue with the {route['host']}: error : {e}")

print("="* 45)
print(f"Sucess : {len(success)}")
print(f"Failed : {len(failed)}")
print(f"Folder : {folder}")
print("="* 45)
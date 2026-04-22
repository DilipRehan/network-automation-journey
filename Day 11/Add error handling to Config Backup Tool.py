from netmiko import ConnectHandler
from datetime import datetime
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
import os

routers = [
    {"device_type": "cisco_ios", "host":"192.168.138.130","username":"admin","password":"cisco123","secret":"cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.135", "username": "admin", "password": "cisco123", "secret": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.136", "username": "admin", "password": "cisco123", "secret": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.1.99", "username": "admin", "password": "cisco123", "secret": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.130", "username": "admin", "password": "wrongpass", "secret": "wrongpass"},
]


timestamp =datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
folder = f"backup/{timestamp}"
os.makedirs(folder)


success = []
failed = []

print("=" * 45)
print("       NETWORK CONFIG BACKUP TOOL v2")
print("=" * 45)

for router in routers:
    try:
        connection = ConnectHandler(**router)
        connection.enable()

        config = connection.send_command("show running-config")
        filename = f"{folder}/config_{router['host']}_{timestamp}.txt"
        with open(filename,"w") as f:
            f.write(f"Device : {router['host']}\n")
            f.write(f"Backup : {timestamp}\n")
            f.write(f"="*45+"\n")
            f.write(config)

            success.append(router['host'])
            print(f"{router['host']} - Backed up")

        connection.disconnect()

    except NetmikoTimeoutException:
        failed.append(router['host'])
        print(f"! {router['host']} - Unreachable (timeout)")

    except NetmikoAuthenticationException:
        failed.append(router['host'])
        print(f"! {router['host']} - Wrong Credentials")

    except Exception as e:
        failed.append(router['host'])
        print(f"! {router['host']} - Failed: {e}")

print("=" * 45)
print(f"  Success : {len(success)}")
print(f"  Failed  : {len(failed)}")
print(f"  Folder  : {folder}")
print("=" * 45)  





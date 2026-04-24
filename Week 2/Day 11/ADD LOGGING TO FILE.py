from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException
from datetime import datetime
import os

router = [
    {"device_type": "cisco_ios", "host": "192.168.138.130", "username":"admin","password":"cisco123","secret":"cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.135", "username": "admin", "password": "cisco123", "secret": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.136", "username": "admin", "password": "cisco123", "secret": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.1.99", "username": "admin", "password": "cisco123", "secret": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.130", "username": "admin", "password": "wrongpass", "secret": "wrongpass"},
]

success = []
failed = []
print("=" * 45)
print("       NETWORK CONFIG BACKUP TOOL v2")
print("=" * 45)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"backup/{timestamp}"
os.makedirs(filename)

for ip in router:
    try:
        connection = ConnectHandler(**ip)
        connection.enable()
        output= connection.send_command("show running-config")
        
        file = f"{filename}/config_{ip['host']}_{timestamp}.txt"
        with open(file,"w") as f:
            f.write(f"Device - {ip['host']}\n")
            f.write(f"Backup - {timestamp}\n")
            f.write(f"="*45+"\n")
            f.write(output)

        success.append(ip['host'])
        print(f"{ip['host']} - Saved sucessfully! ")

        connection.disconnect()
    
    except NetmikoTimeoutException:
        failed.append({ip['host']})
        print(f"{ip['host']} - Timeout connection!")

    except NetmikoAuthenticationException:
        failed.append({ip['host']})
        print(f"{ip['host']} - Invalid User Credintials")

    except Exception as e:
        failed.append({ip['host']})
        print(f"{ip['host']} - Unknown error")
        
print("=" * 45)
print(f"  Success : {len(success)}")
print(f"  Failed  : {len(failed)}")
print(f"  Folder  : {filename}")
print("=" * 45)  

from netmiko import ConnectHandler
from datetime import datetime

routers = [
    {"device_type": "cisco_ios", "host": "192.168.138.130", "username": "admin", "password": "cisco123", "secret": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.135", "username": "admin", "password": "cisco123", "secret": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.136", "username": "admin", "password": "cisco123", "secret": "cisco123"},
]

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

for router in routers:
    try:
        connection = ConnectHandler(**router)
        connection.enable()

        config = connection.send_command("show running-config")
        
        filename = f"config_{router['host']}_{timestamp}.txt"
        with open (filename, "w") as f:
            f.write(config)
        
        print(f"{router['host']} - config saved to {filename}")
        connection.disconnect()

    except Exception as e:
        print(f" ! {router['host']} - Failed : {e}")


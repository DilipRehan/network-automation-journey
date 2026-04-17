from netmiko import ConnectHandler

routers = [
    {"device_type": "cisco_ios", "host": "192.168.138.130", "username": "admin", "password": "cisco123"}, 
    {"device_type": "cisco_ios", "host": "192.168.138.133", "username": "admin", "password": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.134", "username": "admin", "password": "cisco123"},
]

for router in routers:
    try:
        connection = ConnectHandler(**router)
        print(f"Connected ! {router['host']}")

    except Exception as e:
        print (f"Error connecting to {router['host']}: and the error is {e}")
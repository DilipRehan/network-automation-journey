from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.138.134",
    "username": "admin",
    "password": "cisco123",
}

connection = ConnectHandler(**router)
print("Connected !")

output = connection.send_command("Show ip interface brief")
print(output)

connection.disconnect()
print("Disconnected.")
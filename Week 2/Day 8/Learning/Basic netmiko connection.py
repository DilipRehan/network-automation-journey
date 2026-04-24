from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.138.130",
    "username": "admin", 
    "password": "cisco123"
}

connection = ConnectHandler(**router)
print("Connected successfully !")


output = connection.send_command("show version")
print(output)

connection.disconnect()
from netmiko import ConnectHandler
import subprocess

file = open("show_version.txt", "w")



routers = [
    {"device_type": "cisco_ios", "host": "192.168.138.130", "username": "admin", "password": "cisco123"}, 
    {"device_type": "cisco_ios", "host": "192.168.138.133", "username": "admin", "password": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.134", "username": "admin", "password": "cisco123"},
]

for router in routers:
    try:
        connection = ConnectHandler(**router)
        print(f"Connected ! {router['host']}")
              
        output = connection.send_command("show version")
        file.write("=" *40)
        file.write(f"The output for :"+ router ['host']+"\n")
        file.write(output)


        file.write("=\n" *40)
        file.close()

    except Exception as e:
        print (f"Error connecting to {router['host']}: and the error is {e}")
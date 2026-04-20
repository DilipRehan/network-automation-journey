from netmiko import ConnectHandler

router = [{"device_type":"cisco_ios", "host":"192.168.138.130", "username":"admin","password":"cisco123"},
          {"device_type":"cisco_ios", "host":"192.168.138.135", "username":"admin","password":"cisco123"},
          {"device_type":"cisco_ios", "host":"192.168.138.136", "username":"admin","password":"cisco123"}
          
          ]

for route in router:
    try:
        connection = ConnectHandler(**route)
        print(f"\n--- Connected to {route['host']} ---")
        output = connection.send_command("show ip interface brief")
        print(output)
        connection.disconnect()
        print(f"Disconnected from {route['host']}")
    
    
    except Exception as e:
        print(f"Failed to connect the {route['host']} : {e}")
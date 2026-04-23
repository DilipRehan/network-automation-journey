from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException


routers = [
    {"device_type":"cisco_ios","host":"192.168.138.130","username":"admin","password":"cisco123","secret":"cisco123"},
]

commands = ["ip route 172.16.0.0 255.255.0.0 192.168.138.1"]

success = []
failed = []

print("=" * 45)
print("     PUSHING CONFIG TO ALL DEVICES")
print("=" * 45)

for router in routers:
    try:
        connection = ConnectHandler(**router)
        connection.enable()

        #sending the configurations that we already speicifed in the above
        output = connection.send_config_set(commands)

        verify = connection.send_command("show ip route static")

        if "172.16.0.0" in verify:
            success.append(router['host'])
            print(f"{router['host']} - route pushed and verified")
        else:
            failed.append(router['host'])
            print(f"{router['host']} - route not found after push")
        connection.disconnect()

    except NetmikoTimeoutException:
        failed.append(router['host'])
        print(f" ! {router['host']} - Unreachable")
    
    except NetmikoAuthenticationException:
        failed.append(router['host'])
        print(f"{router['host']} - Wrong credentials")
    except Exception as e:
        print(f" ! {router['host']} - failed : {e}")

print("=" *45)
print(f" Success : {len(success)}")
print(f" Failed  : {len(failed)}")
print("=" * 45)


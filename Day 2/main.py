device = input("Enter deivce name: ")
ip = input("Enter IP Address ")
ports = input("Enter ports: ")

ports = int(ports)


if ports>=24:
    size = "Large"
elif ports>=8: 
    size = "Medium"
else:
    size = "Small"

print(f"\n---Device Summary---")
print(f"Device: {device}")
print(f"IP: {ip}")
print(f"Ports: {ports}")
print(f"Size: {size} device")
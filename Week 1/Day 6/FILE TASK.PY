file = open("devices.text", "w")
file.write("Router - 192.168.1.1\n")
file.write("Switch - 192.168.1.2\n")
file.write("Firewall - 192.168.1.3\n")
file.close()

print("File create sucessfully")
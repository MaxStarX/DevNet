devices = []

file = open ("D:\\!Python\\devices.txt", "r")
for item in file :
    item = item.strip()
    devices.append(item)
    
    
file.close()
print(devices)

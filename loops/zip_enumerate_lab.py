#1

names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(index, name)
    
#2

servers = ["app_01", "app_02", "app_02"]
for index, server in enumerate(servers, start=1):
    print(f"server {index}: {server}")
    
#3

errors = ["disk full", "timeout", "connection lost"]
for index, error in enumerate(errors):
    if index % 2 == 0:
        print(f"Error at index {index}: {error}")
        
#4

ports = [22, 80, 443, 8080]
for index, port in enumerate(ports):
    if index > 1:
        print(f"port {index}: {port}")
        
#5

users = ["Admin", "dev", "ops"]
for index, name in enumerate(users, start = 1):
    print(f"User {index}: {name}")
    
#6

files = ["log1.txt", "log2.txt", "log3.txt"]
last = len(files) - 1
for index, file in enumerate(files):
    if index == last:
        print(f"The last file is: {file}")
        
#7

regions = ["us-east-1", "eu-west-1", "ap-south-1"]
for index, region in enumerate(regions):
    if index > 0:
        print(f"Region {index}: {region}")
# #1

# names = ["Alice", "Bob", "Charlie"]
# for index, name in enumerate(names):
#     print(index, name)
    
# #2

# servers = ["app_01", "app_02", "app_02"]
# for index, server in enumerate(servers, start=1):
#     print(f"server {index}: {server}")
    
# #3

# errors = ["disk full", "timeout", "connection lost"]
# for index, error in enumerate(errors):
#     if index % 2 == 0:
#         print(f"Error at index {index}: {error}")
        
# #4

# ports = [22, 80, 443, 8080]
# for index, port in enumerate(ports):
#     if index > 1:
#         print(f"port {index}: {port}")
        
# #5

# users = ["Admin", "dev", "ops"]
# for index, name in enumerate(users, start = 1):
#     print(f"User {index}: {name}")
    
# #6

# files = ["log1.txt", "log2.txt", "log3.txt"]
# last = len(files) - 1
# for index, file in enumerate(files):
#     if index == last:
#         print(f"The last file is: {file}")
        
# #7

# regions = ["us-east-1", "eu-west-1", "ap-south-1"]
# for index, region in enumerate(regions):
#     if index > 0:
#         print(f"Region {index}: {region}")
        
# #8

# services = ["nginx", "redis", "postgres"]
# for index, service in enumerate(services, start = 1):
#     print(f"Service {index}: {service}")
    
# #9

# tasks = ["backup", "cleanup", "monitoring"]
# for index, task in enumerate(tasks):
#     if index % 2 == 0:
#         print(f"Task {index}: {task}")
        
# #10

# containers = ["c1", "c2", "c3", "c4"]
# for index, container in enumerate(containers):
#     print(f"Container {index}: {container}")
#     if index == 2:
#         break
    
#11

# hosts = ["host1", 
#          "host2", 
#          "host3"
# ]
# ips = ["10.0.0.1", 
#        "10.0.0.2", 
#        "10.0.0.3"
# ]
# for host, ip in zip(hosts, ips):
#     print(f"Host name: {host} | IP: {ip}")
    
# #12

# users = ["alice", "bob", "charlie"]
# ids = [101, 102, 103]
# for user, id in zip(users, ids):
#     print(f"User {user} has ID {id}")
    
# #13

# services = ["nginx", "redis", "postgres"]
# ports = [80, 6379, 5432]
# for service, port in zip(services, ports):
#     print(f"{service} - port {port}")
    
# #14

# regions = ["us-east-1", "eu-west-1"]
# zones = ["a", "b"]
# for reg, zone in zip(regions, zones):
#     print(f"Region: {reg} | Zone: {zone}")
    
# #15

# containers = ["c1", "c2", "c3"]
# statuses = ["running", "stopped", "paused"]
# for cont, stat in zip(containers, statuses):
#     if stat == "running":
#         print(f"{cont} is {stat}")
        
# #16

# files = ["file1", "file2"]
# sizes = [100, 200]
# types = ["txt", "log"]
# for file, size, type in zip(files, sizes, types):
#     print(f"{file}.{type} {size} k")
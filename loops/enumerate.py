#enumerate

servers = ["web-01", "web-02", "web-03"]
for index, server in enumerate(servers):
    # print(type(server))
    # print(server)
    print(f"{index} Proccesing server {server}")
host_port = ("127.0.0.1", 3000)
print(host_port)
print(type(host_port))
print(host_port[0])
print(host_port[1])

red_rgb = (255, 0, 0)
print(red_rgb[0])
single_value = ("text",)

print(host_port[-2:])

service_endpoint = ("auth.server.dev.local", 80)
service_endpoint[1] = 433 #Unable to because its a tuple
print(f"The host is {service_endpoint[0]} and the port is {service_endpoint[1]}")


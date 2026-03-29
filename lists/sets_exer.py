ports_list = [8080, 8443, 22, 8080, 443]
unique_ports = set(ports_list)
print(unique_ports)
is_present = 22 in unique_ports
print(is_present)

unique_ports.add(3000)
print(unique_ports)

unique_ports.discard(22)
print(unique_ports)

server_names = {"web01", "web02", "web03"}
tof = 22 in server_names
print(tof)

valid_set = {(1, 2), (3, 4)}

list = [54, 42, 54 ,22 , 1115, 42]
new_list = set(list)
print(new_list)
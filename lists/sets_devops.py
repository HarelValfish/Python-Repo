req_packages = (["python3", "pip", "requests", "boto3", "pip"])
print(req_packages)

x = "requests" in req_packages
y = "ansible" in req_packages

print(f"is 'requests' required? {x}")
print(f"is 'ansible' required? {y}")

req_packages.append("paramiko")
req_packages.remove("pip")
print(req_packages)
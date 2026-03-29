deployment_target = ["east-1", "west-1", "southeast-1"]
print(deployment_target)

print(deployment_target[0])
print(deployment_target[1])

deployment_target.append("west-2")
print(deployment_target)

deployment_target.append("east-2")
print(deployment_target)

deployment_target[1] = "central-1"
print(deployment_target)

print(len(deployment_target))
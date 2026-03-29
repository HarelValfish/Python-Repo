# Comparing lists

friends = ["Bob", "Rolf", "Anna"]
abroad = ["Bob", "Anna", "Rolf"]
print(friends == abroad) #False index is checked as well as the strings themselves.
print(set(friends) == set(abroad)) #True because set has no indexes.
# "==" or "is"
print(friends[1] is abroad[2]) #True because the 2 words compared are the same string.
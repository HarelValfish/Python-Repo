set_of_tuple = {(1, 2), (3, 4)}
is_exist = (1, 2) in set_of_tuple
is_exist2 = (3, 4) in set_of_tuple
print(is_exist)
print(is_exist2)

devs = {"Alice", "Bob", "Charlie"}
admin = {"Alice", "David"}

x = "Alice" in devs & admin
print(x)

devs.union(admin)

devs | admin
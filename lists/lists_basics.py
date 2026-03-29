number_int = 6 #integar
number_float = 6.0 #Float
string = "Baba" #String
boolers = False #Boolean (0)
boolers = True #Boolean (1)

#List
book1 = "Harry Plonter - and the labs of despair"
book2 = "Harry Plonter - and the chamber of secrets"
book3 = "Harry Plonter - and the prisoner of askaban"

harry_books = [
    "harry potter - and the labs of despair", #idx 0
    "harry potter - and the chamber of secrets", #idx 1
    "harry potter - and the prisoner of askaban", #idx 2
    "harry potter - and the goblet of fire", #idx 3
    "harry potter - and the order of the phoenix", #idx 4
    "harry potter - and the half blood prince", #idx 5
    "harry potter - and the deathly hallows" #idx 6
]

# print(harry_books)

# print(harry_books[3])
multi_data_list = [
    "Baba",
    1.2,
    54,
    True,
    ["Harel, Shahar, Yossi"]
]

# print(type(multi_data_list[0])) #String
# print(type(multi_data_list[1])) #Float
# print(type(multi_data_list[2])) #Int
# print(type(multi_data_list[3])) #Boolean
# print(type(multi_data_list[4])) #List

# List
my_list = ["Bob", "Rolf", "Anne"] # [] List is mutable (can be changed)
# print(my_list)

# Tuple
my_tuple = ("Bob", "Rolf", "Anne") # () Tuple is immutable (cannot be changed)  
# print(my_tuple)

# Set
my_set = {"Bob", "Rolf", "Anne"} # {} Set is unordered, unindexed, and does not allow duplicate values. It is mutable (can be changed) but does not support indexing or slicing.
# print(my_set)

my_list = ["Bob", "Rolf", "Anne"]
my_list[0] = smith = "Smith" # List is mutable, we can change the value at index 0
# print(my_list) change Bob to Smith

my_servers = [
    "us-east-1",
    "us-west-1",
    "eu-west-1",
    "il-west-1"
]

# my_tuple = ("bob", "blob")
# my_tuple[0] = "Smith" #ERROR because tuple is immutable

#adding to the list
my_list.append("john")

#tuple cant have anything added because tuple is immutable

#Trying to edit a list inside a tuple\
my_tuple = ("Bob",
            "john",
            "Anna",
            ["black", "white", "red"]
)
print(my_tuple)

my_tuple[3].append("Doe")
print (my_tuple) # can append inside a list thats inside a tuple
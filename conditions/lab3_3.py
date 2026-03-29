# movieset = {"The Matrix", "Terminator", "Fallout"}
# user_movie = input("Enter a move you have watched recently: ")

# if user_movie in movieset:
#     print("Movie is already in the database.")
# else:
#     print("Movie added to the databse")
#     movieset.add(user_movie)
#     print(movieset)

#================================================================

secnum = 7
user_input = input("Enter 'Y' if you would like to play: ")
if user_input == "Y":
    ans = int(input("Guess what number im thinking of: "))
    if ans == secnum:
        print("Correct!")
    else:
        print("Womp Womp")
else:
    print("Okay, Nevermind then :)")
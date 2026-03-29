friends = {"Bob", "Jen", "Rolf"}
print("Jen" in friends)
print("Anna" in friends)

movies = {"BTTF", "Ghosts", "Passangers"}
user_movie = input("Enter a movie you have watched recently: ")
print(user_movie in movies)
print("Pass" in "Passangers")

if user_movie in movies:
    print("Movie is already registered to the list.")
else:
    print("Movie added to the list")
    movies.add(user_movie)

print(movies)
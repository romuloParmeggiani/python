favMovies = ["Bram Stoker's Dracula", "The Shinning", "Blade Runner", "Coraline", "Dune"]
# favMoviesBckup = favMovies would not make a backup of the variable's values, only points out to original object
# Therefore would being affected to change on it and vice versa also!
favMoviesBackup = []
for movie in favMovies:
    favMoviesBackup.append(movie)
print(favMovies, "\n", favMoviesBackup)
# print(favMovies)
#favMovies.append("Predator")
# print(favMovies)
#favMovies.insert(0,"The Last Samurai")
# print(favMovies)
#del(favMovies[4])
#print(favMovies)

#Changes during the execution of the For loop affects the length of favMovies on realtime and makes the execution to break earlier
# for i in favMovies:
#     print(f"{i} Removing {favMovies[0]}...")
#     del(favMovies[0])
# print(favMovies)
#Setting the offSet before initiating the deletion makes sure to iterate through every single item
offSet = len(favMovies)
for i in range(offSet):
    print(f"{i} Removing the movie {favMovies[0]}...")
    del(favMovies[0])
print(favMovies)
for movie in favMoviesBackup:
    favMovies.append(movie)
while len(favMovies) != 0:
    print(f"Removing the movie {favMovies[0]}...")
    del(favMovies[0])
print(favMoviesBackup)
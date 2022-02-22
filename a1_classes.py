"""
CP1404 Assignment
Movie class.
"""
# TODO: Copy your first assignment to this file, then update it to use Movie class
# Optionally, you may also use MovieCollection class

from movie import Movie
from moviecollection import MovieCollection
from operator import itemgetter

FILE = "movies.csv"

MENU = """
Menu:
L - List movies
A - Add new movie
W - Watch a movie
Q - Quit
"""


def main():
    """Program to track movies that a user wish to watch and movies they have already watched"""
    movies = MovieCollection()
    movies.load_movies(FILE)
    movies.sort("year")
    print("Movies To Watch 1.0 - by <Tuan Dat Tran>")
    print(f"{len(movies.movies)} movies loaded")
    print(MENU, end='')
    choose = input(">>> ").lower()
    classify_option(choose, movies)
    movies.save_movies(FILE)


def classify_option(choose, movies):
    """Classify the user's option"""
    while choose != "q":
        if choose == 'l':
            get_list(movies)
        elif choose == 'a':
            add_movie(movies)
        elif choose == 'w':
            # Check whether all movies are watched
            w_count = 0
            for movie in movies.movies:
                if movie.is_watched:
                    w_count += 1
            if w_count == len(movies.movies):
                print("No more movies to watch!")
            else:
                watch_movie(movies)
        else:
            print("Invalid menu choice")
        print(MENU, end='')
        choose = input(">>> ").lower()


def watch_movie(movies):
    """Ask the user for the movie would like to watch and confirm it when the user choose 'w'"""
    print("Enter the number of a movie to mark as watched")
    valid_input = False
    movie_number = None
    while not valid_input:
        try:
            movie_number = int(input(">>> "))
            # Check input range
            while movie_number < 0:
                print("Number must be >= 0")
                movie_number = int(input(">>> "))
            while movie_number > len(movies.movies) - 1:
                print("Invalid movie number")
                movie_number = int(input(">>> "))
            valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    movie = movies.movies[movie_number]
    if not movie.is_watched:
        print(f"{movie.title} from {movie.year} watched")
        movie.is_watched = True
    else:
        print(f"You have already watched {movie.title}")


def get_list(movies):
    """Return the list of movies when the user choose 'l'"""
    watched = 0
    unwatch = 0
    for index, detail in enumerate(movies.movies):
        if not detail.is_watched:
            print(f"{index:>2}. * {detail.title:35} - {detail.year:4} ({detail.category})")
            unwatch += 1
        else:
            print(f"{index:>2}.   {detail.title:35} - {detail.year:4} ({detail.category})")
            watched += 1
    print(f"{watched} movies watched, {unwatch} movies still to watch")


def add_movie(movies):
    """Add new movie to the movie list when the user choose 'a'"""
    title = input("Title: ")
    valid_input = False
    year = None
    while title == '':
        print("Input can not be blank")
        title = input("Title: ")
    while not valid_input:
        try:
            year = int(input("Year: "))
            while year < 0:
                print("Number must be >= 0")
                year = int(input("Year: "))
            valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    category = input("Category: ")
    while category == "":
        print("Input can not be blank")
        category = input("Category: ")
    print(f"{title} ({category} from {year}) added to movie list")
    movies.add_movie(Movie(title, year, category, False))
    movies.sort("year")


if __name__ == '__main__':
    main()

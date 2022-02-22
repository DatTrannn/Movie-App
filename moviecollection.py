"""
CP1404 Assignment
MovieCollection class.
"""

# TODO: Create your MovieCollection class in this file
import csv
from operator import attrgetter
from movie import Movie


class MovieCollection:
    """Represent the information about a movie collection"""
    movies = []

    def add_movie(self, movie):
        """Add a single Movie object to the movies attribute"""
        self.movies.append(movie)

    def get_unwatched_count(self):
        """Get number of unwatched movies"""
        count = 0
        for movie in self.movies:
            if movie.is_watched:
                count += 1
        return count

    def get_watched_count(self):
        """Get number of watched movies"""
        count = 0
        for movie in self.movies:
            if not movie.is_watched:
                count += 1
        return count

    def load_movies(self, filename):
        """Load movies from csv file into Movie objects in the list"""
        with open(filename, 'r') as in_file:
            reader = csv.reader(in_file)
            for line in reader:
                year = int(line[1])
                is_watched = None
                if line[3] == 'w':
                    is_watched = True
                elif line[3] == 'u':
                    is_watched = False
                self.movies.append(Movie(line[0], year, line[2], is_watched))

    def save_movies(self, filename):
        """Save movies from movie list into csv file"""
        with open(filename, 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for movie in self.movies:
                writer.writerow([movie.title, movie.year, movie.category, 'u' if movie.is_watched else 'w'])

    def sort(self, key):
        """Sort by the key passed in, then by title"""
        self.movies.sort(key=attrgetter(key, 'title'))

    def __str__(self):
        return f"{[movie.__str__() for movie in self.movies]}"

"""
CP1404 Assignment
Movie class.
"""


# TODO: Create your Movie class in this file


class Movie:
    """Represent the information about a movie"""
    def __init__(self, title='', year=0, category='', is_watched=False):
        """
            Initialise a movie instance.
                title: string, title of a movie
                year: int, production year of a movie
                category: string, movie category includes Action, Comedy, Documentary, Drama, Fantasy, Thriller
                is_watched: boolean, movie that has been watch or unwatched
        """
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """Print details of the movie"""
        return f"{self.title} ({self.category} from {self.year})" + (" watched" if self.is_watched else "")

    def watch_movie(self):
        """Mark the movie is watched"""
        self.is_watched = True

    def unwatch_movie(self):
        """Mark the movie is unwatched"""
        self.is_watched = False

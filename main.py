"""
Name: Tuan Dat Tran
Date: 11/01/2022
Brief Project Description: MoviesToWatchApp is a Kivy App used for displaying the list of movies to watch in different orders
and mark that the movie has been watched or unwatched as well as add more movie to the list
GitHub URL: https://github.com/JCUS-CP1404/assignment-2---movies-to-watch-kivy-DatTrannn
"""
# TODO: Create your main program in this file, using the MoviesToWatchApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from moviecollection import MovieCollection
from movie import Movie

FILE = "movies.csv"
WATCHED_BGCOLOR = [1, 1, 0, 1]
UNWATCHED_BGCOLOR = [0, 1, 1, 1]
CATEGORY_LIST = ['action', 'comedy', 'documentary', 'drama', 'fantasy', 'thriller']


class MoviesToWatchApp(App):
    """ MoviesToWatchApp is a Kivy App for displaying the list of movies to watch"""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.movies = MovieCollection()
        self.movies.load_movies(FILE)
        self.sort_list = ["Title", "Year", "Category", "Watched"]
        self.current_sort = "Title"
        self.movies.sort("title")

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Movies to Watch"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        self.on_stop()
        return self.root

    def change_sort(self, value):
        """handle change of sort selection, output result to label widget """
        if value == "Watched":
            self.movies.sort("is_watched")
        else:
            self.movies.sort(value.lower())
        self.current_sort = value
        self.update_widgets()

    def create_widgets(self):
        """Create buttons from movies and add them to the GUI."""
        for movie in self.movies.movies:
            if movie.is_watched:
                temp_button = Button(text=movie.__str__(), background_color=WATCHED_BGCOLOR)
            else:
                temp_button = Button(text=movie.__str__(), background_color=UNWATCHED_BGCOLOR)
            temp_button.bind(on_release=self.press_entry)
            temp_button.movie = movie
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handle pressing entry buttons.
        param instance: the Kivy button instance that was clicked
        """
        movie = instance.movie
        if movie.is_watched:
            self.root.ids.output_text.text = "You need to watch " + movie.title
            movie.is_watched = False
            instance.background_color = UNWATCHED_BGCOLOR
        else:
            self.root.ids.output_text.text = "You have watched " + movie.title
            movie.is_watched = True
            instance.background_color = WATCHED_BGCOLOR
        instance.text = movie.__str__()
        self.root.ids.movie_status.text = f"To watch: {self.movies.get_watched_count()}. Watched: {self.movies.get_unwatched_count()}"

    def update_widgets(self):
        """Update buttons' order from sort type"""
        self.root.ids.entries_box.clear_widgets()
        self.create_widgets()

    def add_movie(self):
        """Handle pressing "Add Movie" button"""
        title = self.root.ids.input_title.text
        year = self.root.ids.input_year.text
        category = self.root.ids.input_category.text
        try:
            if title == '' or category == '' or year == '':
                self.root.ids.output_text.text = "All fields must be completed"
            elif category.lower() not in CATEGORY_LIST:
                self.root.ids.output_text.text = "Category must be one of Action, Comedy, Documentary, Drama, Fantasy, Thriller"
            elif int(year) < 0:
                self.root.ids.output_text.text = "Year must be >= 0"
            else:
                movie = Movie(title, int(year), category, False)
                self.movies.add_movie(movie)
                temp_button = Button(text=movie.__str__(), background_color=UNWATCHED_BGCOLOR)
                temp_button.bind(on_release=self.press_entry)
                temp_button.movie = movie
                # add the button to the "entries_box" layout widget
                self.root.ids.entries_box.add_widget(temp_button)
                self.clear()
        except ValueError:
            self.root.ids.output_text.text = "Please enter a valid number"

    def clear(self):
        """Handle pressing Clear button"""
        self.root.ids.input_title.text = self.root.ids.input_year.text = self.root.ids.input_category.text = self.root.ids.output_text.text = ''

    def on_stop(self):
        """Save the file when user quited the app"""
        self.movies.save_movies(FILE)


if __name__ == '__main__':
    MoviesToWatchApp().run()

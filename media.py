""" Module to display movie object, attributes and instances """
import webbrowser


class Movie(object):
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        Intialize instance of class Movie

        Args:
            movie_title (str): Title of the Movie.
            movie_storyline (str): Short description about the movie.
            poster_image (str): Movie Poster Image URL.
            trailer_youtube (str): Movie trailer URL.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Returns:
            webbrowser To play the trailer with your default browser
        """
        webbrowser.open(self.trailer_youtube_url)

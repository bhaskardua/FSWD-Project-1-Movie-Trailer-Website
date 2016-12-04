import webbrowser


class Movie:
    """Class encapsulating the properties of a Movie.

    Attributes:
        movie_title (str): Name of the movie.
        movie_storyline (str): One line description of the movie's plot.
        poster_image (str): Link to an image file of the movie's poster.
        trailer_youtube (str): Link to the movie's trailer on youtube.
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

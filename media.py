import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, released_year,
                 rating, poster_image, trailer_youtube):
        """Constructor of class Movie, parameters needed:

        movie title,
        movie storyline,
        released year,
        rating like G, PG, Pg-13 etc,
        poster image url,
        youtube trailer url
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.released_year = released_year
        self.rating = rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This method is to show the trailer on webbrowser"""
        webbrowser.open(self.trailer_youtube_url)

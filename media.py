import webbrowser

class Movie():
    """
        The Movie class hold the information related to the movies to be displayed
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                    trailer_youtube):
        """
            Initialize the instance property
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
            Open the trailer URL
        """
        webbrowser.open(self.trailer_youtube_url)

#!/usr/local/bin/python
# coding: latin-1

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
    """A cowboy doll is profoundly threatened and jealous when a
    new spaceman figure supplants him as top toy in a boy's room.""",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "http://www.youtube.com/watch?v=4KPTXpQehio")
avatar = media.Movie("Avatar",
    """A paraplegic marine dispatched to the moon Pandora on a unique mission
    becomes torn between following his orders and protecting the world he
    feels is his home. """,
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "http://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
    """After being kicked out of a rock band, Dewey Finn becomes a substitute
    teacher of a strict elementary private school, only to try and turn it
    into a rock band. """,
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "http://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
    """A rat who can cook makes an unusual alliance with a young kitchen
        worker at a famous restaurant. """,
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "http://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnigh in Paris",
    """While on a trip to Paris with his fianc?e's family, a nostalgic
        screenwriter finds himself mysteriously going back to the 1920s
        everyday at midnight. """,
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
    "http://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
    """Katniss Everdeen voluntarily takes her younger sister's place in the
        Hunger Games, a televised competition in which two teenagers from
        each of the twelve Districts of Panem are chosen at random to fight
        to the death.""",
    "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
    "http://www.youtube.com/watch?v=mfmrPu43DF8")


fresh_tomatoes.open_movies_page([toy_story, avatar, school_of_rock, ratatouille,
                                 midnight_in_paris, hunger_games])

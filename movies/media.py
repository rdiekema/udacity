# coding=utf-8

__author__ = 'rdiekema'


class Movie:
    """
    Class for working with movie data.

    :param poster_image_url:
    :param title:
    :param trailer_youtube_url:
    :param year:
    :param rating:
    """

    def __init__(self, poster_image_url, title, trailer_youtube_url, year,
                 rating):
        self.poster_image_url = poster_image_url
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.year = year
        self.rating = rating

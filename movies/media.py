__author__ = 'rdiekema'

import json as j


class Movie:
    def __init__(self, poster_image_url, title, trailer_youtube_url, year, rating):
        self.poster_image_url = poster_image_url
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.year = year
        self.rating = rating
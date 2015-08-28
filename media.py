__author__ = 'rdiekema'

import json as j


class Movie:
    def __init__(self, poster_image_url, title, trailer_youtube_url, json):
        self.poster_image_url = poster_image_url
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb = j.loads(json)


    def getYearReleased(self):
        return self.imdb['Released'][-4:]

    def getRating(self):
        return self.imdb['Rated']


from movies import fresh_tomatoes as ft, media

__author__ = 'rdiekema'


def main():
    movies = list()
    movies.append(media.Movie("https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                              "Jurassic Park", "https://www.youtube.com/watch?v=QWBKEmWWL38", "1993", "PG-13"))
    movies.append(media.Movie("https://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg", "Office Space",
                              "https://www.youtube.com/watch?v=3_fG_zLbBeU", "1999", "R"))
    movies.append(media.Movie("https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "Toy Story",
                              "https://www.youtube.com/watch?v=KYz2wyBy3kc", "1995", "G"))
    movies.append(media.Movie("https://upload.wikimedia.org/wikipedia/en/7/7b/Blazing_saddles_movie_poster.jpg",
                              "Blazing Saddles", "https://www.youtube.com/watch?v=VKayG1TrfuE", "1974", "R"))
    movies.append(media.Movie("https://upload.wikimedia.org/wikipedia/en/4/45/Spaceballs.jpg", "Spaceballs",
                              "https://www.youtube.com/watch?v=uWVSVgU-I0s", "1987", "PG"))
    movies.append(media.Movie("https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", "The Matrix",
                              "https://www.youtube.com/watch?v=vKQi3bBA1y8", "1999", "R"))
    ft.open_movies_page(movies)


if __name__ == '__main__': main()
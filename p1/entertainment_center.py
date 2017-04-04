import media

from fresh_tomatoes import open_movies_page

id_list = [249898, 247658, 1156890, 342858, 247875, 344258]


def fetch_movie_list(idList):
    '''return a movie list through the user defined id'''
    movieList = []

    for id in idList:
        movie = media.Movie(id)
        movieList.append(movie)

    return movieList

if __name__ == '__main__':
    movie_list = fetch_movie_list(id_list)
    open_movies_page(movie_list)

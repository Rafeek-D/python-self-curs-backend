from Show_movies_web import *


list_of_movie=[{'Title': 'Avatar', 'Year': '2009', 'Poster': 'gX300.jpg'},
               {'Title': 'Titanic', 'Year': '1997', 'Poster': '_SX300.jpg'},
               {'Title': 'Titanic', 'Year': '1997', 'Poster': '_SX300.jpg'}]


#print(dict(list_of_movie[0].items()))

#print(list_of_movie[1].get('Title'))

#print(make_moviecard(list_of_movie))

#movie_name = input("put the name of the movie: ")
#det= create_movie(get_movie_short_info(movie_name, plus_key_globale))

#print(list_of_movie)
i = 1
while i < len(list_of_movie):
    list_of_movie.insert(i, 'x')
    i += i+1

print(list_of_movie)
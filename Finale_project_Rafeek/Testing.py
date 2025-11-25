from Finale_project_Rafeek import *
from FP_for_api import *
#from FP_for_DB import *
from DB_Class import *
from DB_Class import MoviesCollection

def test_api_title():
    movie_title="avatar"
    movie= get_movie_infos(movie_title, plus_key_globale)
    assert movie.get("Title") == "Avatar"

#movie_title="titanic"
#print(get_movie_infos(movie_title,plus_key_globale).get("Title"))

def test_DB():
    movie_title = "avatar"
    movie = get_movie_infos(movie_title, plus_key_globale)
    new_movie = MoviesCollection(title=movie.get("Title"), year=movie.get("Year"), poster=movie.get("Poster"))
    new_movie.save()
    name= new_movie.title
    assert name == "Avatar"

    # data = MoviesCollection.objects[0].to_mongo().to_dict().get("title")
    # assert data == "Avatar"


from FP_for_api import *

from bson import ObjectId
from pymongo import MongoClient
from mongoengine import connect, disconnect, Document
from mongoengine import StringField, IntField, ListField
from Show_movies_web import *
from FP_for_api import *


#'''
from os import remove


###-------------------------
## DB Movies: K00P
# Define a database name "movies_DB".
database = "moviesDB"

##-----------------------------------------------
# if the db=name. and the name of DB not exist than you will not get a error and if you create a collection than it will create a DB with this collection!!
connect(host="mongodb+srv://rafeekslack_db_user:......ldwJTBVs2h6i@clus0.jnqagzn.mongodb.net/?retryWrites=true&w=majority&appName=Clus0", db=database)
##-----------------------------------------------


#'''
##-----------------------------------------------
# Student here represent a collection in the database
class MoviesCollection(Document):
    title = StringField(max_length=64, required=True)
    year = IntField()
    poster = StringField()

    def get_info(self):
        return f"the name:{self.title}, the year:{self.year}, the poster:{self.poster}"
        #return f"the name:{self.name}, the location:{self.location}, the courses:{self.courses[0]}, the age:{self.age} "
#'''

class DB_Class_fun:

## save the Movies list into DB/Collection
    def put_movie_into_DB (list_movies):
        #i=len(list_movies)
        i=0
        for movie in list_movies:
            new_movie = MoviesCollection(title=movie.get("title"), year=movie.get("year"), poster=movie.get("poster"))
            new_movie.save()
            i=i+1
            print(f"your_movies_collection have been {i} Movies saved successfully")

## pu one movie to DB
    def put_one_movie_into_DB(movie_name):
        new_movie = MoviesCollection(title=movie_name.get("title"), year=movie_name.get("year"), poster=movie_name.get("poster"))
        new_movie.save()
        print(f"one movie has seved into your_movies_collection successfully")


    # all the movie with this name
    def delete_movie_from_DB (name):
        for movie in MoviesCollection.objects(title=name):
            movie.delete()

    #one movie with the name
    def delete_one_movie_from_DB(name_movie):
        x= "there are no movie with this name"
        for movie in MoviesCollection.objects:
            if movie.title == name_movie:
                movie.delete()
                x= "the movie has removed successfully"
                break
                #return f'the movie has removed successfully'
                #return x
        print(x)

    #delete all the movies from DB
    def delete_all_movies_from_DB():
        MoviesCollection.objects.delete()

    def get_movie_from_DB (name: str):
        x= f'the are no movie with this name: {name}'
        for movie in MoviesCollection.objects:
            if movie.title == name:
                #return movie.get_info()
                x= movie.get_info()
                break
        return x

    def get_all_movies_from_DB():
        x=[]
        for movie in MoviesCollection.objects:
            data = movie.to_mongo().to_dict()
            data.pop("_id", None)
            x.append(data)
        return x
    ## the same whit get_all_movies_from_DB but another style
    def get_all_movies_from_DB2():
        n_mov=[]
        for movie in MoviesCollection.objects:
            data = movie.to_mongo().to_dict()
            data.pop("_id", None)
            n_mov.append(data)
        return n_mov


''' 
    def do_list_to_dic_mov(list_of_dic):
        new_dic={}
        for dic in list_of_dic:
            new_dic["Title"] = dic.get("Title")
            new_dic["Year"] = dic.get("Year")
            new_dic["Poster"] = dic.get("Poster")
        return new_dic
'''


################# testing######

#'''
if __name__ == "__main__":
    # mov1= MoviesCollection(    title="rr", year="11", poster="tttt")
    # mov1.save()
    #print(DB_Class_fun.get_movie_from_DB("Avatar"))
    #print(MoviesCollection.objects.count())
    #print(get_all_movies_from_DB2())
    #delete_movie_from_DB("rr")
     #for user in MoviesCollection.objects:
     #   print(user.title)

    print("the length of the List of Movies is: ",len(DB_Class_fun.get_all_movies_from_DB()))
    #print(DB_Class_fun.get_all_movies_from_DB())
    #print("the typ of get_all_movies_from_DB ist: ", type(DB_Class_fun.get_all_movies_from_DB()))

    #print(DB_Class_fun.delete_one_movie_from_DB("tt"))
    #DB_Class_fun.delete_one_movie_from_DB("Titanic")
    print(len(DB_Class_fun.get_all_movies_from_DB()))

    #DB_Class_fun.delete_movie_from_DB("Avatar")
    #print("the length of the List of Movies is: ", len(DB_Class_fun.get_all_movies_from_DB()))

    #print (do_list_to_dic_mov(get_all_movies_from_DB())

    #print(get_all_movies_from_DB2())

    #print(make_moviecard(get_all_movies_from_DB()))

    #for movie in Movies_Collection.objects:
    #   print(type(movie.to_mongo().to_dict()))


    #print(DB_Class_fun.get_movie_from_DB("gg"))
    #print(DB_Class_fun.get_movie_from_DB("Avatar"))

#    for user in MoviesCollection.objects:
#        data= user.to_mongo().to_dict()
#        print(data)
#        print(data.get("title"))

#   print(MoviesCollection.objects)

#   print("first")
#   print(MoviesCollection.objects[2].to_mongo().to_dict().get("title"))

#'''
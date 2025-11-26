

from FP_for_api import *

from bson import ObjectId
from pymongo import MongoClient
from mongoengine import connect, disconnect, Document
from mongoengine import StringField, IntField, ListField
from Show_movies_web import *
from FP_for_api import *

##'''
from os import remove


''' 

###-------------------------
## DB Movies: K00P
# Define a database name "movies_DB".
database = "moviesDB"

##-----------------------------------------------
# if the db=name. and the name of DB not exist than you will not get a error and if you create a collection than it will create a DB with this collection!!
connect(host="mongodb+srv://rafeekslack_db_user:.......ldwJTBVs2h6i@clus0.jnqagzn.mongodb.net/?retryWrites=true&w=majority&appName=Clus0", db=database)
##-----------------------------------------------


##-----------------------------------------------
# Student here represent a collection in the database
class MoviesCollection(Document):
    title = StringField(max_length=64, required=True)
    year = IntField()
    poster = StringField()

    def get_info(self):
        return f"the name:{self.title}, the year:{self.year}, the poster:{self.poster}"
        #return f"the name:{self.name}, the location:{self.location}, the courses:{self.courses[0]}, the age:{self.age} "

## save the Movies list into DB/Collection
def put_movie_into_DB (list_movies):
    #i=len(list_movies)
    i=0
    for movie in list_movies:
        new_movie = MoviesCollection(title=movie.get("Title"), year=movie.get("Year"), poster=movie.get("Poster"))
        new_movie.save()
        i=i+1
    print(f"your_movies_collection have been {i} Movies saved successfully")

def delete_movie_from_DB (name):
    for movie in MoviesCollection.objects(title=name):
        movie.delete()

def get_movie_from_DB (name: str):
    for movie in MoviesCollection.objects:
        if movie.title == name:
            return movie.get_info()

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


################# testing######

###'''

'''
#if __name__ == "__main__":
    # mov1= MoviesCollection(    title="rr", year="11", poster="tttt")
    # mov1.save()
    # print(get_movie_from_DB("Avatar"))
    #print(get_all_movies_from_DB())
    #print(MoviesCollection.objects.count())
    #print(get_all_movies_from_DB2())
    #delete_movie_from_DB("rr")
     #for user in MoviesCollection.objects:
     #   print(user.title)


    #print(get_all_movies_from_DB2())

    #print(make_moviecard(get_all_movies_from_DB()))

    #for movie in Movies_Collection.objects:
    #    print(type(movie.to_mongo().to_dict()))


#print(get_movie_from_DB("Titanic"))

#    for user in MoviesCollection.objects:
#        data= user.to_mongo().to_dict()
#        print(data)
#        print(data.get("title"))

#print(MoviesCollection.objects)

#print("first")
#print(MoviesCollection.objects[2].to_mongo().to_dict().get("title"))

#'''


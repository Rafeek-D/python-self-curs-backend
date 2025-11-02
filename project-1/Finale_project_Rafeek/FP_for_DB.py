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
database = "movies_DB"

##-----------------------------------------------
# if the db=name. and the name of DB not exist than you will not get a error and if you create a collection than it will create a DB with this collection!!
connect(host="mongodb+srv://rafeekslack_db_user:....ldwJTBVs2h6i@clus0.jnqagzn.mongodb.net/?retryWrites=true&w=majority&appName=Clus0", db=database)
##-----------------------------------------------


##-----------------------------------------------
# Student here represent a collection in the database
class Movies_Collection(Document):
    title = StringField(max_length=64, required=True)
    year = IntField()
    poster = StringField()

    def get_info(self):
        return f"the name:{self.title}, the year:{self.year}, the poster:{self.poster}"
        #return f"the name:{self.name}, the location:{self.location}, the courses:{self.courses[0]}, the age:{self.age} "

## save the Movies list into DB/Collection
def put_movie_into_DB (list_movies):
    i=len(list_movies)
    for movie in list_movies:
        new_movie = Movies_Collection(title=movie.get("Title"), year=movie.get("Year"), poster=movie.get("Poster"))
        new_movie.save()
    print(f"your_movies_collection have been {i} Movies saved successfully")

def delete_movie_from_DB (name):
    for movie in Movies_Collection.objects(name=name):
        movie.delete()

def get_movie_from_DB (name: str):
    for movie in Movies_Collection.objects:
        if movie.title == name:
            return movie.get_info()

def get_all_movies_from_DB():
    x=[]
    for movie in Movies_Collection.objects:
        data = movie.to_mongo().to_dict()
        data.pop("_id", None)
        x.append(data)
    return x

def get_all_movies_from_DB2():
    n_mov=[]
    for movie in Movies_Collection.objects:
        data = movie.to_mongo().to_dict()
        data.pop("_id", None)
    return n_mov





if __name__ == "__main__":

    #print(get_all_movies_from_DB2())

    #print(make_moviecard(get_all_movies_from_DB()))

    #for movie in Movies_Collection.objects:
    #    print(type(movie.to_mongo().to_dict()))
    print(Movies_Collection.objects.count())

#print(get_movie_from_DB("Titanic"))

    for user in Movies_Collection.objects:
        data= user.to_mongo().to_dict()
        print(data)
        print(data.get("title"))

print(Movies_Collection.objects)

print("first")
print(Movies_Collection.objects[2].to_mongo().to_dict().get("title"))
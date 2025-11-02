# mongodb+srv://rafeekslack_db_user:<db_password>@clus0.jnqagzn.mongodb.net/?appName=Clus0

from fastapi import FastAPI, Request, Response
from flask import Flask, render_template, request
import uvicorn
import string
import  requests
from FP_for_api import *
from FP_for_DB import *
from Show_movies_web import *
from Finale_project_Rafeek import FP_for_DB


if __name__ == "__main__":
    #get movie infos about avatar by API
    first_movie=get_movie_short_info("avatar", plus_key_globale)
    #put the movie into the list
    your_movies.append(first_movie)
    #create movie infos about titanic into the list
    create_movie(get_movie_short_info("titanic", plus_key_globale))
    create_movie(get_movie_short_info("rocky", plus_key_globale))

    # put_movie_into_DB(your_movies)

    #print(your_movies) # => list of dic
    #print(type(your_movies)) # => <class 'list'>
    #print(your_movies[0].get("Title"))
    #print(your_movies[0].get("Year"))
    #print(your_movies[0].get("Poster"))

    # save the movie into DB and crate new collection

    #print(len(your_movies))
    #print(get_movie_from_DB("Titanic"))

    #print(get_all_movies_from_DB())
    #your_movies=get_all_movies_from_DB()



    #app_flask.run(debug=True, use_reloader=False)
    uvicorn.run(app, host="127.0.0.1", port=8000)



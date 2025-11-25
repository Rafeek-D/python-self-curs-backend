

import flask
from fastapi import FastAPI, Request, Response
from flask import Flask, render_template, request
import uvicorn
import string
import  requests

from FP_main import *
from FP_for_api import *
from FP_for_DB import *
from DB_Class import *

from mongoengine import *

'''
list_of_movie=[{'Title': 'Avatar', 'Year': '2009',
                'Poster': 'https://m.media-amazon.com/images/M/MV5BMDEzMmQwZjctZWU2My00MWNlLWE0NjItMDJlYTRlNGJiZjcyXkEyXkFqcGc@._V1_SX300.jpg'},
               {'Title': 'Titanic', 'Year': '1997',
                'Poster': 'https://m.media-amazon.com/images/M/MV5BYzYyN2FiZmUtYWYzMy00MzViLWJkZTMtOGY1ZjgzNWMwN2YxXkEyXkFqcGc@._V1_SX300.jpg'}]
'''

def make_moviecard(list_of_movie):
    x= "\n"
    for dic in list_of_movie:
        title = dic.get('title')
        year = dic.get('year')
        poster = dic.get('poster')
        x= x + f"""
            <h1>{title}</h1>
            <p>{year}</p>
            <img src="{poster}" alt="{title}" width="200"/>
            <br>----------------------------------<br>
            """
    return x


your_movies = DB_Class_fun.get_all_movies_from_DB()

app_flask = flask.Flask(__name__)



@app_flask.route('/')
def index():
    #return "hi"
    return render_template('show_movies.html',
    #heading=a_in,
    #movie_card = movie_title,)
    movie_card=make_moviecard(your_movies, ))
    #movie_card=make_moviecard(get_all_movies_from_DB(),))




''' 
app_flask = flask.Flask(__name__)

@app_flask.route('/')
def index():
    #return "hi"
    return render_template('show_movies.html',
    #heading=a_in,
    #movie_card = movie_title,)
    movie_card=make_moviecard(list_of_movie, ))



if __name__ == '__main__':
    #print(list_of_movie[0].get('Title'))
    app_flask.run(debug=True, use_reloader=False)

'''

if __name__ == '__main__':
    print(your_movies)
 #   print(your_movies[0].get('title'))
    app_flask.run(debug=True, use_reloader=False)





##########testing#########
#mov=get_all_movies_from_DB_2()
#print(get_all_movies_from_DB())
#print(mov)
#print(your_movies)
#print(type(your_movies))

#print(your_movies[0].get('Title'))
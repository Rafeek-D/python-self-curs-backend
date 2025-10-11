import os

import flask
from fastapi import FastAPI, Request, Response
from flask import Flask, render_template, request
import uvicorn
import string
import  requests


def show_movie_infos(movie_title):
    #response_show_movie_title = requests.get(url_part1 + titel_input + movie_title + plus_key)
    response_show_movie_inf = requests.get(f"http://www.omdbapi.com/?t={movie_title}&apikey=1b0aaab6")
    return response_show_movie_inf.json()
    #return response_show_movie_title


#print(show_movie_infos("titanic"))

############

app_flask = flask.Flask(__name__)

heading_text= " infos about Your Movie are:"
movie_title = show_movie_infos("titanic")
foto= "https://m.media-amazon.com/images/M/MV5BYzYyN2FiZmUtYWYzMy00MzViLWJkZTMtOGY1ZjgzNWMwN2YxXkEyXkFqcGc@._V1_SX300.jpg"

@app_flask.route('/')
def index():
    #return "hi"
    return render_template('test.html',
    #heading = heading_text,
    heading=a_in,
    para = movie_title,
    image = foto,
                           )
    #return render_template('for_code.html')


#def run_code():
    app_flask.run(debug=True)

#a_in = input("put your heading here")
#run_code()

''' 
## from cg

if __name__ == '__main__':
    # Only run this in the MAIN process, not the reloader
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true' and app_flask.debug:
        # Skip input on first run (used only to trigger the reloader)
        pass
    else:
        # Real main run: ask input once
        a_in = input("Put your heading here: ")

    # Now start Flask app (debug=True will auto-reload)
    app_flask.run(debug=True, use_reloader=False)
'''

##from m
if __name__ == '__main__':
    a_in= input("put your heading here")
    #app_flask.run(debug=True)  ## here it will reload the code after every change and with input it execute often
    app_flask.run(debug=True, use_reloader=False) ## here it will not reload the code and input only one time

##











##########
""" 
## leater

#app = FastAPI()


@app.get("/")
def get_root():


## here is the src="{movie.Poster}" get the Poster from the response of the
def movie_card_func (movie):
    return '''  <a
        href="#"
        target="_blank"
        class="movie-card"
      >
        <img
          src="{movie.Poster}"
          alt="Pi Poster"
        />
        <div class="movie-info">
          <h2>Pi</h2>
          <p>Year: 2008</p>
          <p>⭐ Rating: 9.0</p>
        </div>
      </a> '''
"""
#############
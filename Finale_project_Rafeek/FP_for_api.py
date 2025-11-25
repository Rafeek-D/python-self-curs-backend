#xxxab6
import flask
from fastapi import FastAPI, Request, Response
from flask import Flask, render_template, request
import uvicorn
import string
from typing import List, Dict
import  requests

from FP_for_DB import *
from DB_Class import DB_Class_fun
from lession_10_minipro_movies.mini_pro_movies_with_htmlflask import movie_title

#url = "http://www.omdbapi.com/?t=titanic&apikey=1b0aa...."


#url_part1= "http://www.omdbapi.com/?"
#titel_input= "t="
#name_input= "titanic"
plus_key_globale= "&apikey=1b0aa..."


def get_url_from_titele(movie_title,plus_key):
    return requests.get(f"http://www.omdbapi.com/?t={movie_title}"+plus_key)


def get_movie_infos(movie_title,plus_key):
    #response_show_movie_inf = requests.get(f"http://www.omdbapi.com/?t={movie_title}&apikey=1b0aaab6")
    response_show_movie_inf = requests.get(f"http://www.omdbapi.com/?t={movie_title}"+plus_key)
    return response_show_movie_inf.json()
    #return response.text

def get_movie_response_status1(movie_title,plus_key):
    response_show_status = requests.get(f"http://www.omdbapi.com/?t={movie_title}"+plus_key)
    return int(response_show_status.status_code)

def get_movie_response_status2(response):
    code= response.status_code
    return code

def get_movie_short_info(movie_title,plus_key):
    response_show_movie_inf = requests.get(f"http://www.omdbapi.com/?t={movie_title}" + plus_key)
    dic_response= response_show_movie_inf.json()
    dic= {"title":dic_response.get("Title"),"year":dic_response.get("Year"),"poster":dic_response.get("Poster")}
    return dic

def get_movie_response_status_movie_name(movie_title,plus_key):
    response_show_status = requests.get(f"http://www.omdbapi.com/?t={movie_title}" + plus_key)
    return  int(response_show_status.status_code)



app = FastAPI()
movies =[]
#your_movies=[]
#your_movies = get_all_movies_from_DB()
#your_movies = DB_Class_fun.get_all_movies_from_DB()
@app.get("/")
def read_root():
    return {"message": "Hello, your Movies Database"}


@app.get("/your_movies")
def get_movies():
    return your_movies

##
@app.get("/your_movies/getone/{movie_name}")
def get_user2(movie_name: str):
    for movie in your_movies:
        if movie.get("title") == movie_name:
            return movie
### the number of user_id in Browser is from 0,1,....


@app.post("/to_list/movie")
def create_movie(movie: dict):
    your_movies.append(movie)
    if get_movie_response_status_movie_name(dict["Title"],plus_key_globale) == 200:
        print(f'the status is:', get_movie_response_status_movie_name(dict["Title"],plus_key_globale))
    else:
        print("the status is not 200")
    return movie

#####
@app.put("/movie_update_year/{movie_name}")
def update_movie(movie_name: str, your_movies: List[Dict]):
    for movie in your_movies:
        if movie.get("title") == movie_name:
            movie["year"]="2025"
            return {"message": "Movie updated successfully", "movie": movie}
    return {"error": "User not found"}


@app.delete("/delete_movie/{movie_name}")
def delete_user(movie_name: str):
    for movie in your_movies:
        if movie["title"] == movie_name:
            return your_movies.pop(movie)
    DB_Class_fun.delete_one_movie_from_DB(movie_name)
    return {"error": "User not found"}




################# testing######
#response = requests.get(url_part1 + titel_input + name_input +plus_key)
#print(response.json()) #<class 'dict'>
#print(response.text)  #<class 'str'>
#print(response.json().get('Title'))  #Titanic


#print(get_movie_infos("avatar",plus_key_globale)) #{'Title': 'Avatar', 'Year': ....}
#print(type(get_movie_infos("avatar",plus_key_globale))) #<class 'dict'>
#print("the title: " + get_movie_infos("avatar",plus_key_globale).get("Title"))
#print("the year: " + get_movie_infos("avatar",plus_key_globale).get("Year"))
#print("the year: " + get_movie_infos("avatar",plus_key_globale).get("Poster"))
#print(get_movie_response_status2(get_url_from_titele("avatar",plus_key_globale)))


#print(get_movie_short_info("titanic",plus_key_globale))
#print(get_movie_short_info("titanic",plus_key_globale).get("Title"))
#t=get_movie_short_info("titanic",plus_key_globale)["Title"]
#t=get_movie_short_info("titanic",plus_key_globale)["Title"]="ttt"
#print(t)
#print(len(your_movies))


#create_movie(get_movie_short_info("rocky", plus_key_globale))
#print(len(your_movies))
#print(get_movie_response_status_movie_name("titanic",plus_key_globale))
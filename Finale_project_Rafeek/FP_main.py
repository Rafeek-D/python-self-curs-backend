# mongodb+srv://rafeekslack_db_user:<db_password>@clus0.jnqagzn.mongodb.net/?appName=Clus0

from fastapi import FastAPI, Request, Response
from flask import Flask, render_template, request
import uvicorn
import string
import  requests
from FP_for_api import *
from FP_for_DB import *
from Finale_project_Rafeek.DB_Class import DB_Class_fun
from Show_movies_web import *
from Finale_project_Rafeek import FP_for_DB
from DB_Class import *
from Show_movies_web import *

#####################option 1 without the while loop###############################
#if __name__ == "__main__":

    #0) macke sure the list of the movies from DB
    #your_movies = DB_Class_fun.get_all_movies_from_DB()

    #1) create movie infos into the list, but not one movie, if the DB exist:

    #create_movie(get_movie_short_info("titanic", plus_key_globale))
    #create_movie(get_movie_short_info("rocky", plus_key_globale))
    #create_movie(get_movie_short_info("avatar", plus_key_globale))

    #2) save the movie into DB and crate new collection:

    #DB_Class_fun.put_movie_into_DB(your_movies)

    #one movie add
    #DB_Class_fun.put_one_movie_into_DB(create_movie(get_movie_short_info("titanic", plus_key_globale)))
    #

    #3) print the movies:
    #your_movies = DB_Class_fun.get_all_movies_from_DB()
    #print(len(your_movies))
    # print(DB_Class_fun.get_movie_from_DB("Titanic"))
    #print(DB_Class_fun.get_all_movies_from_DB())

    #4) delete all movie with the name:
    #DB_Class_fun.delete_movie_from_DB("Titanic")
    #print(your_movies)

    #5) delete all the movies from DB
    #DB_Class_fun.delete_all_movies_from_DB()
    #print(len(your_movies))

    #delete one movie
    #DB_Class_fun.delete_one_movie_from_DB(Titanic)

    #6) as a html overview:
    #app_flask.run(debug=True, use_reloader=False)

    #7) as a api overview:
    #uvicorn.run(app, host="127.0.0.1", port=8000)


######################option 2 with while loop##############################################

if __name__ == "__main__":
    while True:
        name = input("Enter what do you want, or 'goout' to exit: \n"
                     "1) list all the movies from DB\n"
                     "2) create new movie from api to DB \n"
                     "3) get one movie from DB\n"
                     "4) remove one movie from DB\n"
                     "5) show the result into as a api (put api and not number)\n"
                     "6) show the result as a HTML (put html and not nubmer)\n"
                     ).strip().lower()

        if name == "goout":
            print("Exiting program...")
            break

        # Handle t1 / t2 / t3
        if name == "1":
            your_movies = DB_Class_fun.get_all_movies_from_DB()
            print(f'you have {len(your_movies)} movies from DB')
            #movies_with_line= your_movies
            #i = 0
            for i in range(len(your_movies)):
                print(f'the {i+1} movie is {your_movies[i].get("title")}:')
                print(your_movies[i])
                i += i + 1
            #print("the movie are\n:" ,movies_with_line)
        elif name == "2":
            x= True
            #movie_name = input("put the name for the create movie: ")
            while x:
                movie_name = input("put the name for the create movie: ")
                if movie_name:
                    #create_movie(get_movie_short_info(movie_name, plus_key_globale))
                    DB_Class_fun.put_one_movie_into_DB(create_movie(get_movie_short_info(movie_name, plus_key_globale)))
                    your_movies = DB_Class_fun.get_all_movies_from_DB()
                    x= False
                else:
                    print("Unknown option. Try again.\n")
                    continue
        elif name == "3":
            movie_name = input("put the name for the get movie: ")
            print(DB_Class_fun.get_movie_from_DB(movie_name))
        elif name == "4":
            #delete one movie
            movie_name = input("put the name for the remove movie: ")
            DB_Class_fun.delete_one_movie_from_DB(movie_name)

        #elif name == "4":
         #   print("4")
        # =========================
        # NEW CASE: api / html
        # =========================
        elif name == "api":
            print("Starting FastAPI server...")
            uvicorn.run(app, host="127.0.0.1", port=8000)
            break  # END LOOP AFTER SERVER STARTS
        elif name == "html":
            print("Starting Flask server...")
            your_movies=DB_Class_fun.get_all_movies_from_DB()

            app_flask.run(debug=True, use_reloader=False)
            break  # END LOOP AFTER SERVER STARTS
        else:
            print("Unknown option. Try again.\n")
            continue















###############testing###############################

  #get movie infos about avatar by API
    #first_movie=get_movie_short_info("avatar", plus_key_globale)

    #put the movie into the list
    #your_movies.append(first_movie)

# print(your_movies) # => list of dic
# print(type(your_movies)) # => <class 'list'>
# print(your_movies[0].get("Title"))
# print(your_movies[0].get("Year"))
# print(your_movies[0].get("Poster"))


#your_movies= FP_for_DB.get_all_movies_from_DB()
    #your_movies = DB_Class_fun.get_all_movies_from_DB()
    #print(your_movies)
    #print(len(your_movies))
    #your_movies.append(get_movie_short_info("rocky", plus_key_globale))
    #print(len(your_movies))
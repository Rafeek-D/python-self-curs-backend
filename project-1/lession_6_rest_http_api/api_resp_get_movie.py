
#from tkinter.font import names
import string

import  requests

url = "http://www.omdbapi.com/?t=titanic&apikey=1b0aaab6"
url_part1= "http://www.omdbapi.com/?"
titel_input= "t="
name_input= "titanic"
plus_key= "&apikey=1b0aaab6"

#response = requests.get(url)
response = requests.get(url_part1 + titel_input + name_input +plus_key)
#print(response.json())
#print(response.text)
#print(response.json().get('Title'))

def show_movie_infos(movie_title):
    #response_show_movie_title = requests.get(url_part1 + titel_input + movie_title + plus_key)
    response_show_movie_inf = requests.get(f"http://www.omdbapi.com/?t={movie_title}&apikey=1b0aaab6")
    return response_show_movie_inf.json()
    #return response_show_movie_title

def get_movie_response_status(movie_title):
    response_show_status = requests.get(f"http://www.omdbapi.com/?t={movie_title}&apikey=1b0aaab6")
    return int(response_show_status.status_code)




print("the infos about the movie:")
print(show_movie_infos("avatar"))
#{'Title': 'Avatar', 'Year': '2009', 'Rated': 'PG-13', .....}

print("the title: " + show_movie_infos("avatar").get("Title"))
print("the year: " + show_movie_infos("avatar").get("Year"))

print("the code(200 or so): ",response.status_code)
#print(show_movie_infos("avatar").status_code)

print(type(show_movie_infos("avatar")))
# <class 'dict'>

print(isinstance(show_movie_infos("avatar"), dict))
#TRUE

print(show_movie_infos("avatar").keys())
#dict_keys(['Title', 'Year', 'Rated', 'Released', 'Runtime', .....'Response'])


print(type(show_movie_infos("avatar").keys()))
# <class 'dict_keys'>

print(show_movie_infos("avatar").items())
# ict_items([('Title', 'Avatar'), ('Year', '2009'),.....

print("the key Title is in:"  , "Title" in show_movie_infos("avatar").keys())
#the key Title is in: True

print("the word Error is in:" , "Error" in show_movie_infos("avatar").keys())
# the word Error is in: False
print( "the negativ from false: " , not ("Error" in show_movie_infos("avatar").keys()))
#the negativ from false:  True



####
name="T"
age= 3
string_com= "test %s and num %d n."%(name,age)
print(string_com)
#test T and num 3 n.
######

print("###########Program take infos about movie from API#########")

movie_name= input("put the name to show the infos aubout it:")
#print(movie_name.lower())
error_is_in_dic= ("Error" in show_movie_infos(movie_name).keys())

if get_movie_response_status(movie_name) == 200 and isinstance(show_movie_infos(movie_name), dict) and  show_movie_infos(movie_name)\
        and not error_is_in_dic:
    print("its ok")
    print(show_movie_infos(movie_name))
else:
    print("its not ok")


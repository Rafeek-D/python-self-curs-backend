from tkinter.font import names

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

def show_movie_title(movie_title):
    #response_show_movie_title = requests.get(url_part1 + titel_input + movie_title + plus_key)
    response_show_movie_title = requests.get(f"http://www.omdbapi.com/?t={movie_title}&apikey=1b0aaab6")
    return response_show_movie_title.json()
    #return response_show_movie_title

print(show_movie_title("avatar"))
print("the title: " + show_movie_title("avatar").get("Title"))
print("the year: " + show_movie_title("avatar").get("Year"))
print(response.status_code)

####
name="T"
age= 3
string_com= "test %s and num %d n."%(name,age)
print(string_com)
######
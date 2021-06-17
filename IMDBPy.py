# import imdb
#
# access = imdb.IMDb()
# movie = access.get_movie(1132626)
#
# print("title: %s year: %s" % (movie['title'], movie['year']))
# print("Cover url: %s" % movie['cover url'])
#
#
#
#
# from imdb import IMDb
# ia = IMDb()
#
#
# def getmovieID(movie_name):
#     movie = ia.search_movie(movie_name)[0]
#     get_movie = ia.get_movie(movie.movieID)
#     return get_movie
#
#
# def getcast(movie_name):
#     movie = getmovieID(movie_name)
#     casts_objects = movie.get('cast')
#     casts = []
#     for person in casts_objects:
#         casts.append(person.get('name'))
#     return casts
#
# print(getcast('Saw'))

import requests
import base64
from tkinter import *
window=Tk()

url = "https://upload.wikimedia.org/wikipedia/commons/8/8f/FullColourGIF.gif"

encodedPic = base64.(requests.get(url).content)
image = PhotoImage(data=encodedPic)
label = Label(image=image)
label.pack()

window.title('Check my cool thumbnail fetcher')
window.mainloop()
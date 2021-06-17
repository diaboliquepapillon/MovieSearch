from tkinter import *
from tkinter.ttk import Progressbar, Style
import imdb
from PIL import Image
from io import BytesIO
import requests
import tkinter.font as font
import datetime
import json

access = imdb.IMDb()

def open_dialog(userid):
    moviewindow = Tk()
    moviewindow.state("zoomed")
    moviewindow.title('Login Form')
    moviewindow.geometry(f'{moviewindow.winfo_screenwidth()}x{moviewindow.winfo_screenheight()}')
    moviewindow.resizable(FALSE, NO)
    moviewindow.config(bg='white')

    moviewindow.option_add('*Font', 'Verdana')
    moviewindow.option_add('*Background', 'white')

    Label(text="Search : ", fg='black').place(x=10, y=11)
    search_entry = Entry(moviewindow, fg='black')
    search_entry.place(x=90, y=10, height=25, width=moviewindow.winfo_screenwidth() - 250)
    Button(text="Find", fg='white', bg='#E50914', command=lambda: search(search_entry.get())).place(x=moviewindow.winfo_screenwidth() - 150, y=10, height=26, width=140)

    s = Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')

    progress = Progressbar(moviewindow, style="red.Horizontal.TProgressbar", orient = HORIZONTAL, length = 100, mode = 'determinate')
    progress.place(anchor='sw', x=10, y=62, width=moviewindow.winfo_screenwidth() - 20, bordermode="outside")
    
    def load_search_history():
        clear_frame()
        myfont = font.Font(size=10)
        xplacement = 5
        yplacement = 27

        label = Label(mainframe, text='Userid', bg="white", fg="black")
        label['font'] = font.Font(size=10, weight='bold')
        label.place(x=5, y=0)

        label = Label(mainframe, text='Search Term', bg="white", fg="black")
        label['font'] = font.Font(size=10, weight='bold')
        label.place(x=150, y=0)

        label = Label(mainframe, text='Date & time', bg="white", fg="black")
        label['font'] = font.Font(size=10, weight='bold')
        label.place(x=300, y=0)

        seperator = Frame(mainframe, bg='black')
        seperator.place(x=8, y=21, height=2, width=mainframe.winfo_width()-40)  

        try:
            history = json.loads(open('./history.json').read())
        except:
            history = []
        if history:
            history = [x for x in history if x['userid'] == userid]

        for row in history:
            label = Label(mainframe, text=row['userid'], bg="white", fg="black")
            label['font'] = myfont
            label.place(x=xplacement, y=yplacement)

            label = Label(mainframe, text=row['search_term'], bg="white", fg="black")
            label['font'] = myfont
            label.place(x=xplacement + 150, y=yplacement)

            label = Label(mainframe, text=row['search_time'], bg="white", fg="black")
            label['font'] = myfont
            label.place(x=xplacement + 300, y=yplacement)

            seperator = Frame(mainframe, bg='grey')
            seperator.place(x=xplacement+4, y=yplacement+21, height=1, width=mainframe.winfo_width()-40)
            yplacement+=25

    def load_watch_list():
        clear_frame()
        myfont = font.Font(size=10)
        xplacement = 5
        yplacement = 65

        label = Label(mainframe, text='My Watchlist', bg="white", fg="black")
        label['font'] = font.Font(size=20, weight='bold')
        label.place(x=5, y=0)        

        seperator = Frame(mainframe, bg='black')
        seperator.place(x=8, y=35, height=2, width=mainframe.winfo_width()-40)

        label = Label(mainframe, text='Userid', bg="white", fg="black")
        label['font'] = font.Font(size=10, weight='bold')
        label.place(x=5, y=40)

        label = Label(mainframe, text='Movie Name', bg="white", fg="black")
        label['font'] = font.Font(size=10, weight='bold')
        label.place(x=150, y=40)

        label = Label(mainframe, text='Date Added', bg="white", fg="black")
        label['font'] = font.Font(size=10, weight='bold')
        label.place(x=500, y=40)

        seperator = Frame(mainframe, bg='black')
        seperator.place(x=8, y=62, height=2, width=mainframe.winfo_width()-40)

        try:
            watch_list = json.loads(open('./watch_list.json').read())
        except:
            watch_list = []
        if watch_list:
            watch_list = [x for x in watch_list if x['userid'] == userid]

        for row in watch_list:
            label = Label(mainframe, text=row['userid'], bg="white", fg="black")
            label['font'] = myfont
            label.place(x=xplacement, y=yplacement)

            label = Label(mainframe, text=row['movie_name'], bg="white", fg="black")
            label['font'] = myfont
            label.place(x=xplacement + 150, y=yplacement)

            label = Label(mainframe, text=row['date_added'], bg="white", fg="black")
            label['font'] = myfont
            label.place(x=xplacement + 500, y=yplacement)

            seperator = Frame(mainframe, bg='grey')
            seperator.place(x=xplacement+4, y=yplacement+21, height=1, width=mainframe.winfo_width()-40)
            yplacement+=25

    def load_watched_movies_list():
        clear_frame()
        myfont = font.Font(size=10)
        xplacement = 5
        yplacement = 65

        label = Label(mainframe, text='Movies I already watched', bg="white", fg="black")
        label['font'] = font.Font(size=20, weight='bold')
        label.place(x=5, y=0)        

        seperator = Frame(mainframe, bg='black')
        seperator.place(x=8, y=35, height=2, width=mainframe.winfo_width()-40)

        label = Label(mainframe, text='Userid', bg="white", fg="black")
        label['font'] = font.Font(size=10, weight='bold')
        label.place(x=5, y=40)

        label = Label(mainframe, text='Movie Name', bg="white", fg="black")
        label['font'] = font.Font(size=10, weight='bold')
        label.place(x=150, y=40)

        label = Label(mainframe, text='Date Added', bg="white", fg="black")
        label['font'] = font.Font(size=10, weight='bold')
        label.place(x=500, y=40)

        seperator = Frame(mainframe, bg='black')
        seperator.place(x=8, y=62, height=2, width=mainframe.winfo_width()-40)

        try:
            watched_movies = json.loads(open('./watched_movies.json').read())
        except:
            watched_movies = []
        if watched_movies:
            watched_movies = [x for x in watched_movies if x['userid'] == userid]

        for row in watched_movies:
            label = Label(mainframe, text=row['userid'], bg="white", fg="black")
            label['font'] = myfont
            label.place(x=xplacement, y=yplacement)

            label = Label(mainframe, text=row['movie_name'], bg="white", fg="black")
            label['font'] = myfont
            label.place(x=xplacement + 150, y=yplacement)

            label = Label(mainframe, text=row['date_added'], bg="white", fg="black")
            label['font'] = myfont
            label.place(x=xplacement + 500, y=yplacement)

            seperator = Frame(mainframe, bg='grey')
            seperator.place(x=xplacement+4, y=yplacement+21, height=1, width=mainframe.winfo_width()-40)
            yplacement+=25

    def close_program():
        moviewindow.destroy()

    def place_menu_buttons():
        menu_buttons_width = 200
        menu_buttons_height = 40

        first_button_x_location = moviewindow.winfo_screenwidth() // 7
        button_y_location = moviewindow.winfo_screenheight() - 70

        history_button = Button(moviewindow, text='Search History', fg='white', bg='#E50914', command=load_search_history)
        history_button.place(x=first_button_x_location, y=button_y_location, height=menu_buttons_height, width=menu_buttons_width)

        watch_list_button = Button(moviewindow, text='My Watchlist', fg='white', bg='#E50914', command=load_watch_list)
        watch_list_button.place(x=first_button_x_location + 210, y=button_y_location, height=menu_buttons_height, width=menu_buttons_width)

        watched_movies_button = Button(moviewindow, text='My Watched Movies', fg='white', bg='#E50914', command=load_watched_movies_list)
        watched_movies_button.place(x=first_button_x_location + 420, y=button_y_location, height=menu_buttons_height, width=menu_buttons_width)

        clear_search_results = Button(moviewindow, text='Clear Search Results', fg='white', bg='#E50914', command=clear_frame)
        clear_search_results.place(x=first_button_x_location + 630, y=button_y_location, height=menu_buttons_height, width=menu_buttons_width)

        exit_button = Button(moviewindow, text='Exit', fg='white', bg='#E50914', command=close_program)
        exit_button.place(x=first_button_x_location + 840, y=button_y_location, height=menu_buttons_height, width=menu_buttons_width)

    def clear_frame():
        # destroy all widgets from frame
        for widget in mainframe.winfo_children():
           widget.destroy()

    mainframe = Frame(moviewindow, relief=GROOVE, bd=10)
    mainframe.place(x=10, y=70, width=moviewindow.winfo_screenwidth()-19, height=moviewindow.winfo_screenheight() - 150)
    
    place_menu_buttons()

    def add_to_watch_list(movie_data):
        try:
            watch_list = json.loads(open('./watch_list.json').read())
        except:
            watch_list = []
        watch_list.append({'userid':userid, 'movie_name': movie_data.data['title'], 'date_added': str(datetime.datetime.now())})
        db = open('./watch_list.json','w')
        db.write(json.dumps(watch_list))

    def add_to_watched(movie_data):
        try:
            watched_movies = json.loads(open('./watched_movies.json').read())
        except:
            watched_movies = []
        watched_movies.append({'userid':userid, 'movie_name': movie_data.data['title'], 'date_added': str(datetime.datetime.now())})
        db = open('./watched_movies.json','w')
        db.write(json.dumps(watched_movies))

    def search(search_string):
        try:
            history = json.loads(open('./history.json').read())
        except:
            history = []
        history.append({'userid':userid, 'search_term': search_string, 'search_time': str(datetime.datetime.now())})
        db = open('./history.json','w')
        db.write(json.dumps(history))
        
        myfont = font.Font(size=10)
        advratio = 10
        results = access.search_movie(search_string)
        advratio = 100/len(results)
        progress['value'] = 0
        moviewindow.update_idletasks()
        movie_index = 0
        xplacement = 5
        yplacement = 27

        name_label = Label(mainframe, text='Movie Name', bg="white", fg="black")
        name_label['font'] = font.Font(size=10, weight='bold')
        name_label.place(x=5, y=0)

        actions_label = Label(mainframe, text='Actions', bg="white", fg="black")
        actions_label['font'] = font.Font(size=10, weight='bold')
        actions_label.place(x=mainframe.winfo_width()-180, y=0)

        actions_label = Label(mainframe, text='Actions', bg="white", fg="black")
        actions_label['font'] = font.Font(size=10, weight='bold')
        actions_label.place(x=mainframe.winfo_width()-180, y=0)       

        rating_label = Label(mainframe, text='Rating', bg="white", fg="black")
        rating_label['font'] = font.Font(size=10, weight='bold')
        rating_label.place(x=mainframe.winfo_width()-360, y=0)
        
        genre_label = Label(mainframe, text='Genre', bg="white", fg="black")
        genre_label['font'] = font.Font(size=10, weight='bold')
        genre_label.place(x=mainframe.winfo_width()-500, y=0)

        seperator = Frame(mainframe, bg='black')
        seperator.place(x=8, y=21, height=2, width=mainframe.winfo_width()-40)        
        for movie in results[:5]:
            movie_index+=1

            movieID = int(movie.getID())
            movie_data = access.get_movie(movieID)

            try:
                rating=movie_data.data['rating']
            except:
                rating='N/A'
            try:
                genre = movie_data.data['genres'][0]
            except:
                genre = 'N/A'

            progress['value'] += advratio
            moviewindow.update_idletasks()
            mainframe.update()

            movie_year = ""

            if "year" in movie.keys(): movie_year = str(movie['year'])
            
            label = Label(mainframe, text=movie['title']+" ("+movie_year+")", bg="white", fg="black")
            label['font'] = myfont
            label.place(x=xplacement, y=yplacement)

            label = Label(mainframe, text=rating, bg="white", fg="black")
            label['font'] = myfont
            label.place(x=mainframe.winfo_width()-360, y=yplacement)

            label = Label(mainframe, text=genre, bg="white", fg="black")
            label['font'] = myfont
            label.place(x=mainframe.winfo_width()-500, y=yplacement)

            button = Button(mainframe, text="Add to Watchlist", fg='white', bg='#E50914', command=lambda movie_data=movie_data: add_to_watch_list(movie_data))
            button['font'] = myfont
            button.place(x=mainframe.winfo_width()-280, y=yplacement, height=18, width=120)

            button = Button(mainframe, text="Watched", fg='white', bg='#E50914', command=lambda movie_data=movie_data: add_to_watched(movie_data))
            button['font'] = myfont
            button.place(x=mainframe.winfo_width()-150, y=yplacement, height=18, width=120)

            url = movie['full-size cover url']
            im = Image.open(BytesIO(requests.get(url).content))
            im.save('images/image'+str(movie_index)+'.png', 'PNG')

            seperator = Frame(mainframe, bg='grey')
            seperator.place(x=xplacement+4, y=yplacement+21, height=1, width=mainframe.winfo_width()-40)
            yplacement+=25

if __name__ == "__main__":
    open_dialog()
from tkinter import *
from tkinter.ttk import Progressbar, Style
import imdb
from PIL import Image
from io import BytesIO
import requests

access = imdb.IMDb()

def open_dialog():
    WIDTH = 900
    HEIGHT = 780

    moviewindow = Tk()
    moviewindow.title('Login Form')
    moviewindow.geometry(f'{WIDTH}x{HEIGHT}')
    moviewindow.resizable(FALSE, NO)
    moviewindow.config(bg='white')


    moviewindow.option_add('*Font', 'Verdana')
    moviewindow.option_add('*Background', 'white')

    Label(text="Search : ", fg='black').place(x=10, y=11)
    search_entry = Entry(moviewindow, fg='black')
    search_entry.place(x=90, y=10, height=25, width=660)
    Button(text="Find", fg='white', bg='#E50914', command=lambda: search(search_entry.get())).place(x=760, y=10, height=26, width=130)

    menuframe = Frame(moviewindow, bd=10, bg='white')
    menuframe.place(x=70, y=70, width=160, height=700, anchor='n')
    
    seperator = Frame(moviewindow, bd=10, bg='grey')
    seperator.place(x=143, y=70, width=1, height=700, anchor='n')

    Button(menuframe, text="Menu", fg='white', bg='#E50914').place(x=5, y=00, height=26, width=130)
    Button(menuframe, text="Menu", fg='white', bg='#E50914').place(x=5, y=40, height=26, width=130)
    Button(menuframe, text="Menu", fg='white', bg='#E50914').place(x=5, y=80, height=26, width=130)
    Button(menuframe, text="Menu", fg='white', bg='#E50914').place(x=5, y=120, height=26, width=130)
    Button(menuframe, text="Menu", fg='white', bg='#E50914').place(x=5, y=160, height=26, width=130)
    Button(menuframe, text="Menu", fg='white', bg='#E50914').place(x=5, y=200, height=26, width=130)
    Button(menuframe, text="Menu", fg='white', bg='#E50914').place(x=5, y=240, height=26, width=130)
    Button(menuframe, text="Menu", fg='white', bg='#E50914').place(x=5, y=280, height=26, width=130)
    Button(menuframe, text="Disconnect", fg='white', bg='#E50914').place(x=5, y=660, height=26, width=130)

    mainframe = Frame(moviewindow, relief=GROOVE, bd=10)
    mainframe.place(x=520, y=70, width=740, height=700, anchor='n')

    s = Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
    progress = Progressbar(moviewindow, style="red.Horizontal.TProgressbar", orient = HORIZONTAL, length = 100, mode = 'determinate')
    progress.place(anchor='sw', x=10, y=62, width=870, bordermode="outside")
     
    
    def search(search_string):
        mainframe = Frame(moviewindow, relief=GROOVE, bd=10)
        mainframe.place(x=520, y=70, width=740, height=700, anchor='n')
        advratio = 10
        results = access.search_movie(search_string)
        advratio = 100/len(results)
        progress['value'] = 0
        moviewindow.update_idletasks()
        movie_index = 0
        xplacement = 5
        yplacement = 5
        for movie in results:
            movie_index+=1

            progress['value'] += advratio
            moviewindow.update_idletasks()

            movie_year = ""

            if "year" in movie.keys(): movie_year = str(movie['year'])
            
            Label(mainframe, text=movie['title']+" ("+movie_year+")", bg="white", fg="black").place(x=xplacement, y=yplacement)
            Button(mainframe, text="Details", fg='white', bg='#E50914').place(x=646, y=yplacement, height=26, width=62)

            url = movie['cover url'].replace('@._V1_UX32_CR0,0,32,44_AL_.', '@._V1_SX300.')
            im = Image.open(BytesIO(requests.get(url).content))
            im.save('images/image'+str(movie_index)+'.png', 'PNG')

            seperator = Frame(mainframe, bg='grey')
            seperator.place(x=xplacement+5, y=yplacement+40, width=700, height=2)
            yplacement+=50

        

if __name__ == "__main__":
    open_dialog()
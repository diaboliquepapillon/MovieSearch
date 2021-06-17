from tkinter import *

HEIGHT = 534
WIDTH = 413
# #------------------------------- Functions--------------------------------


# #------------------------------- Functions--------------------------------

selected_movie = Tk()
selected_movie.title("Your Movie")
selected_movie.geometry(f'{HEIGHT}x{WIDTH}')
selected_movie.resizable(FALSE, NO)

C = Canvas(selected_movie, height=534, width=413)
background_image = PhotoImage(file='./movie.png')
background_label = Label(selected_movie, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

main_frame = Frame(selected_movie)
main_frame.place(relx=0.094, rely=0.048, relheight=0.831, relwidth=0.794)

image_frame = Frame(main_frame, background="#000000")
image_frame.place(relx=0.024, rely=0.029, relheight=0.51, relwidth=0)

movie_name = Label(main_frame, text = 'MOVIE NAME')
movie_name.place(relx=0.59, rely=0.058, height=31, width=74)

info = Label(main_frame, text = 'Info')
info.place(relx=0.448, rely=0.175, height=251, width=194)

seen_button = Button(main_frame, text='Seen this Movie')
seen_button.place(relx=0.04, rely=0.691, height=34, width=127)

wish_button = Button(main_frame, text='Add to my Wish List')
wish_button.place(relx=0.04, rely=0.604, height=34, width=127)





selected_movie.mainloop()
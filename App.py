from tkinter import *
from tkinter import messagebox
from mainwindowR2 import open_dialog
import json
import datetime

HEIGHT = 1000
WIDTH = 560
users = {}

# #------------------------------- Functions--------------------------------

def registration():
    global users
    label_error = None

    frame = Frame(app, bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7,
                relheight=0.6, anchor='n')

    label = Label(frame, text='Sign Up', font='25')
    label.place(relwidth=1, relheight=0.1)

    label_login = Label(frame, text='Login:')
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    login_register = Entry(frame)
    login_register.place(relx=0.4, rely=0.2,
                         relheight=0.1, relwidth=0.55)

    label_pass1 = Label(frame, text='Password:')
    label_pass1.place(rely=0.4, relwidth=0.35, relheight=0.1)

    password1 = Entry(frame, show='*')
    password1.place(relx=0.4, rely=0.4,
                         relheight=0.1, relwidth=0.55)

    label_pass2 = Label(frame, text='Confirm password:')
    label_pass2.place(rely=0.6, relwidth=0.35, relheight=0.1)

    password2 = Entry(frame, show='*')
    password2.place(relx=0.4, rely=0.6,
                    relheight=0.1, relwidth=0.55)

    button = Button(frame, text='Sign Up', command=lambda: signup())
    button.place(relx=0.3, rely=0.8, relheight=0.15, relwidth=0.5)

    def signup():
        users = json.loads(open('./db.json').read())
        nonlocal label_error
        error = ''
        if label_error:
            label_error.destroy()

        if len(login_register.get()) == 0:
            error = '*login error'
        elif login_register.get() in [x['login'] for x in users]:
            error = '*Username already exists'
        elif len(password1.get()) < 6 or len(password1.get()) > 14:
            error = '*your password needs to be between 6 and 14 characters'
        elif not password1.get() == password2.get():
            error = '*password error'
        else:
            save()

        label_error = Label(frame, text=error, fg='red')
        label_error.place(rely=0.7)

    def save():
        user = {
            'userid': str(datetime.datetime.timestamp(datetime.datetime.now())).replace('.',''),
            'login': login_register.get(),
            'password': password1.get()

        }
        users = json.loads(open('./db.json').read())
        users.append(user)
        db = open('./db.json','w')
        db.write(json.dumps(users))


        # users[login_register.get()] = password1.get()
        # with open('users.vv', 'wb') as f:
        #     pickle.dump(users, f)

        login_form()


def login_form():
    frame = Frame(app, bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7,
                relheight=0.6, anchor='n')

    label = Label(frame, text='Sign In', font='16')
    label.place(relwidth=1, relheight=0.1)

    label_login = Label(frame, text='Login:')
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    login_enter = Entry(frame)
    login_enter.place(relx=0.4, rely=0.2,
                         relheight=0.1, relwidth=0.55)

    label_pass = Label(frame, text='Password:')
    label_pass.place(rely=0.4, relwidth=0.35, relheight=0.1)

    password_field = Entry(frame, show='*')
    password_field.place(relx=0.4, rely=0.4,
                    relheight=0.1, relwidth=0.55)

    button = Button(frame, text='Sign In', command=lambda: login_pass())
    button.place(relx=0.3, rely=0.8, relheight=0.15, relwidth=0.5)
    def login_pass():
        loggedin = False
        users = json.loads(open('./db.json').read())
        for user in users:
            if user['login'] == login_enter.get() and user['password'] == password_field.get():
                loggedin = True
                #messagebox.showinfo('Welcome', 'Welcome to app')
                app.destroy()
                open_dialog(user['userid'])

        if not loggedin: messagebox.showerror('Error','Invalid login or password')

        # if login_enter.get() in users and \
        #     users[login_enter.get()] == password.get():
        #     messagebox.showinfo('Welcome', 'Welcome to app')
        # else:
        #     messagebox.showerror('Error', 'Invalid login or password')
# #------------------------------- Functions--------------------------------

app = Tk()
app.title('Login Form')
app.geometry(f'{HEIGHT}x{WIDTH}')
app.resizable(FALSE, NO)
app.config(bg='white')




C = Canvas(app, height=HEIGHT, width=WIDTH)
background_image= PhotoImage(file='./image.png')
background_label = Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


app.option_add('*Font', 'Verdana')
app.option_add('*Background', 'white')

signup_button = Button(text='SIGN UP',fg='white', bg='#E50914', command=registration)
signup_button.place(relx=0.2, rely=0.1, relwidth=0.3)

signin_button = Button(text='SIGN IN',fg='white', bg='#E50914', command=login_form)
signin_button.place(relx=0.5, rely=0.1, relwidth=0.3)

app.mainloop()
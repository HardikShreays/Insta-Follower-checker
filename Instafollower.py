from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import instaloader
from PIL import ImageTk, Image

old_follower = open('Old_Follower.db','r')
old_following = open('Old_Following.db','r')

profile = None
follower_list = open('Follower.db','w')
following_list = open('Following.db','w')


def dont_follow():
    tk = Tk()
    top = Listbox(tk)
    followinglist = []
    res = []
    for i in profile.get_followers():
        i = str(i)
        i = i.split(' ')[1]
        followinglist.append(i)
    for j in profile.get_followees():
        j = str(j)
        j = j.split(' ')[1]
        if j not in followinglist:
            # print(j)
            res.append(j)
    # print(res)
    for m in res:
        top.insert(0, m)
    top.pack()
    tk.mainloop()


def recently_unfollowed():
    tk = Tk()
    res = []
    for val, followers in enumerate(profile.get_followers()):
        followers = str(followers)
        followers = followers.split(' ')[1]
        # following_list.write(followers + '\n')
        if followers not in old_follower.readlines():
            res.append(followers)
    top = Listbox(tk)
    l = lambda x: top.insert(0, x)
    map(l, res)
    top.pack()
    tk.mainloop()


def get_following():
    tk = Tk()
    top = Listbox(tk)
    for val, followees in enumerate(profile.get_followees()):
        followees = str(followees)
        followees = followees.split(' ')[1]
        # following_list.write(followees + '\n')
        top.insert(val, f'{val + 1}. {followees}')
    top.pack()
    top.mainloop()


def get_followers():
    tk = Tk()
    top = Listbox(tk)
    for val, follower in enumerate(profile.get_followers()):
        follower = str(follower)
        follower = follower.split(' ')[1]
        # follower_list.write(follower + '\n')
        top.insert(val,f'{val+1}. {follower}')
    top.pack()
    top.mainloop()



def main():
    win = Tk()
    win.iconbitmap('logo.ico')
    win.title('Login window')
    win.config(bg='#F9741E')
    win.geometry('200x200')
    win.maxsize(200, 200)
    win.minsize(200, 200)
    Button(win, command=get_followers, text='Get Followers').place(x=10, y=0)
    Button(win, command=get_following, text='Get Following').place(x=10, y=30)
    Button(win, command=recently_unfollowed, text='Who Recently Unfollowed').place(x=10, y=60)
    Button(win, command=dont_follow, text='Doesn\'t Follow You' ).place(x=10, y=90)
    win.mainloop()



def get_value():
    global profile
    username = en1.get()
    password = en2.get()
    L = instaloader.Instaloader()
    try:
        L.login(username, password)
        profile = instaloader.Profile.from_username(L.context, username)
        root.destroy()
        main()
    except Exception as E:
        messagebox.showerror("Error", str(E))

    #todo:add command GUI


root = Tk()
img = ImageTk.PhotoImage(Image.open("download.jpg"))

canvas = Canvas(root, width=230, height=220)
canvas.place(x=225, y=10)
canvas.create_image(5, 5, anchor=NW, image=img)
root.iconbitmap('logo.ico')
root.title('Follow Checker')
root.config(bg='#F9741E')
root.geometry('600x400')
root.maxsize(600, 400)
root.minsize(600, 400)
en1 = StringVar()
en2 = StringVar()
Label(root, text="Username: ").place(x=225, y=270)
Label(root, text="Password: ").place(x=225, y=300)
Entry(root, textvariable=en1, font="lucica 11 bold").place(x=300, y=270)
Entry(root, textvariable=en2, font="lucica 11 bold", show="*").place(x=300, y=300)
Button(root, command=get_value, text='Log In').place(x=350, y=350)
root.mainloop()


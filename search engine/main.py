import tkinter as tk
import webbrowser

root = tk.Tk()
root.title("search station")
root.geometry("400x150")
x = tk.StringVar()
def fb():
    word = x.get()
    webbrowser.open_new("https://www.facebook.com/search/top/?q"+word)
def yt():
    word = x.get()
    webbrowser.open_new("https://www.youtube.com/results?search_query="+word)
def ig():
    word = x.get()
    webbrowser.open_new("https://www.instagram.com/explore/search/keyword/?q"+word)
def tw():
    word = x.get()
    webbrowser.open_new("https://twitter.com/search?q="+word)
def search():
    word = x.get()
    search = ("https://www.google.com/search?q="+word)
    webbrowser.open_new(search)
x = tk.StringVar()
b1= tk.Button(root,text="Facebook",fg="white",bg="#3b5998",command=fb)
b2= tk.Button(root, text="Youtube",fg="White",bg="#FF0000",command=yt)
b3=tk.Button(root,text="Instagram",fg="White",bg="#C13584",command=ig)
b4=tk.Button(root,text="twitter",fg="White",bg="#013220",command=tw)
b5=tk.Button(root,text="Search",fg="White",bg="#282828",command=search)

b1.place(x=10,y=70,height=30,width=128)
b2.place(x=148,y=70,height=30,width=120)
b3.place(x=270,y=70,height=30,width=120)
b4.place(x=40,y=105,height=30,width=320)
b5.place(x=320,y=10,height=50,width=70)
e1 = tk.Entry(root,textvariable=x)
e1.place(x=10,y=10,width=300,height=50)
root.mainloop()



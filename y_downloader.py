import tkinter as tk
from pytube import YouTube
def genstream():
    link = inputxt.get(1.0, "end-1c")    # here we will get an input 
    lbl3.config(text="provided input is:"+link)
    choice=clicked.get()
    print(options[choice])
    print(type(options[choice]))
    strm=options[choice]      # here we got which stream we have to down load .
    
    youtube1=YouTube(link)
    print(youtube1.title)
    videos=youtube1.streams.all()
    vid=list(enumerate(videos))# it will craete a dictionary type of object which is easy to show 
    lb4.config(text="downloading.."+youtube1.title)
    videos[strm].download()
    print("download sucessfull")
    lb5.config(text="download successfull")
    
    
    
    
    
    
frame=tk.Tk()
frame.title("Youtube downloader")
frame.geometry("500x500")
lb1=tk.Label(frame,text="Well come to youtube downloader",font=("Times New Roman",30,"bold"),fg="green",bg="black")
lb1.place(x=30,y=50)
lb2=tk.Label(frame,text="put the url",font=( "Times New Roman",15,"italic"),fg="red",bg="black")
lb2.place(x=90,y=150)
inputxt=tk.Text(frame,width=30,height=5)
inputxt.place(x=100,y=200)
#creating the option maenu
# Dropdown menu options
options = {"144p mp4":0,
    "360p mp4":1,
    "480p mp4":7,
    "720p mp4":2,
    "1080p mp4":3,
    "1080 webm":4,
    "720 webm":6,
    "480p webm":8}
    

#setting the data type

clicked =tk.StringVar(frame)
#setting the default value to the drop down
clicked.set("vid quality")
#creating the drop down
drop=tk.OptionMenu(frame,clicked,*options)
drop.place(x=100,y=300)


btn=tk.Button(frame,text="Enter Link",bg="black",fg="red",command=genstream)
btn.place(x=150,y=330)

lbl3=tk.Label(frame,text="",bg="White",fg="Blue")
lbl3.place(x=100,y=400)
lb4=tk.Label(frame,text="")
lb4.place(x=100,y=430)
lb5=tk.Label(frame,text="")
lb5.place(x=100,y=460)

frame.mainloop()
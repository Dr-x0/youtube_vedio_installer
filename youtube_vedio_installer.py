from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter import ttk

root=Tk()
root.geometry("800x400")
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")
Label(root,text="youtube video downloader",font='arial 20 bold').pack()

link=StringVar()
Label(root,text='Paste Link Here:',font='arial 15 bold').place(x=160,y=60)
Entry(root,width=70,textvariable=link).place(x=32,y=90)
folder_l=Entry(root,width=70).place(x=32,y=170)
def brwose():

    director=filedialog.askdirectory(title="save video")
    folder_l.delete(0,"end")
    folder_l.insert(0,director)
browse=Button(root,text="Browse",height=10,command=brwose ).place(x=450,y=160)

#
def Downloader():
    url=YouTube(str(link.get()))
    video=url.streams.filter(progressive=True,file_extension="mp4").order_by("resolution").desc().first()
    folder=folder_l.get()
    video.download(folder)
    Label(root,text='DOWNLOADED',font="arial 15 bold",).place(x=190,y=260)

Button(root,text="DOWNLOAD",font="arial 20 bold",bg='pale violet red', padx = 2, command = Downloader).place(x=150 ,y = 230)

folder_label=Label(root,text="downlod folder ",font='arial 15 bold').place(x=160,y=140)

########________________________________________________________________________________________________________________

#_______________________________________________________________________________    




#folder_label=Label(root,text="downlod folder ",font='arial 15 bold').place(x=160,y=130)

##################################################################################

########________________________________________________________________________________________________________________
root.mainloop()
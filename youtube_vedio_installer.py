from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.geometry("800x400")
root.resizable(0, 0)
root.title("DataFlair-youtube downloader")
Label(root, text="YouTube Video Downloader", font='arial 20 bold').pack()

link = StringVar()
Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
Entry(root, width=70, textvariable=link).place(x=32, y=90)

folder_l = Entry(root, width=70)
folder_l.place(x=32, y=170)

def browse():
    director = filedialog.askdirectory(title="Select Folder to Save Video/Audio")
    folder_l.delete(0, "end")
    folder_l.insert(0, director)

Button(root, text="Browse", height=2, command=browse).place(x=450, y=160)

# ComboBox to select format
format_choice = ttk.Combobox(root, values=["MP4", "MP3"], state="readonly")
format_choice.place(x=150, y=120)
format_choice.set("MP4")  # Default to MP4

def downloader():
    try:
        url = YouTube(str(link.get()))
        format_selected = format_choice.get()
        folder = folder_l.get()

        if folder == '':
            messagebox.showerror("Error", "Please select a folder to save the file")
            return

        if format_selected == "MP4":
            video = url.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
            video.download(folder)
            messagebox.showinfo("Success", "Video Downloaded Successfully!")
        elif format_selected == "MP3":
            audio = url.streams.filter(only_audio=True).first()
            audio.download(folder)
            messagebox.showinfo("Success", "Audio Downloaded Successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

Button(root, text="DOWNLOAD", font="arial 20 bold", bg='pale violet red', padx=2, command=downloader).place(x=150, y=230)

folder_label = Label(root, text="Download Folder", font='arial 15 bold').place(x=160, y=140)

root.mainloop()

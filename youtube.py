from tkinter import *
import pytube


# Functions
def download():
    video_url = url.get()
    try:
        youtube = pytube.Youtube(video_url)
        video = youtube.streams.first()
        video.download(r'C:\Users\90551\Desktop')
        notif.config(fg="green", text="Video donloaded succesufully")
    except Exception as e:
        print(e)
        notif.config(fg="red", text="Video could not be downloaded")


# Main screen
master = Tk()
master.title("Youtube video downlaoder")

# Labels

Label(master, text="Youtube mp4 converter", fg="red", font=("Bangers", 15)).grid(sticky=N, padx=100, row=0)
Label(master, text="Please enter URL for your video below: ", font=("Calibri", 15)).grid(sticky=N, padx=100, row=1,
                                                                                         pady=15)
notif = Label(master, font=("Calibri", 12))
notif.grid(sticky=N, pady=1, row=4)
# Vars
url = StringVar()
# Entry
Entry(master, width=50, textvariable=url).grid(sticky=N, row=2)
Button(master, width=20, text="Download", font=("Arial", 12), command=download).grid(sticky=N, row=3, pady=15)
master.mainloop()

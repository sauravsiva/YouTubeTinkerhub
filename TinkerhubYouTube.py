import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

#Tkinter widgets
def Widgets():

	head_label = Label(root, text="YouTube Video Downloader",
					padx=15,
					pady=15,
					font="SegoeUI 14",
					bg="#000000",
					fg="red")
	head_label.grid(row=1,
					column=1,
					pady=10,
					padx=5,
					columnspan=3)

	link_label = Label(root,
					text="YouTube link :",
					bg="#7F00FF",
                    relief=GROOVE,
					pady=5,
					padx=5)
	link_label.grid(row=2,
					column=0,
					pady=5,
					padx=5)

	root.linkText = Entry(root,
						width=35,
						textvariable=video_Link,
						bg="#36454F",
						fg="#FFFFFF",
						font="Arial 14")
	root.linkText.grid(row=2,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)


	destination_label = Label(root,
							text="Destination :",
							bg="#7F00FF",
							pady=5,
							padx=9,
							relief=GROOVE)
	destination_label.grid(row=3,
						column=0,
						pady=5,
						padx=5)


	root.destinationText = Entry(root,
								width=27,
								textvariable=download_Path,
								bg="#36454F",
								fg="#FFFFFF",
								font="Arial 14")
	root.destinationText.grid(row=3,
							column=1,
							pady=5,
							padx=5)


	browse_B = Button(root,
					text="Browse",
					command=Browse,
					width=10,
					bg="#71797E",
					relief=GROOVE)
	browse_B.grid(row=3,
				column=2,
				pady=1,
				padx=1)

	Download_B = Button(root,
						text="Download Video",
						command=Download,
						width=20,
						bg="#FF5F1F",
						pady=10,
						padx=15,
						relief=RAISED,
						font="Georgia, 13")

	Download_B.grid(row=4,
					column=1,
					pady=20,
					padx=20)


# Defining Browse() to select a destination folder to save the video

def Browse():
	download_Directory = filedialog.askdirectory(
		initialdir="YOUR DIRECTORY PATH", title="Save Video")

	download_Path.set(download_Directory)

# Defining Download() to download the video
def Download():

	# getting user-input Youtube Link
	Youtube_link = video_Link.get()
	
	# Select the optimal location for saving the downloaded file 
	download_Folder = download_Path.get()
	getVideo = YouTube(Youtube_link)

	# Getting all the available streams of the youtube video and selecting the highest resolution video 
	videoStream = getVideo.streams.get_highest_resolution()

	# Downloading the video to destination directory
	videoStream.download(download_Folder)

	# Displaying the message
	messagebox.showinfo("SUCCESSFULLY",
						"DOWNLOADED AND SAVED IN\n"
						+ download_Folder)

root = tk.Tk()

# Setting the title, background color and size of the tkinter window and disabling the resizing property
root.geometry("520x280")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="#000000")

# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()

Widgets()
root.mainloop()
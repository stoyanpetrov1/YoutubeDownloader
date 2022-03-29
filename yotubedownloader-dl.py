from __future__ import unicode_literals
import tkinter as tk
from yt_dlp import YoutubeDL


def download_audio():
    url = link.get()
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'DownloadedAudio/%(extractor_key)s/%(title)s.%(ext)s',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_video():
    url = videolink.get()
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'outtmpl': 'DownloadedVideo/%(extractor_key)s/%(title)s.%(ext)s',
        'noplaylist': True,
        }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


window = tk.Tk()
window.iconbitmap('youtube-icon-png-black-6.ico')
window.geometry("800x500")
window.config(bg="#F29075")
window.resizable(width=True, height=True)
window.title('YouTube MP3 Downloader')

link = tk.StringVar()
download_Path = tk.StringVar()
videolink = tk.StringVar()

tk.Label(window, text='Youtube Audio Downloader', font='roboto 20 bold', bg="#F29075").pack()
tk.Label(window, text='↓Paste Your YouTube Audio Link Here↓', font='roboto 20 bold', bg="#F29075").pack()
tk.Label(window, text='', font='roboto 5 ', bg="#F29075").pack()
tk.Entry(window, width=100, textvariable=link, font='roboto 15 bold', bg="#F7F7FF").pack()
tk.Label(window, text='', font='roboto 3 ', bg="#F29075").pack()
tk.Button(window, text='Download Audio', font='roboto 15 bold', fg="white", bg='#212121', padx=10,
          command=download_audio).pack()


tk.Label(window, text='', font='roboto 5 ', bg="#F29075").pack()
tk.Label(window, text='↓Paste Your YouTube Video Link Here↓', font='roboto 20 bold', bg="#F29075").pack()
tk.Entry(window, width=100, textvariable=videolink, font='roboto 15 bold', bg="#F7F7FF").pack()
tk.Button(window, text="Download Video", command=download_video, font='roboto 15 bold', fg="white", bg='#212121',
          padx=10).pack()

window.mainloop()

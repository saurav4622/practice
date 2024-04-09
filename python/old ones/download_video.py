from pytube import youtube
link=input("enter your URL here: ")
video=youtube(link)
stream=video.streams.get_highest_resolution()
stream.download()
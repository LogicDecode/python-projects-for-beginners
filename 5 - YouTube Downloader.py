# Import required modules
from pytube import YouTube
from pytube import cli

# Welcome message
print("\n\nWelcome to YouTube Downloader!")

# Get the URL from the user
url = input("Enter the YouTube URL: ")

file_size = 0


def progress_Check(stream=None, chunk=None, remaining=None):
    cli.display_progress_bar(file_size-remaining, file_size)


def on_download_finished(stream=None, file_handle=None):
    print("\n\nDownload Complete!")


# Initialize the YouTube class
yt = YouTube(url)
yt.register_on_progress_callback(progress_Check)
yt.register_on_complete_callback(on_download_finished)

# Print video metadata
print("\n\n-------------------\n\n")
print("Title: ", yt.title)
print("\n\n-------------------\n\n")
print("Description: ", yt.description)
print("\n\n-------------------\n\n")
print("Views: ", yt.views)
print("\n\n-------------------\n\n")
print("Duration: ", yt.length, "seconds")
print("\n\n-------------------\n\n")
print("Thumbnail URL: ", yt.thumbnail_url)
print("\n\n-------------------\n\n")
print("Keywords", *yt.keywords, sep="\n- ")
print("\n\n-------------------\n\n")

# Print All Streams
print("All Streams: ", *yt.streams, sep="\n- ")
print("\n\n-------------------\n\n")

# Get only the audio stream
print("Audio Streams: ", *yt.streams.filter(only_audio=True), sep="\n- ")
print("\n\n-------------------\n\n")

# Get only the video stream
print("Video Streams: ", *yt.streams.filter(only_video=True), sep="\n- ")
print("\n\n-------------------\n\n")

# Get progressive streams
print("Progressive Streams: ", *yt.streams.filter(progressive=True), sep="\n- ")
print("\n\n-------------------\n\n")

# Get highest resolution stream
yt_highest = yt.streams.get_highest_resolution()

# Get specific stream
# stream = yt.streams.get_by_itag(18)

# Download the video
# yt_highest.download()

# Download the video to a specific directory
file_size = yt_highest.filesize
print("Downloading: ", yt_highest.title)
yt_highest.download("youtube")

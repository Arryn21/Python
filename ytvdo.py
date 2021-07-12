from pytube import YouTube

url = "https://youtu.be/BV9t3Cp18Rc"

my_v = YouTube(url)

print("Title:")

print(my_v.title)

print("Thumbnail")

print(my_v.thumbnail_url)

# for stream in my_v.streams:
#     print(stream)

my_v = my_v.streams.get_highest_resolution()

my_v.download()

import pytube

url = input("Url video:")

path="C:"

pytube.YouTube(url).streams.get_highest_resolution().download(path)


            
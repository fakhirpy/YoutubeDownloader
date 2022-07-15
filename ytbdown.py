import pytube

url = input("Url video:")

# to use in termux or linux and the directory is not "C:" change to the desired location.
path="C:"

pytube.YouTube(url).streams.get_highest_resolution().download(path)


            

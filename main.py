import requests
from PIL import Image

user = input("Enter minecraft username: ")
url = "https://minotar.net/skin/" + user
response = requests.get(url, stream=True)
img = Image.open(response.raw)
img.save("output/" + user + ".png")
print(user + "'s skin has been downloaded to the output folder!")

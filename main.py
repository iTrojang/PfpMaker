import requests
from PIL import Image,ImageFilter
from PIL import ImageFilter
from PIL import ImageDraw

h = 700
w = 700

name = input("What Name? ")
color = input("What Color Should the back ground be? ")
busthead = input("Bust OR head: ")

r = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
rdata = r.json()
uuid = rdata["id"]
names = rdata["name"]
req = requests.get(f"https://visage.surgeplay.com/{busthead}/512/{uuid}")
with open("face.png","wb") as f:
    f.write(req.content)

img = Image.open("face.png")
res = img.convert("RGB")
pink = 255,192,203
width = res.size[0]
height = res.size[1]
for x in range(0,width):
    for y in range(0,height):
        data = res.getpixel((x, y))
        if color == "pink":
            if (data[0] == 0 and data[1] == 0 and data[2] == 0 ):
                res.putpixel((x, y), (255,192,203))
        elif color == "red":
            if (data[0] == 0 and data[1] == 0 and data[2] == 0 ):
                res.putpixel((x, y), (255,0,0))
        elif color == "blue":
            if (data[0] == 0 and data[1] == 0 and data[2] == 0 ):
                res.putpixel((x, y), (173,216,230))


font = ImageDraw.ImageFont.truetype("Reglisse-0WOD9.otf",size=100)
d = ImageDraw.Draw(res)
d.text((88,451),text=names,font=font)
res.save("Finish.png")

imgfil = Image.open("Finish.png")
img3 = imgfil.filter(ImageFilter.SHARPEN)

img3.save("Finish.png")

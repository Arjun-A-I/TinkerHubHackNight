import tweepy
import config
from PIL import Image,ImageDraw,ImageFont

img = Image.open('a.jpg')
d = ImageDraw.Draw(img)
fnt=ImageFont.truetype("comicbd.ttf",10)


idd=int(input("Enter Tweet ID==>"))
client=tweepy.Client(bearer_token=config.bearer_token)
response=client.get_tweet(id=idd)
for i in response[:1]:
    x=str(i)

d.text((10,10),x, font= fnt, fill=(255,255,255))
img.show()
print(i)
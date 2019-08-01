import tweepy
from colour import Color
from PIL import Image, ImageDraw
from random import randint as rint
from creds import *


# Authenticate to Twitter

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def random_gradient(name):
    size = 500
    img = Image.new("RGB", (size,size), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    r, g, b = rint(0, 255), rint(0, 255), rint(0, 255)
    dr = (rint(0, 255) - r) / 500.
    dg = (rint(0, 255) - r) / 500.
    db = (rint(0, 255) - r) / 500.

    for i in range(size):
        r, g, b = r + dr, g + dg, b + db
        draw.line((i, 0, i, size), fill = (int(r), int(g), int(b)))

    img.save(name+".png", "PNG")


# for name in range(10):
name = rint(0, 1000)
random_gradient(str(name))


# api.update_status("Test Tweet")
filename = str(name) + ".png"
api.update_with_media(filename)

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication.")

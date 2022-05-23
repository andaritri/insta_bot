from instapy import InstaPy
import os


username = os.environ.get('INSTA_USER')
password = os.environ.get("PASSWORD")


session = InstaPy(username=username, password=password)
session.login()

followings = session.grab_following('portuguesewithlucilene')
print(followings)

session.end()

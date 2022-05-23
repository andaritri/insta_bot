from instapy import InstaPy
import os


username = os.environ.get('INSTA_USER')
password = os.environ.get("PASSWORD")


session = InstaPy(username=username, password=password, headless_browser=True)
session.login()

followings = session.grab_following(username='portuguesewithlucilene', amount=2000)
print(followings)

session.end()

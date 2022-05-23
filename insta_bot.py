from instapy import InstaPy
import os


username = os.environ.get('INSTA_USER')
password = os.environ.get("PASSWORD")


session = InstaPy(username=username, password=password, headless_browser=True)
session.login()

followers = session.grab_followers(username='la_liendraa', amount=100, store_locally=False)

print("----->>>", followers)

session.end()

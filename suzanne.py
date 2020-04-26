
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

#your login credentials
insta_username='suzanneabele'
insta_password='Ffj6tj12'

#path to your workspace
set_workspace(path=None)

def job():
  session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
  with smart_run(session):
    session.set_do_comment(enabled=True, percentage=60)
    session.set_comments(['🔥', 'Great picture!'])
    session.set_do_follow(enabled=True, percentage=40, times=100)
    session.like_by_tags(['#travel', 'fashion', 'food'], amount=100, media='Photo')


job()
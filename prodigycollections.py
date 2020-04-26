
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

#your login credentials
insta_username='prodigycollections'
insta_password='Charlieboy11'

#path to your workspace
set_workspace(path=None)

def job():
  session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
  with smart_run(session):
    session.set_do_comment(enabled=True, percentage=60)
    session.set_comments(['🔥', 'Great picture!', "Love this! Dm for clothing business opportunity!"])
    session.like_by_tags(['fitness'], amount=100, media='Photo')


job()
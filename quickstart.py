from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

#your login credentials
insta_username='neededmemes'
insta_password='J0nnyb0y123!'

#path to your workspace
set_workspace(path=None)

def job():
  session = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
  with smart_run(session):
    session.set_do_comment(enabled=True, percentage=60)
    session.set_comments(['hey if you need an app built or any programming done let me know:)', 'Hey I built a bot for instagram that mines likes and followers let me know if you want to try it!', 'Hey love your posts definitely consider hiring me on upwork if you need any marketing/programming help! Would love to help you. http://bit.ly/2S3Gvr2'])
    session.set_do_like(enabled=True, percentage=100)
    session.like_by_tags(['startups'], amount=100, media='Photo')


job()
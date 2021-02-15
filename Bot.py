from time import sleep
from requests import post


class Bot:


    def __init__(self,users,comments,session_id,login_secure):
        self.users = users
        self.comments = comments
        data = {"comment": comments, "sessionid": session_id, "feature2": -1}
        cookies = {"sessionid": session_id, "steamLoginSecure": login_secure}

        print('Starting...')
        for c in comments:
            self.post_comments(users,c,data,cookies)


    def post_comments(self,users,comment,data,cookies):
        for u in users:
            resp = post(f"https://steamcommunity.com/comment/Profile/post/"+u+"/-1", data=data, cookies=cookies)
            print(resp.json())
            sleep(15)

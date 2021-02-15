from time import sleep
from requests import post
from Bot import Bot


'''
    How to get
        user_id         --> Go to https://steamidfinder.com/
        session_id      --> Go to steam in your browser, INSPECT the page, find session_id var
        login_secure    --> Go to browser cookies, find steam cookie and get login_secure

'''

users = ['USER_ID']
comments = ['comment']
session_id = 'SESSION_ID'
login_secure = 'LOGIN_SECURE'

steam_bot = Bot(users,comments,session_id,login_secure)

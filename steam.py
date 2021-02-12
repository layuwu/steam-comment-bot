from time import sleep
import toml
from colorama import Style, Fore
from requests import post
from tqdm import tqdm, trange

#config = open("config.txt",'r')
#comentarios = open("comentarios.txt",'r')
login_secure = "LOGIN SECURE AQUI"
session_id = "ID AQUI"
sleeptime = 15

#Usuario que recebera os comentarios
usuario = ['ID DO USUARIO AQUI']

comentario = 'Seu comentario aqui!'

data = {"comment": comentario, "sessionid": session_id, "feature2": -1}
cookies = {"sessionid": session_id, "steamLoginSecure": login_secure}

for c in comentario:
    data = {"comment": c, "sessionid": session_id, "feature2": -1}
    cookies = {"sessionid": session_id, "steamLoginSecure": login_secure}
    resp = post(f"https://steamcommunity.com/comment/Profile/post/{0}/-1", data=data, cookies=cookies).format(usuario)
    print(resp.json())
    
    
    
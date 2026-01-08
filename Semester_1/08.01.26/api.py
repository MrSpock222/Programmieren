from requests import *
import random

url ="https://chat.johanneskoch.dev/"

r = post(url + "register", json={"username" : "testuser"})
print(r.text)
user_id = r.json()["userId"]

c = get(url + "message/colors")
print(c.text)

colors = c.json()["supportedColors"]
color = random.choice(colors)

m = post(url + "message", json={"from" : user_id, "color": color, "message": "test3" })
print(m.text)
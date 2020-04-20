import os
import random
import webbrowser
import getpass

name = input("What Show do you want to watch?")

url = "/media/" + getpass.getuser() +"/NAME OF DRIVE/" + name + "/"

list = []
for root, dirs, files in os.walk(url, topdown=False):
   for name in files:
      show = (os.path.join(root, name))
      list.append(os.path.join(root, name))



show = str(random.choice(list))

print(show)

webbrowser.open(show)

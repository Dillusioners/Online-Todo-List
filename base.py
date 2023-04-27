import requests
import json


def register():
  name = input("Please enter your name: ")
  password = input("Please enter your password: ")
  if len(password) < 8:
    print("Password must be at least 8 characters long. \n \n")
    register()
  else:
    url = "https://FreeDB.pythonanywhere.com/add_user?username=" + name + "&password=" + password
    URL = requests.get(url)
    print("Successfully registered ", name, "!")
    

  return name, password

def login():
  name = input("Please enter your name:")
  password = input("Please enter your password: ")
  data = requests.get("https://FreeDB.pythonanywhere.com/get_user")
  data = data.json()['USERS']
  FOUND = False
  state = False
  for i in range(0, len(data)):
    if data[i]["username"] == name:
      if data[i]["password"] == password:
        print("Logged in user successfully!")
        FOUND = True
        state = True
        break
      else:
        print("Wrong username or password!")
        FOUND = True
    else:
      FOUND = False

  if FOUND == False:
    print("User not found!")
  
  return name, password, state


def save_task(username):
  delete_url = "https://FreeDB.pythonanywhere.com/delete_todo?username="+username
  DELETE_URL = requests.get(delete_url)
  
  f = open("Tasks.json")
  url = "https://FreeDB.pythonanywhere.com/add_todo?"
  data = json.load(f)
  data['username'] = username
  for i in data:
    url = url + str(i) + "=" + str(data[i]) + "&"
  f.close()

  url = url[:-1]

  URL = requests.get(url)
  print("SAVED TASK TO DATABASE!")

def get_task(username):
  url = "https://FreeDB.pythonanywhere.com/get_todo"
  data = requests.get(url)
  data = data.json()['TODOS']
  FOUND = False
  for i in range(0, len(data)):
    if data[i]["username"] == username:
      try:
        json_file = open('Tasks.json','w')
        data[i].pop("username", None)
        json.dump(data[i], json_file)
        json_file.close()
        print("Retrived data from user's database successfully!")
        FOUND = True
        break
      except:
        print("\n \n ERROR RETRIVING DATA! \n \n")

  if FOUND == False:
    print("User not found!")

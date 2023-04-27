import json
import os
import time
import base



def display_and_input():
  while True:
    print("")
    print("TODO™ LIST MANAGER")
    print("1. View list")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")
    try:
      choice = int(input(">> What do you want to do? : "))
    except Exception as e:
      print(e)
    else:
      if choice == 1:
        viewList()
      elif choice == 2:
        task = input("\nEnter task to add: ")
        add_task(task)
      elif choice == 3:
        task_number = input("\nEnter task number to remove: ")
        remove_task( task_number)
      elif choice == 4:
        break
      else:
        print("Invalid choice.")

def createDirectory():
  with open('Tasks.json', 'w') as f:
    f.write("{}")
    print(">> [Console] : The json file is created")


def viewList():  #USED TO VIEW THE LIST
  print("\nTODO™ LIST:")
  with open('Tasks.json', 'r') as file:
    data = json.load(file) 
    if (len(data) == 0):
      print(">> No Tasks available. Add more to see.")
    else:
      for key, val in data.items():
        print(f"Task {key}: {val}")
        time.sleep(.5)


def add_task(task):
  data = {}
  try:
    with open('Tasks.json', 'r') as f:
      data = json.load(f)
    
    json_file = open('Tasks.json','w')
    taskIndex = len(data) + 1
    data[taskIndex] = task
    json.dump(data, json_file)
    json_file.close() 

  except json.decoder.JSONDecodeError:
    with open('Tasks.json', 'w') as o:
      o.write('{}')
      print(">> Could not add task, try again!")
      return 0
    
  print(">> Successfully Added task")


def remove_task(task_number):
    try:
      file = open('Tasks.json', 'r')
      data = json.load(file)
      file.close()
      counter = int(task_number)
      data2 = {} 
      del data[task_number]
      for key, value in data.items():
        if int(key) > counter:
          up_data = {str(int(key) - 1):value}
        else:
          up_data = {key:value}

        data2.update(up_data)
        
      data = data2
          
      with open('Tasks.json', 'w') as f:
        json.dump(data, f)

    except json.decoder.JSONDecodeError:
      with open('Tasks.json', 'w') as o:
        o.write('{}')
        print(" >> Couldnot remove task, try again!")

    except KeyError:
      print(">> Invalid key! Try again")
          
    else:
      print(">> Successfully Removed task")


def main():
  loggedIn = False
  username = ""
  password = ""
  while True:
    if not os.path.exists('Tasks.json'):
      createDirectory()
  
    print("")
    print("TODO™ LIST MANAGER")
    print("1. Login")
    print("2. Register")
    print("3. Logout")
    print("4. Save Data")
    try:
      choice = int(input(">> What do you want to do? : "))
    except Exception as e:
      print(e)
    else:
      if choice == 1:
        print(" ")
        username, password, loggedIn = base.login()
        base.get_task(username)
        if not loggedIn:
          main()
      elif choice == 2:
        print(" ")
        username, password = base.register()
        loggedIn = True
      elif choice == 3:
        print("LOGGED YOU OUT!")
        loggedIn = False
      elif choice == 4:
        if username == "":
          print("Log in First!")
        else:
          base.save_task(username)
      else:
          print("Invalid choice.")
    if loggedIn:
      display_and_input()


if __name__ == "__main__":
  main()

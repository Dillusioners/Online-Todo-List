import requests
import json


def register():
  name = input("Please enter your name: ")
  password = input("Please enter your password: ")
  if len(password) < 8:
    print("Password must be at least 8 characters long. \n \n")
    register()
import requests
import json


# Function to register a user
def register():
  # Get user input for name and password
  name = input("Please enter your name: ")
  password = input("Please enter your password: ")
  
  # Check password length and prompt user to re-enter if it's too short
  if len(password) < 8:
    print("Password must be at least 8 characters long. \n \n")
    register()
  else:
    # Create the registration URL
    url = "https://FreeDB.pythonanywhere.com/add_user?username=" + name + "&password=" + password
    URL = requests.get(url)
    print("Successfully registered ", name, "!")
    
  # Return the name and password
  return name, password


# Function to log in a user
def login():
  # Get user input for name and password
  name = input("Please enter your name:")
  password = input("Please enter your password: ")
  
  # Get the list of registered users from the database
  data = requests.get("https://FreeDB.pythonanywhere.com/get_user")
  data = data.json()['USERS']
  
  # Initialize variables for user matching and login state
  FOUND = False
  state = False
  
  # Iterate through the list of registered users and check if the input name and password match
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

  # Print a message if the user is not found in the database
  if FOUND == False:
    print("User not found!")
  
  # Return the name, password, and login state
  return name, password, state


# Function to save a task to the database
def save_task(username):
  # Delete any existing tasks for the user
  delete_url = "https://FreeDB.pythonanywhere.com/delete_todo?username="+username
  DELETE_URL = requests.get(delete_url)
  
  # Open the task data file
  f = open("Tasks.json")
  
  # Create the URL to add the task data to the database
  url = "https://FreeDB.pythonanywhere.com/add_todo?"
  
  # Load the task data from the file and add the username to the data dictionary
  data = json.load(f)
  data['username'] = username
  
  # Iterate through the task data and add each item to the URL as a parameter
  for i in data:
    url = url + str(i) + "=" + str(data[i]) + "&"
  f.close()

  # Remove the final "&" character from the URL
  url = url[:-1]

  # Add the task data to the database using the URL
  URL = requests.get(url)
  print("SAVED TASK TO DATABASE!")

# Function to get a task from the database
def get_task(username):
  # Create the URL to get the task data from the database
  url = "https://FreeDB.pythonanywhere.com/get_todo"
  
  # Get the task data from the database and extract the list of tasks
  data = requests.get(url)
  data = data.json()['TODOS']
  
  # Initialize variable for user matching
  FOUND = False
  
  # Iterate through the list of tasks and check if the username matches
  for i in range(0, len(data)):
    # Check if the user is found
    if data[i]["username"] == username:
      try:
        # Open the task data file
        json_file = open('Tasks.json','w')
        # Removing the username value
        data[i].pop("username", None)
        # Adding the retrived data to the task data file
        json.dump(data[i], json_file)
        json_file.close()
        print("Retrived data from user's database successfully!")
        # Prompting user match.
        FOUND = True
        break
      except:
        print("\n \n ERROR RETRIVING DATA! \n \n")

  if FOUND == False:
    print("User not found!")

import sys
import fileinput

def main():
  # Checking for input data table
  arguments_list = sys.argv[1:]
  if len(arguments_list) != 1:
    print("Please run the program providing one argument, which specifys the path to the mta data table.")
  else:
    try:
      pass
      #note fot rebasing idk
    except:
      pass

  # Starting program
  print("""
    Welcome to the subway program. \n
    To begin, try typing 'help' to see the list of valid commands. \n
    """)
  
  # Program loop
  user_input = str(input("Enter option: "))
  while user_input != "quit":
    if user_input == "help":
      print_help()
    else:
      print("Invalid option. Type 'help' to see the list of valid commands.")
    user_input = str(input("Enter option: "))



if "__main__" == __name__:
  main()

def print_help():
	print("""
  liststations - \n
	print a list of names of all subway stations \n
        listroutestations - lists the route of a specific train line (number or letter) \n
        listroutes - lists the train lines at a given station \n
        liststationportals - lists entrances/exits of a given station and if it has a elevator \n
        nearest - nearest <latitude> <longitude> would provide nearby stations and routes \n
        quit - """)

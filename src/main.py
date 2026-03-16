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
    user_input = str(input("Enter option: "))



if "__main__" == __name__:
  main()

def print_help():
	print("""
  liststations - \n
	listroutestations - \n
	listroutes - \n
	liststationportals - \n
	nearest - \n
	quit - """)

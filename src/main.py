
import sys
def main():
  # Checking for input data table
  args = sys.argv[1:]
  if len(args) != 1:
    print("Please run the program providing one argument, which specifys the path to the mta data table.")
  else:
    pass

  # Starting program
  print("""
    Welcome to the subway program. n \
    To begin, try typing 'help' to see the list of valid commands. 
    """)




if "__main__" == __name__:
  main()

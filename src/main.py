import sys
import fileinput

# Data types
class Station:
  name: str
  # Division,
  # Line,
  # Station Name,
  # Station Latitude,
  # Station Longitude,
  # Route1,Route2,Route3,Route4,Route5,Route6,Route7,Route8,Route9,Route10,Route11,
  # Entrance Type,
  # Entry,
  # Exit Only,
  # Vending,
  # Staffing,
  # Staff Hours,
  # ADA,
  # ADA Notes,
  # Free Crossover,
  # North South Street,
  # East West Street,
  # Corner,
  # Entrance Latitude,
  # Entrance Longitude,
  # Station Location,
  # Entrance Location
  def __init__(self, line):
    pass


def main():
  # Checking for input data table
  arguments_list = sys.argv[1:]
  if len(arguments_list) != 1:
    print("Please run the program providing one argument, which specifys the path to the mta data table.")
  else:
    file_path = arguments_list[1]
    station_data = initialize_data(file_path)

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

def initialize_data(file_path):
  try:
    f = open(file_path)
  except:
    print ("Error: file not found. Please check the file path and try again.")
  #ignore first line because that is the header
  station_dict = {}
  f.readline()
  #each line get the station name, and insert into array of stations storing station datatypes
  while(f.readable()):
    line = f.readline()
    #store each property
    #if the next entry is the same station, add exit to exit array and entrence to enterance array
    #if the next entry is different repeat initial process.
    #if end of file, break loop
    if line == "":
      break
  
  return station_dict



if "__main__" == __name__:
  main()

def print_help():
        print("""
  liststations - print a list of names of all subway stations \n
        listroutestations - lists the route of a specific train line (number or letter) \n
        listroutes - lists the train lines at a given station \n
        liststationportals - lists entrances/exits of a given station and if it has a elevator \n
        nearest - nearest <latitude> <longitude> would provide nearby stations and routes \n
        quit - """)

def list_stations(station_dict):
  # create a list for station names
  #for each item in statuion dict, add station name to list 
  #sort the list
  #print
  pass
  #DONE



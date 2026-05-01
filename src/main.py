"""
  MTA Subway Station Data Program
  Usage: main.py <path to mta data table>
  Description: 
    This program takes in a data table of mta subway stations and allows the user to query the data
    in various ways, such as listing all stations, listing stations on a specific train line, listing
    train lines at a specific station, listing entrances/exits of a specific station and accessibility,
    and finding nearby stations based on latitude and longitude. The program is designed to be
    user-friendly and provides helpful prompts for the user to navigate through the options.
  Authors: 
  Date: 4/20/2026
  Data Source: 
"""
import sys, duckdb, os, re

def print_help():
        print("""
  help - prints this help message
  liststations - print a list of names of all subway stations
  listroutestations - lists the route of a specific train line (number or letter)
  listroutes - lists the train lines at a given station
  liststationportals - lists entrances/exits of a given station and if it has a elevator
  nearest - nearest <latitude> <longitude> would provide nearby stations and routes
  quit - exits the program
  """)

def list_stations(station_dict):
  # create a list for station names
  #for each item in statuion dict, add station name to list 
  #sort the list
  #print
  pass
  #DONE

def list_route_stations(station_dict):
	# create a stations on a specific train line
	# for each station that has that train line, add station name to train station list
	# sort the list
	# print
	pass
	#Done

def list_routes(station_dict):
	# Lists train lines of a specific station
	# for each train line found at a station, add train line to the list
	# sort the list
	# print
	pass
	#done

def list_station_portals(station_name):
    # duckdb.query("""SELECT Entrance, Exit
    #                 WHERE Station Name == ?""", station_name)
	pass
	#Done

def nearest(station_dict):

	pass
	#Done 

def main():
  # Checking for input data table
  if len(sys.argv) < 1:
    print("""Error: No arguments were provided. Please provide the path to the mta data table as an argument.\nUsage: main.py <path to mta data table>""")
    exit(1)
  else:
    file_path = sys.argv[1]

  # Initialize duckdb  
  con = duckdb.connect()
  con.execute(f"""CREATE TABLE IF NOT EXISTS station_data AS SELECT * FROM read_csv_auto('{file_path}')""")

  # Starting program
  print("""
    Welcome to the subway program. \n
    To begin, try typing 'help' to see the list of valid commands. \n
    To exit, type 'quit'.
    """)
  
  # Program loop
  user_input = str(input("Enter option: "))
  while user_input != "quit":
    if user_input == "help":
      print_help()
    elif user_input == "liststations":
      list_stations()
    elif user_input == "listroutestations":
      list_route_stations()
    elif user_input == "^listroutes\s+(.+)$":
      
      list_routes(input)
    else:
      print("Invalid option. Type 'help' to see the list of valid commands.")
    user_input = str(input("Enter option: "))

if "__main__" == __name__:
  main()
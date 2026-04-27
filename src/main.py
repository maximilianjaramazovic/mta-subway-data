#!/usr/bin/env python3
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
import sys, csv, sqlite3

def main():
  # Checking for input data table
  arguments_list = sys.argv[1:]
  if len(arguments_list) != 1:
    print("""Error: No arguments were provided. Please provide the path to the mta data table as an argument.\nUsage: main.py <path to mta data table>""")
    exit(1)
  else:
    file_path = arguments_list[1]
    initialize_db(file_path)


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

def initialize_db(file_path):
  with sqlite3.connect('mta.db') as con:
    cur = con.cursor()
    with open(file_path, mode="r") as f:
        reader = csv.reader(f)
        reader.__next__() # skipping header
        data = list(reader)

    # Bulk insterting data into the database
    cur.executemany("INSERT INTO stations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?", data)


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

def list_route_stations():
	# create a stations on a specific train line
	# for each station that has that train line, add station name to train station list
	# sort the list
	# print
    #Get Train Route from User
    route = input("Enter the train line (e.g., N, R, M, 1): ").strip().upper()
    #Connecting Database created in initialize_db
    with sqlite3.connect('mta.db') as con:
        cur = con.curser()

        #Use of % since a station may serve many routes
        #This looks for route anywhere in the 'route' column
        query = "Select Distinct station_name FROM stations WHERE routes like ?"
        cur.execute(query, (f'%{route}%',))

        #Taking name and sorting
        stations = [row[0] for row in cur.fetchall()]
        stations.sort()

    #Print results
    if stations: 
        print(f"\nStations on the {route} line:")
        for station in stations:
            print(f"- {stations}")
    else:
        print(f"No stations found for line {route}.")
	#Done

def list_routes(station_dict):
	# Lists train lines of a specific station
	# for each train line found at a station, add train line to the list
	# sort the list
	# print
	pass
	#done

def list_station_portals(station_dict):
	# Lists the entrances/exits of a specific station and accessibility
	# For each station find all entrances/exits, add to the list
	# Print
	pass
	#Done

def nearest(station_dict):
	# Uses specific latitude and longitude to find nearest station to user's location
	# For all stations near the area, add to the list
	# Print
	pass
	#Done 


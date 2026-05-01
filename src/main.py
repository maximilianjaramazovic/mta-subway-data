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
import sys, duckdb

def print_help():
    print("""
    liststations - print a list of names of all subway stations \n
    listroutestations - lists the route of a specific train line (number or letter) \n
    listroutes - lists the train lines at a given station \n
    liststationportals - lists entrances/exits of a given station and if it has a elevator \n
    nearest - nearest <latitude> <longitude> would provide nearby stations and routes \n
    quit - """ )

def list_stations(station_dict):
  # create a list for station names
  #for each item in statuion dict, add station name to list 
  #sort the list
  #print
  pass
  #DONE

def list_route_stations(connection: duckdb.DuckDBPyConnection):
	# create a stations on a specific train line
	# for each station that has that train line, add station name to train station list
	# sort the list
	# print
    #Get Train Route from User
    route = input("Enter the train line (e.g., N, R, M, 1): ").strip().upper()
    #Connecting Database created in initialize_db

    #Use of % since a station may serve many routes
    #This looks for route anywhere in the 'route' column
    query = f"""
      Select Distinct stop_name 
      FROM stops
      WHERE daytime_routes like ?
      """
    connection.execute(query, (f'%{route}%',))

    #Taking name and sorting
    stations = [row[0] for row in connection.fetchall()]
    stations.sort()

    #Print results
    if stations: 
        print(f"\nStations on the {route} line:")
        for station in stations:
            print(f"- {station}")
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
  con.execute("""
    CREATE TABLE stops (
      gtfs_stop_id VARCHAR(3),
      station_id INTEGER,
      complex_id INTEGER,
      division VARCHAR,
      line VARCHAR,
      stop_name VARCHAR,
      borough VARCHAR,
      cbd BOOLEAN,
      daytime_routes VARCHAR,
      structure VARCHAR,
      gtfs_latitude DOUBLE,
      gtfs_longitude DOUBLE,
      north_direction_label VARCHAR,
      south_direction_label VARCHAR,
      ada INTEGER,
      ada_northbound INTEGER,
      ada_southbound INTEGER,
      ada_notes VARCHAR,
      georeference VARCHAR
    );
  """)

  con.execute(f"""
    COPY stops 
    FROM '{file_path}' (AUTO_DETECT TRUE);
  """)

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
      list_route_stations(con)
    elif user_input == "^listroutes\s+(.+)$":
      
      list_routes(input)
    else:
      print("Invalid option. Type 'help' to see the list of valid commands.")
    user_input = str(input("Enter option: "))

if "__main__" == __name__:
  main()

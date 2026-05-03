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
import sys, duckdb, re

def print_help():
    print("""
    liststations - print a list of names of all subway stations \n
    listroutestations - lists the route of a specific train line (number or letter) \n
    listroutes - lists the train lines at a given station \n
    liststationportals - lists entrances/exits of a given station and if it has a elevator \n
    nearest - nearest <latitude> <longitude> would provide nearby stations and routes \n
    quit - """ )

def list_stations(connection: duckdb.DuckDBPyConnection):

  # create a list for station names
  #for each item in statuion dict, add station name to list sorted alphabetically
    query = f"""
            SELECT DISTINCT stop_name
            FROM stops
            ORDER BY stop_name ASC
        """

    connection.execute(query)
  
    #Getting names from the tuples
    station = [row[0] for row in connection.fetchall()]

    #print
    if stations:
        print("\nAll Subway Sations:")
        for station in stations:
            print(f"- {station}")
    else:
        print("No stations found.")
        
    #DONE

def list_route_stations(connection: duckdb.DuckDBPyConnection, route):
	# create a stations on a specific train line
	# for each station that has that train line, add station name to train station list
	# sort the list
	# print

    #Use of % since a station may serve many routes
    #This looks for route anywhere in the 'daytime_routes' column
    query = f"""
      Select Distinct stop_name 
      FROM stops
      WHERE daytime_routes like ?
      """
    connection.execute(query, (f'%{route.upper()}%',))

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
    # Get station name from user
    station = input("Enter the station name (e.g., Rector St, 86 St): ").strip()

	# for each train line found at a station, add train line to the list
    # Selecting daytime_routes based on station
    query = f"""
        Select DISTINCT daytime_routes
        FROM stops
        WHERE stop_name LIKE ?
    """

    # Use of % so '86 St' can find 86 St - Lex Ave'
    connection.execute(query, (f'%{station}%',))

	# sort the list
    # Using row[0] to unwrap
    routes = [row[0] for row in connection.fetchall()]
    routes.sort()

	# print
    if routes: 
        print(f"\nRoutes available at {station}:")
        for route in routes:
            print(f"- {route}")
    else:
        print(f"No routes found for station: {station}. Please check input")
	#done

def list_station_portals(connection: duckdb.DBPyConnection, station_name):
    # duckdb.query("""SELECT Entrance, Exit
    #                 WHERE Station Name == ?""", station_name)
    # Case sensitive
    query = f"""
        SELECT DISTINCY entrance_name, entrance_type
        FROM stops 
        WHERE stop_name = ?
    """

    connection.execute(query, (station_name,))
    # Fetch name and type
    portals = connection.fetchall()

    #Print
    if portals:
        print(f"\nPortals for {station_name}:")
        for name, e_type in portals:
            # Match unique name and what type of entrance
            print(f"- {name} (Type: {e_type})")
    else:
        print(f"No portals found for station: {station_name}. Double check station name")

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
    elif re.match(r"^listroutestations\s+(.+)$", user_input, re.IGNORECASE):
      match = re.match(r"^listroutestations\s+(.+)$", user_input, re.IGNORECASE)
      route = match.group(1).strip()
      list_route_stations(con, route)
    elif user_input == "^listroutes\s+(.+)$":
      
      list_routes(input)
    else:
      print("Invalid option. Type 'help' to see the list of valid commands.")
    user_input = str(input("Enter option: "))

if "__main__" == __name__:
  main()

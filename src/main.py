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
import sys, duckdb, re, math, unittest

#---------- MAIN PROGRAM FUNCTIONS ----------

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
    stations = [row[0] for row in connection.fetchall()]

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

def list_routes(connection: duckdb.DuckDBPyConnection, arguments):
	# Lists train lines of a specific station
  
  gps_match = re.match(r"^\((-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)\)$", arguments.strip(), re.IGNORECASE) # check for gps coordinate argument
  street_match = re.match(r"^([^,]+),\s*([^,]+),\s*(NE|NW|SE|SW)$", arguments.strip(), re.IGNORECASE) # Check for street address

  if gps_match:
    #extract arguments
    latitude = gps_match.group(1)
    longitude = gps_match.group(2)
    station = f"({latitude}, {longitude})" # for output
    
    query = """
      SELECT DISTINCT daytime_routes
      FROM stops
      WHERE gtfs_latitude == ?   
      AND gtfs_longitude == ?;
    """
    params = [latitude, longitude]
  elif street_match:
    station = None

    query = f"""
      Select DISTINCT daytime_routes
      FROM stops
      WHERE stop_name LIKE ?
    """

    params = []
  else: # Invalid case
    print(f"No routes found for station: {station}. Please check input")
	

  connection.execute(query, params)
  #clean up results
  routes = [row[0] for row in connection.fetchall()][0]
  routes = routes.split(' ')

	# print
  print(f"\nRoutes available at{station}:")
  for route in routes:
    print(f"- {route}")
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

def nearest(connection: duckdb.DuckDBPyConnection, latitude: float , longitude: float):
  if abs(latitude) > 180 or abs(longitude) > 180:
    print("Invalid nearest command. Type 'help' for usage details.")
    return
  
  rows = connection.execute("""
    SELECT
      stop_name,
      gtfs_latitude,
      gtfs_longitude,
      daytime_routes,
    FROM stops
""").fetchall()
  
  min_distance = float('inf')
  closest = None

  for row in rows:
    plat = row[1]
    plon = row[2]

    distance = haversine(latitude, longitude, plat, plon)

    if distance < min_distance:
      min_distance = distance
      closest = row

    print("\nClosest portal:")
    print(f"    General portal location: {closest[3]} & {closest[4]} at {closest[5]} corner")
    print(f"    Unique portal: ({closest[1]}, {closest[2]})")

    routes = closest[6].replace(" ", ",")
    print(f"\nClosest routes: {routes}")
	#Done 

#---------- HELPER FUNCTIONS ----------

def haversine(lat1, long1, lat2, long2) -> float:
  TWO_R = 2 * 6368 #km - earth's radious
  delta_phi = (lat2 - lat1) / 2
  delta_lamda = (long2 - long1) / 2
  return TWO_R * math.asin(math.sqrt(math.pow(math.sin(delta_phi), 2) + math.cos(lat1) * math.cos(lat2) * math.pow(math.sin(delta_lamda), 2)))

def init_db():
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
  return con

#---------- MAIN ----------

def main(connection: duckdb.DuckDBPyConnection):
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
      # help case
      print_help()
    elif user_input == "liststations":
      # list stations case
      list_stations()
    elif re.match(r"^listroutestations\s+(.+)$", user_input, re.IGNORECASE):
      # List route stations case
      match = re.match(r"^listroutestations\s+(.+)$", user_input, re.IGNORECASE)
      route = match.group(1).strip()
      list_route_stations(con, route)
    elif re.match(r"^listroutes\s+(.+)$", user_input, re.IGNORECASE):
      match = re.match(r"^listroutes\s+(.+)$", user_input, re.IGNORECASE)
      args = match.group(1).strip()
      list_routes(con, args)
    else:
      # invalid case
      print("Invalid option. Type 'help' to see the list of valid commands.")

    user_input = str(input("Enter option: "))

if "__main__" == __name__:
  if len(sys.argv) < 1:
    print("""Error: No arguments were provided. Please provide the path to the mta data table as an argument.\nUsage: main.py <path to mta data table>""")
    exit(1)
  else:
    file_path = sys.argv[1]

  con = init_db()
  list_routes(con, "(40.75529, -73.987495)")
  main(con)

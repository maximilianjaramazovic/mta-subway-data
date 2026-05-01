[1mdiff --cc src/main.py[m
[1mindex b8a453c,29e386c..0000000[m
[1m--- a/src/main.py[m
[1m+++ b/src/main.py[m
[36m@@@ -12,7 -12,47 +12,51 @@@[m
    Date: 4/20/2026[m
    Data Source: [m
  """[m
[32m++<<<<<<< HEAD[m
[32m +import sys, csv, duckdb, os[m
[32m++=======[m
[32m+ import sys, csv, sqlite3[m
[32m+ [m
[32m+ def main():[m
[32m+   # Checking for input data table[m
[32m+   arguments_list = sys.argv[1:][m
[32m+   if len(arguments_list) != 1:[m
[32m+     print("""Error: No arguments were provided. Please provide the path to the mta data table as an argument.\nUsage: main.py <path to mta data table>""")[m
[32m+     exit(1)[m
[32m+   else:[m
[32m+     file_path = arguments_list[1][m
[32m+     initialize_db(file_path)[m
[32m+ [m
[32m+ [m
[32m+   print("""[m
[32m+     Welcome to the subway program. \n[m
[32m+     To begin, try typing 'help' to see the list of valid commands. \n[m
[32m+     """)[m
[32m+   [m
[32m+   # Program loop[m
[32m+   user_input = str(input("Enter option: "))[m
[32m+   while user_input != "quit":[m
[32m+     if user_input == "help":[m
[32m+       print_help()[m
[32m+     else:[m
[32m+       print("Invalid option. Type 'help' to see the list of valid commands.")[m
[32m+     user_input = str(input("Enter option: "))[m
[32m+ [m
[32m+ def initialize_db(file_path):[m
[32m+   with sqlite3.connect('mta.db') as con:[m
[32m+     cur = con.cursor()[m
[32m+     with open(file_path, mode="r") as f:[m
[32m+         reader = csv.reader(f)[m
[32m+         reader.__next__() # skipping header[m
[32m+         data = list(reader)[m
[32m+ [m
[32m+     # Bulk insterting data into the database[m
[32m+     cur.executemany("INSERT INTO stations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?", data)[m
[32m+ [m
[32m+ [m
[32m+ if "__main__" == __name__:[m
[32m+   main()[m
[32m++>>>>>>> routestations[m
  [m
  def print_help():[m
          print("""[m

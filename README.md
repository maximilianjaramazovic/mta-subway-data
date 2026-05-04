# MTA Subway Data CLI

A command-line subway station data management and lookup system built in Python using DuckDB.

This project allows users to load MTA subway station data from CSV and interactively query station information, train routes, route stations, nearby portals, and nearest subway locations through a terminal interface.

---

## Features

- Load and manage MTA subway station data using DuckDB
- Query all subway stations
- List stations served by a specific route
- List routes available at a station portal
- Find portals belonging to a station
- Locate the nearest subway station from GPS coordinates
- Interactive command-line interface

---

## Tech Stack

- Python 3.14+
- DuckDB
- uv package manager

---

## Project Structure

```text
mta-subway-data/
│
├── src/
│   └── main.py
│
├── res/
│   └── mta_subway_stations.csv
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Installation

This project uses `uv` for dependency and environment management.

### 1. Clone the repository

```bash
git clone https://github.com/maximilianjaramazovic/mta-subway-data.git
cd mta-subway-data
```

### 2. Sync dependencies

```bash
uv sync
```

This will create the local virtual environment and install all required packages.

---

## Running the Program

Run the CLI by providing the MTA station CSV file as a command-line argument:

```bash
uv run src/main.py ./res/mta_subway_stations.csv
```

---

## Available Commands

| Command | Description |
|---------|-------------|
| `help` | Display all valid commands |
| `liststations` | List all subway stations |
| `listroutestations <route>` | List all stations on a given route |
| `listroutes <portal>` | List all train routes accessible from a portal |
| `liststationportals <station>` | List all portals for a given station |
| `nearest <latitude> <longitude>` | Find nearest subway station to coordinates |
| `quit` | Exit the program |

---

## Example Usage

```text
Enter option: listroutestations A
Enter option: listroutes (40.753087, -73.979537)
Enter option: nearest 40.684 -73.977
Enter option: quit
```

---

## Data Source

MTA Subway Stations dataset provided by the U.S. Government open data catalog:

https://catalog.data.gov/dataset/mta-subway-stations

---

## Notes

- The program expects a valid MTA subway stations CSV file at startup.
- If no file path is provided, the program exits with an error.
- If the file cannot be opened or appears corrupted, the program exits safely.

---

## Authors

Nathan Climaco, Maximilian Jaramazovic, Christopher Sandoval Ochoa

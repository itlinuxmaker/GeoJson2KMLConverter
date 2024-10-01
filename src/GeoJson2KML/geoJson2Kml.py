import os
import json
import simplekml
from datetime import datetime, timezone

"""
GeoJson2Kml Converter
Version: 1.0.0
Author: Andreas Günther, info@it-linuxmaker.com
License: GPL-3.0

This program is released under the terms of the GNU General Public License version 3.
For more information, see the license file or https://www.gnu.org/licenses/gpl-3.0.de.html
"""

# Function for secure parsing of timestamps
def parse_timestamp(timestamp_str):
    try:
        return datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S%z")

# Function to filter positions based on startTimestamp and endTimestamp
def filter_positions(file_path, start_date, end_date):
    filtered_positions = []
    with open(file_path, "r") as f:
        data = json.load(f)
        for entry in data.get("timelineObjects", []):
            if "activitySegment" in entry:
                segment = entry["activitySegment"]
                if "duration" in segment:
                    start_timestamp = parse_timestamp(segment["duration"]["startTimestamp"])
                    end_timestamp = parse_timestamp(segment["duration"]["endTimestamp"])
                    if start_timestamp <= end_date and end_timestamp >= start_date:
                        filtered_positions.append(segment)
            if "placeVisit" in entry:
                visit = entry["placeVisit"]
                if "duration" in visit:
                    start_timestamp = parse_timestamp(visit["duration"]["startTimestamp"])
                    end_timestamp = parse_timestamp(visit["duration"]["endTimestamp"])
                    if start_timestamp <= end_date and end_timestamp >= start_date:
                        filtered_positions.append(visit)
    
    return filtered_positions

# Main function for browsing the years and months and creating the KML file
def extract_and_generate_kml(base_path, start_date, end_date, include_lines):
    all_filtered_positions = []
    
    # Check if we are in the correct directory (where the year folders are)
    if not any(folder.isdigit() and len(folder) == 4 for folder in os.listdir(base_path)):
        raise FileNotFoundError("Jahresordner nicht gefunden. Bitte wechseln Sie in das Verzeichnis, das direkt oberhalb der Jahresordner liegt.")

    # Scrolling through the years and months in the directory
    for year_dir in sorted(os.listdir(base_path)):
        year_path = os.path.join(base_path, year_dir)
        if os.path.isdir(year_path):
            for month_file in sorted(os.listdir(year_path)):
                if month_file.endswith(".json"):
                    month_file_path = os.path.join(year_path, month_file)
                    print(f"Verarbeite: {month_file_path}")
                    filtered_positions = filter_positions(month_file_path, start_date, end_date)
                    all_filtered_positions.extend(filtered_positions)

    # Sort all positions chronologically by start time
    all_filtered_positions.sort(key=lambda x: parse_timestamp(x['duration']['startTimestamp']))

    # Generate KML file
    kml = simplekml.Kml()

    # Adding the positions to the KML file
    for entry in all_filtered_positions:
        if "location" in entry and "latitudeE7" in entry["location"] and "longitudeE7" in entry["location"]:
            lat = entry["location"]["latitudeE7"] / 1e7
            lon = entry["location"]["longitudeE7"] / 1e7
            address = entry.get("location", {}).get("address", "Unbekannte Adresse")
            start_time = entry["duration"]["startTimestamp"]
            end_time = entry["duration"]["endTimestamp"]

            point = kml.newpoint(coords=[(lon, lat)])
            point.name = address
            point.description = f"Start: {start_time}\nEnde: {end_time}"
            point.timestamp.when = start_time

        # Add the lines if desired
        if include_lines and "startLocation" in entry and "endLocation" in entry:
            start_lat = entry["startLocation"]["latitudeE7"] / 1e7
            start_lon = entry["startLocation"]["longitudeE7"] / 1e7
            end_lat = entry["endLocation"]["latitudeE7"] / 1e7
            end_lon = entry["endLocation"]["longitudeE7"] / 1e7

            line = kml.newlinestring(
                coords=[(start_lon, start_lat), (end_lon, end_lat)]
            )

            start_time = entry["duration"]["startTimestamp"]
            end_time = entry["duration"]["endTimestamp"]
            line.name = f"Strecke von {start_time} bis {end_time}"
            line.description = f"Strecke von {start_time} bis {end_time}"
            line.style.linestyle.color = simplekml.Color.blue
            line.style.linestyle.width = 3

    # File name based on the time period
    kml_filename = f"location_history_{start_date.strftime('%Y-%m-%d')}_bis_{end_date.strftime('%Y-%m-%d')}.kml"
    kml.save(kml_filename)
    print(f"KML-Datei {kml_filename} erfolgreich erstellt.")

# Enter the time period
start_date_str = input("Startdatum (im Format YYYY-MM-DD): ")
end_date_str = input("Enddatum (im Format YYYY-MM-DD): ")

# Option to add the lines
include_lines = input("Sollen auch die Strecken (Linien) hinzugefügt werden? (ja/nein): ").lower() == 'ja'

# Converting the start and end dates to datetime objects
start_date = datetime.strptime(start_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
end_date = datetime.strptime(end_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)

# Set the base path as the current working directory
base_path = os.getcwd()

# Starting the extraction and KML generation
try:
    extract_and_generate_kml(base_path, start_date, end_date, include_lines)
except FileNotFoundError as e:
    print(e)
    sys.exit(1)

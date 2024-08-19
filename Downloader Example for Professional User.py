# This python script provides an example of how reports and datasets can be downloaded directly form GSSA.
# User who use this script to download datasets need to prepare their python environment and workspace.
# 
# Downloader Example for Professional User.py
# Author: Alex Zou
# Aug 2024


import os
import json
import requests
import csv

url = "https://catalog.uat.sarig.sa.gov.au/api/3/action/recently_changed_packages_activity_list"

# Send GET request and handle response
response = requests.get(url)

if response.status_code == 200:
  # Parse JSON data
  data = response.json()

  # Create list to store package titles
  package_titles = []

  # Extract package titles from response
  for item in data["result"]:
    package_titles.append(item["data"]["package"]["title"])

  # Create download folder if it doesn't exist
  import os
  download_folder = "/download"
  if not os.path.exists(download_folder):
    os.makedirs(download_folder)

  # Save package titles to CSV file
  with open(os.path.join(download_folder, "recently_changed_packages.csv"), "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Package Title"])  # Header row
    writer.writerows(zip(package_titles))  # Write each title as a row

  print("Successfully saved package titles to recently_changed_packages.csv")
else:
  print(f"Error: Request failed with status code {response.status_code}")
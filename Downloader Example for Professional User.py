# Example: Download "recently changed dataset activity" from the SARIG Catalogue (CKAN Action API).
# Note: This script downloads JSON activity metadata (not the dataset files themselves).
#

# Author: Alex Zou
# Date: March 2026

import os
import requests
import pandas as pd
import urllib3

# 1. Setup & Security Bypass
# Silences the 'InsecureRequestWarning' caused by verify=False (Please make sure you are on controlled network with a known TLS interception proxy)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 2. Configuration
# You can change the URL to search for gold, return up to 100 rows, IMPORTANT:package_search stores the list in data['result']['results'], please use json_normalize to flatten the nested dictionaries
# URL = "https://catalog.sarig.sa.gov.au/api/3/action/package_search?q=gold&rows=100"
URL = "https://catalog.sarig.sa.gov.au/api/3/action/recently_changed_packages_activity_list"
FOLDER_NAME = "datafolder"
FILE_NAME = "sarig_recently_changed_packages_activity.csv"
FILE_PATH = os.path.join(FOLDER_NAME, FILE_NAME)

# Mimic a real browser to avoid 403 Forbidden errors
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 3. Create the folder if it doesn't exist
if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)
    print(f"Created folder: {FOLDER_NAME}")

# 4. Fetch the data
try:
    print("Connecting to SARIG API...")
    response = requests.get(URL, headers=HEADERS, verify=False, timeout=15)
    
    # Raise an error if the HTTP request failed (e.g., 403, 404, 500)
    response.raise_for_status()
    
    data = response.json()

    if data.get('success'):
        # 5. Process and Save
        activities = data['result']
        df = pd.DataFrame(activities)
        
        # Save to the specific folder path
        df.to_csv(FILE_PATH, index=False)
        print(f"Success! Data saved to: {FILE_PATH}")
        print(f"Total records retrieved: {len(df)}")
    else:
        print("API returned success=False. Check the URL or API status.")

except requests.exceptions.HTTPError as err:
    print(f"HTTP Error occurred: {err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


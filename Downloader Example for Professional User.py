# Example: download recent package activity metadata from the SARIG catalogue CKAN Action API.
# Note: this script exports activity metadata to CSV; it does not download dataset files.
#
# Author: Alex Zou
# Updated: 2026-06-24
# Review note: request shape and response handling were reviewed in-repo; live endpoint verification
# could not be completed from this environment because catalog.sarig.sa.gov.au did not resolve.

import os

import pandas as pd
import requests
import urllib3


def env_flag(name: str, default: str = "true") -> bool:
    return os.getenv(name, default).strip().lower() not in {"0", "false", "no", "off"}


VERIFY_TLS = env_flag("SARIG_VERIFY_TLS", "true")
URL = "https://catalog.sarig.sa.gov.au/api/3/action/recently_changed_packages_activity_list"
FOLDER_NAME = "datafolder"
FILE_NAME = "sarig_recently_changed_packages_activity.csv"
FILE_PATH = os.path.join(FOLDER_NAME, FILE_NAME)
TIMEOUT_SECONDS = 30

# Example alternate query shape:
# https://catalog.sarig.sa.gov.au/api/3/action/package_search?q=gold&rows=100

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

if not VERIFY_TLS:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.makedirs(FOLDER_NAME, exist_ok=True)

try:
    print("Connecting to SARIG API...")
    response = requests.get(
        URL,
        headers=HEADERS,
        verify=VERIFY_TLS,
        timeout=TIMEOUT_SECONDS,
    )
    response.raise_for_status()

    data = response.json()
    activities = data.get("result", [])

    if not data.get("success"):
        raise ValueError("API returned success=False.")

    if not isinstance(activities, list):
        raise ValueError("Expected the CKAN action to return a list in result.")

    df = pd.DataFrame(activities)
    df.to_csv(FILE_PATH, index=False)

    print(f"Success! Data saved to: {FILE_PATH}")
    print(f"Total records retrieved: {len(df)}")

except requests.exceptions.RequestException as err:
    print(f"Request error occurred: {err}")
except ValueError as err:
    print(f"Response validation error: {err}")
except Exception as err:
    print(f"An unexpected error occurred: {err}")

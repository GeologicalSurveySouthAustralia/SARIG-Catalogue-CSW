# This python script provides an example of how reports and datasets can be downloaded directly form GSSA.
# User who use this script to download datasets need to prepare their python environment and workspace.
# 
# Downloader Example for Professional User.py
# Author: Alex Zou
# Aug 2024


import csv
import os
import requests
from urllib import parse
import json
from pathlib import Path
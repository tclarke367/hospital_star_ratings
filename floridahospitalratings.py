# Project 1: Florida hospital star ratings vs. county demographics
# Does the location ownership of hospitals impact their rating (what conclusion can I draw from this) 

import csv          # saving a spreadsheet
import os           # making the output folder
import statistics   # averages and medians
import requests     # getting data from websites

HOSPITAL_URL = "https://data.cms.gov/provider-data/api/1/datastore/query/xubh-q36u/0"
COUNTY_URL = ("https://onemap.cdc.gov/onemapservices/rest/services/SVI/"
              "CDC_ATSDR_Social_Vulnerability_Index_2022_USA/FeatureServer/1/query")

def get_hospitals():
    # get every Florida hospital from Medicare
    settings = {"limit": 500, "conditions[0][property]": "state", "conditions[0][value]": "FL"}
    response = requests.get(HOSPITAL_URL, params=settings)
    if response.status_code != 200:
        print("Couldn't get hospitals, error", response.status_code)
        return []
    return response.json()["results"]


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

def get_counties():
    # get percent of Black, percent of Hispanic, and percent of uninsured for every Florida county (from the CDC)
    settings = {"where": "ST_ABBR='FL'", "outFields": "COUNTY,EP_AFAM,EP_HISP,EP_UNINSUR",
                "returnGeometry": "false", "f": "json"}
    response = requests.get(COUNTY_URL, params=settings)
    if response.status_code != 200:
        print("Couldn't get counties, error", response.status_code)
        return {}

    counties = {}
    for item in response.json()["features"]:
        info = item["attributes"]
        counties[fix_name(info["COUNTY"])] = {
            "pct_black": info["EP_AFAM"],
            "pct_hispanic": info["EP_HISP"],
            "pct_uninsured": info["EP_UNINSUR"],
        }
    return counties


def fix_name(name):
    # Medicare site uses all caps n says "ST. JOHNS" and the CDC says "St. Johns County",
    # make both look the same: uppercase, no "COUNTY", no spaces,dots, or dashes
    name = name.upper().replace(" COUNTY", "")
    for symbol in [" ", ".", "-"]:
        name = name.replace(symbol, "")
    return name


def describe(label, stars):
    #how many hospitals, average stars, percent that got 1-2 stars
    low = len([s for s in stars if s <= 2])
    avg = round(statistics.mean(stars), 2)
    return f"  {label}: {len(stars)} hospitals, avg {avg} stars, {round(100 * low / len(stars))}% got 1-2 stars"




def main():
    # get data from both websites
    hospitals = get_hospitals()
    counties = get_counties()
    if not hospitals or not counties:
        print("Missing data, stopping")
        return

    #keep only the hospitals that have a star rating and add their county's info
    rated = []
    for h in hospitals:
        if h["hospital_overall_rating"].isdigit():
            county = counties[fix_name(h["countyparish"])]
            rated.append({
                "name": h["facility_name"],
                "county": h["countyparish"],
                "ownership": h["hospital_ownership"],
                "stars": int(h["hospital_overall_rating"]),
                "pct_black": county["pct_black"],
                "pct_hispanic": county["pct_hispanic"],
                "pct_uninsured": county["pct_uninsured"],
            })

    print(len(rated), "of", len(hospitals), "Florida hospitals have a star rating")


if __name__ == "__main__":
    main()
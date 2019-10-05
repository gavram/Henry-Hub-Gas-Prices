import os
import requests
import json
import csv
import matplotlib
from matplotlib import pyplot as plt

api_url_annual = "https://api.eia.gov/series/?api_key=" \
                 + "76c7b40fb506528c68e66cc40d1a2670&series_id=NG.RNGWHHD.A"

# Obtaining Yearly Data for Natural Gas Prices and writing in
# "CSVs\annual.csv", using annual API series_id
json_data = requests.get(api_url_annual).json()
with open('CSVs/annual.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Year', 'Price'])
    writer.writerows(json_data ['series'][0]['data'])

api_url_monthly = "https://api.eia.gov/series/?api_key=" \
                   + "76c7b40fb506528c68e66cc40d1a2670&series_id=NG.RNGWHHD.M"

# Obtaining Monthly Data for Natural Gas Prices and writing in
# "CSVs\monthly_from_api.csv", using monthly API series_id
json_data = requests.get(api_url_monthly).json()
with open('CSVs/monthly.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Month/Year', 'Price'])
    for pair in json_data ['series'][0]['data']:
        date = pair[0]
        date = date[4:6] + "/" + date[0:4]
        price = pair[1]
        writer.writerow([date, price])

api_url_daily = "https://api.eia.gov/series/?api_key=" \
                + "76c7b40fb506528c68e66cc40d1a2670&series_id=NG.RNGWHHD.D"

# Obtaining Daily and Monthly Data for Natural Gas Prices, then writing in
# "CSVs\daily_from_api.csv" and "CSVs\monthly_from_daily_api.csv",
# using daily API series_id

# Daily Prices
json_data = requests.get(api_url_daily).json()
with open('CSVs/daily.csv', 'w', newline="") as csvfile:
    writer_day = csv.writer(csvfile)
    writer_day.writerow(['Date', 'Price'])
    for pair in json_data ['series'][0]['data']:
        date = pair[0]
        date_day = date[4:6] + "/" + date[6:8] + "/" + date[0:4]
        price = pair[1]
        if bool(price):
            writer_day.writerow([date_day, price])

# Monthly Prices as prices for the first day of the month
# for which data is available, from Daily API
with open('CSVs/monthly_from_daily_api.csv', 'w', newline="") as csvfile:
    writer_month = csv.writer(csvfile)
    writer_month.writerow(['Month/Year', 'Price'])
    n = len(json_data ['series'][0]['data'])
    for i in range(0,n-1):
        if i > 0 :        
            pair = json_data ['series'][0]['data'][i]
            pair_prev = json_data ['series'][0]['data'][i-1]
            date = pair[0]
            date_prev = pair_prev[0]
            if int(date_prev[4:6])>int(date[4:6]) or \
               int(date[0:4]) > int(date_prev[0:4]):
                date_new = date[4:6] + "/" + date[0:4]
                price = pair[1]
                writer_month.writerow([date_new, price])
        i = i + 1
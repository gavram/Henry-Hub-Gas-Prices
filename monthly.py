import os
import requests
import json
import csv
import matplotlib
from matplotlib import pyplot as plt

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

# Wait for user input
# Displaying chart on screen
print("Data is stored in CSVs/monthly.csv")
key = input("Do you want to print a chart? Press 'y'" \
            + " to print chart or any other key to quit program: " )
if key == 'y':
    # Printing chart
    x = []
    y = []
    with open('CSVs/monthly.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in plots:
            if i > 0:
                x.append(float(row[0][3:8])+float(row[0][0:2])/12)
                y.append(float(row[1]))
            i = i + 1
    plt.figure(figsize=(30, 10))
    plt.plot(x, y, label='Natural Gas Monthly Prices')
    plt.xlabel('Month')
    plt.ylabel('Price')
    plt.title('Natural Gas Monthly Prices')
    plt.axis([1997, 2020, 0, 15])
    plt.grid(True)
    plt.legend()
    plt.show()
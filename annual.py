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

# Wait for user input
# Displaying chart on screen
print("Data is stored in CSVs/annual.csv")
key = input("Do you want to print a chart? Press 'y'" \
            + "to print chart or any other key to quit program: " )
if key == 'y':
    x = []
    y = []
    with open('CSVs/annual.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in plots:
            if i > 0:
                x.append(int(row[0]))
                y.append(float(row[1]))
            i = i + 1
    plt.figure(figsize=(30, 10))
    plt.plot(x, y, label='Natural Gas Yearly Prices')
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.title('Natural Gas Yearly Prices')
    plt.axis([1997, 2018, 0, 10])
    plt.grid(True)
    plt.legend()
    plt.show()

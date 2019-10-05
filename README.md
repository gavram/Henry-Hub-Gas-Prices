# Henry-Hub-Gas-Prices

	This small project is used to get Henry Hub natural gas prices.

	Prices are obtained from http://www.eia.gov/dnav/ng/hist/rngwhhdm.htm.

While there are many ways to get pricing from this site, the API
method has been chosen here for many reasons. The main reasons are the speed,
the simplicity of the Python code and the non-overloading of the server with
unnecessary queries.

The resulting data is in the CSVs folder.
	
	1. annual.py
Annual data for the price of natural gas. The data is obtained using
annual.py where there is an option and the ability to represent the data graphically
on the screen. The data is stored in annual.csv

	2. monthly.py
Monthly data for the price of natural gas. The data is obtained using monthly.py,
where there is an option and the ability to represent the data graphically on the
screen. The data is stored in monthly.csv

	3. daily.py
Daily data for the price of natural gas. The data is obtained using daily.py, which has the option and the ability to represent the data graphically on the screen. The data is stored in daily.csv
	This program is also used to obtain monthly data using the daily API, as the first date of the month for which data is available. The data is stored in monthly_from_daily_api.csv
	
	4. ng_prices.py
	This is a program that combines the previous three, but without the ability to draw a chart. The data is stored in the previously mentioned CSV files.

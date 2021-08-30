BNB analysis project

This project is base on the Binance Coin Data set [Here](https://www.kaggle.com/amritpal333/binance-coin-data) made by Dr. Amritpal Singh 
and enriched using the CoinGecko api[here](https://www.coingecko.com/es/api/documentation?)[here](https://api.coingecko.com/api/v3/coins/binancecoin/market_chart/range?vs_currency=usd&from=1510185600&to=1627344000000)
for additional information to be able to analyze the BNB token to its potential.
This project is to be able to understand better the previous movements of this token and to be able to project its future with further exploration.
All of the exploration into the data has been carried out with Python using Jupyter Notebook[here](https://jupyter-notebook.readthedocs.io/en/stable/) and VCS(VisualStudioCode)[here](https://code.visualstudio.com/docs)

To clean and enrich the data, various techniques have been used, such as:
- Changing and re arranging data to be in a clearer, more legible order.
- Calling of API for additional data that was not available in the original dataset.
- Extraction of data from API and creation of new dataframe.
- Use of unix timestamp and its conversion into legible date time.
- Merge between two datasets, using merge option.

Various libraries were used to import, transform and visualize the data given. These are:
-pandas[here](https://pandas.pydata.org/docs/)
-requests[here](https://docs.python-requests.org/en/master/)
-json [here](https://docs.python.org/3/library/json.html)
-plotly.express [here](https://plotly.com/python/plotly-express/)





import yfinance as yf
import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

prices = yf.download("AAPL", start="2020-01-01", end="2020-12-31")['Close']

#pct change is used to determine with how many percent from the starting price has it risen
#F.E starting = 80 ending = 100, how many percent is the change?
# 80 + x%.80 = 100  do the math, and we get ->    x = (100-80/80)*100
#formula for pct change = 100 * (P_new - P_old)/P_old
# When pct_change is positive -> growth and vice versa when it's negative


returns = prices.pct_change().dropna()
daily_stdev = float(returns.std())
last_price = float(prices.iloc[-1])

# standard deviation shows how clustered all possible points are. The higher it is the worse it is for us because
# stdev works this way: there is a mean value and the further we go from the center, the bigger the spread is
# meaning the bigger the stdev the bigger the possibility is for the computer to choose an inaccurate value
# therefore making the prediction of the price less reliable
# its formula is calculating the means of the prices basically and gives a range for the computer to chose from.
#number of simulations
num_simulations = 5

num_days = 252

random_shocks = np.random.normal(0, daily_stdev, (num_days, num_simulations))
price_paths = last_price * (1 + random_shocks).cumprod(axis=0)

#random_shocks uses the standard deviation to pick a random percentage return in that range
#price_paths forms each point in the grid using the random shock.

print(daily_stdev)

plt.figure(figsize=(10, 6))
plt.plot(price_paths)
plt.title("Monte Carlo Simulation of AAPL")
plt.show()

#so to summarize: standard deviation creates a "radius" of points filled with the percentage return.
# Then, random_shocks groups it under a variable scattered across the number of days and simulations.
# Lastly, price_paths generates each point by: multiplies it by those scattered percentage returns day-by-day,
# generating the final dollar-value points in the grid.
#jwsd

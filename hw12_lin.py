''' Take your solution from Homework 11 and complete the Monte Carlo
step (step 6) in parallel. There are many ways you can go about doing
this, and I'm not looking for anything too complicated. If you can get
multiple processes crunching the data together, that is great. Using
IPython’s built-in tools would be a great method Compare the timing for
your solution in homework 11 and this parallel solution. This is similar
to what you did in homeworks 6 and 7. Ideally, you'll see some speed
improvement. The amount you see will largely be based the capabilities
of your hardware, and less on the software implementation. There is
additional overhead for running an operation in parallel, so speed gains
will be more obvious with a larger number of calculations. As with the
last homework, you will submit this to me as an IPython notebook.
Include the results of your comparison there, along with everything else
(code, charts, graphs, etc.) '''

import os
os.chdir('/Python27/Lib/site-packages')
os.getcwd()

import time
import numpy  as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:/Users/blin261/Desktop/DATA602/apple.2011.csv", names = ["date", "price", "percent change"], skiprows = 1)
df["percent change"] = pd.to_numeric(df["percent change"], errors = "coerce")

mu = df["percent change"].mean()
sigma = df["percent change"].std()
last_price = df["price"].iloc[-1]

def final_price(last_price, mu, sigma, days):
    s = np.random.normal(mu, sigma, days)
    for i in s:
        last_price = last_price * (1 + i)
    return last_price

def MonteCarlo(last_price, mu, sigma, loops):
    output = []
    for i in range(loops):
        output.append(final_price(last_price, mu, sigma, 20))
    return output

#Regular Method

np.random.seed(888)
start = time.clock()
MonteCarlo(last_price, mu, sigma, 10000)
run_time_regular = time.clock() - start
print run_time_regular

import ipyparallel
clients = ipyparallel.Client()
clients.block = True
print clients.ids


#Parallel Method One

dview = clients.direct_view()
dview = clients[:]

start = time.clock()
%px output = []
for i in range(10000):
    output.append(final_price(last_price, mu, sigma, 20))

output = dview.gather("output")
run_time_parallel = time.clock() - start
print run_time_parallel

#Parallel Method Two

dview = clients.direct_view()
dview = clients[:]

start = time.clock()
output = dview.apply_async(MonteCarlo, "last_price, mu, sigma, 10000")
run_time_parallel2 = time.clock() - start
print run_time_parallel2

print ("Regular Method Processing Time: %s seconds" % run_time_regular)
print ("Parallel Method One Processing Time: %s seconds" % run_time_parallel)
print ("Parallel Method Two Processing Time: %s seconds" % run_time_parallel2)

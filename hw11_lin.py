import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def final_price(last_price, mu, sigma, days):
    s = np.random.normal(mu, sigma, days)
    for i in s:
        last_price = last_price * (1 + i)
    return last_price


if __name__ == "__main__":
    df = pd.read_csv("C:/Users/blin261/Desktop/DATA602/apple.2011.csv",
    names = ["date", "price", "percent change"], skiprows = 1)
    
    df["percent change"] = pd.to_numeric(df["percent change"], errors = "coerce")
    df["price"] = pd.to_numeric(df["price"], errors = "coerce")

    print df.head()
    print df.dtypes


    mu = df["percent change"].mean()
    sigma = df["percent change"].std()
    print mu
    print sigma


    last_price = df["price"].iloc[-1]
    print last_price
    
    np.random.seed(888)
    print final_price(last_price, mu, sigma, 20)

    output = []
    for i in range(10000):
        output.append(final_price(last_price, mu, sigma, 20))

    plt.hist(output)
    plt.xlabel('Apple Stock Price')
    plt.ylabel("Frequency")
    plt.show()

    VaR = np.percentile(output, 1)
    print VaR
    

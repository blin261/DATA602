import pandas as pd
import numpy as np
import re


if __name__ == "__main__":
    df = pd.read_csv("C:/Users/blin261/Desktop/DATA602/epa-http.txt",
    sep = "\s+", header = None, na_values = "-", names = ["host", "time", "request",
    "http_reply_code", "bytes"])


    print df.dtypes
    print df.head()


    print ""
    print "Question 1: Which hostname or IP address made the most requests?"
    host_size = df.groupby("host").size()
    host_size = host_size.sort_values(ascending = False)
    print host_size[:1]


    print""
    print "Question 2: Which hostname or IP address received the most total bytes from the server?  How many bytes did it receive?"
    df["bytes"] = pd.to_numeric(df["bytes"])
    bytes_size = df.groupby("host")["bytes"].sum()
    bytes_size = bytes_size.sort_values(ascending = False)
    print bytes_size[:1]


    print ""
    print "Question 3: During what hour was the server the busiest in terms of requests?"
    df["time"] = pd.to_datetime(df["time"], format = "[%d:%H:%M:%S]")
    df["hour"] = df["time"].dt.hour
    hourly_request = df.groupby("hour").size()
    hourly_request = hourly_request.sort_values(ascending = False)
    print hourly_request[:1]


    print ""
    print "Question 4: Which .gif image was downloaded the most during the day?"
    df_subset = df[df['http_reply_code'].isin(['200'])]
    gif_image = df_subset[df_subset["request"].str.contains(".gif ")]
    gif_size = gif_image.groupby("request").size()
    gif_size = gif_size.sort_values(ascending = False)
    print gif_size[:1]


    print ""
    print "Question 5: What HTTP reply codes were sent other than 200?"
    df_subset1 = df[-df['http_reply_code'].isin(['200'])]
    http_code_size = df_subset1.groupby("http_reply_code").size()
    http_code_size = http_code_size.sort_values(ascending = False)
    print http_code_size   

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.ndimage as ndimage
import scipy.misc as misc
from scipy import stats
from scipy.optimize import curve_fit


if __name__ == "__main__":
    '''
    1. Express the cars.data.csv data as a series of bar graphs.
    '''
    df = pd.read_csv("C:/Users/blin261/Desktop/DATA602/cars.data.csv",
    header = None, names = ["buying", "maint", "doors",
    "persons", "lug_boot", "safety", "class_distribution"])
    
    plt.figure(1)
    
    plt.subplot(221)
    buying_size = df.groupby("buying").size()
    x = np.arange(len(list(buying_size.index)))
    y = np.array(buying_size)
    plt.bar(x, y, color = "red")
    plt.xticks(x, list(buying_size.index))
    plt.xlabel('buying')
    plt.ylabel("Frequency")

    plt.subplot(222)
    maint_size = df.groupby("maint").size()
    x = np.arange(len(list(maint_size.index)))
    y = np.array(buying_size)
    plt.bar(x, y, color = "yellow")
    plt.xticks(x, list(maint_size.index))
    plt.xlabel('maint')
    plt.ylabel("Frequency")

    plt.subplot(223)
    safety_size = df.groupby("safety").size()
    x = np.arange(len(list(safety_size.index)))
    y = np.array(safety_size)
    plt.bar(x, y, color = "blue")
    plt.xticks(x, list(safety_size.index))
    plt.xlabel('safety')
    plt.ylabel("Frequency")

    plt.subplot(224)
    doors_size = df.groupby("doors").size()
    x = np.arange(len(list(doors_size.index)))
    y = np.array(doors_size)
    plt.bar(x, y, color = "green")
    plt.xticks(x, list(doors_size.index))
    plt.xlabel('doors')
    plt.ylabel("Frequency")
    
    plt.show()

    '''
    2. Plot your results from the linear regression in homework 5 and 7
    (for any of the provided data sets).  The plot should include.
    '''
    
    brainandbody = pd.read_csv('C:/Users/blin261/Desktop/DATA602/brainandbody.csv')
    brain = brainandbody["brain"]
    body = brainandbody["body"]
    plt.scatter(brain, body,  color = 'black')
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(brain, body)
    line = slope * brain + intercept
    plt.plot(brain, line, 'r-')
    linear_equation = "body = %s * brain %s" % (slope, intercept)
    
    plt.text(1000, 5000, linear_equation)
    plt.xlabel('Brain Weight')
    plt.ylabel("Body Weight")
    plt.show()

    '''
    3. Create an overlay of the center points found in objects.png from
    homework 8. 
    '''
    
    objects_url = "C:/Users/blin261/Desktop/DATA602/objects.png"
    np_array = misc.imread(objects_url)
    img = ndimage.gaussian_filter(np_array, 2)
    thres = img > img.mean()
    labels, count = ndimage.label(thres)
    center = ndimage.measurements.center_of_mass(img, labels, range(1, count))
    df1 = pd.DataFrame(center, columns = ["x","y", "z"])
    plt.scatter(df1["y"], df1["x"], color = 'red')
    plt.imshow(img)
    plt.show()

    '''
    4. Plot a line graph that shows the hour by hour change in number of server
    requests from the HTTP in homework 9.
    '''
    
    df2 = pd.read_csv("C:/Users/blin261/Desktop/DATA602/epa-http.txt",
    sep = "\s+", header = None, na_values = "-", names = ["host", "time", "request",
    "http_reply_code", "bytes"])

    df2["time"] = pd.to_datetime(df2["time"], format = "[%d:%H:%M:%S]")
    df2["hour"] = df2["time"].dt.hour
    hourly_request = df2.groupby("hour").size()
    hour = range(1, 25)
    df3 = pd.DataFrame.from_items([('x', hour), ('y', hourly_request)])
    plt.plot(df3["x"], df3["y"], 'ro-')
    plt.xlabel('Hour')
    plt.ylabel("HTTP Request")
    plt.show()

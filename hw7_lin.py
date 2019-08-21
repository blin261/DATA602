import numpy
import timeit
import time
import copy
import pandas as pd
import Tkinter
import tkFileDialog
from scipy.optimize import curve_fit
from scipy import stats

setup = '''
import numpy
from scipy.optimize import curve_fit
from scipy import stats


import pandas as pd
import Tkinter
import tkFileDialog
import copy


def load_file():
    root = Tkinter.Tk()
    root.withdraw()

    filename = tkFileDialog.askopenfilename(parent = root)
    raw_data = open(filename)
    brainandbody = pd.read_csv(raw_data, delimiter = ",")
    return brainandbody


def variance(data_frame, column):
    variance = 0
    mean = sum(data_frame[column]) / len(data_frame)
    variance = sum((data_frame[column] - mean) ** 2)/(len(data_frame) - 1)
    return variance    


def covariance(data_frame, x, y):
    covariance = 0
    x_mean = sum(data_frame[x]) / len(data_frame)
    y_mean = sum(data_frame[y]) / len(data_frame)

    covariance = sum((data_frame[x]  - x_mean) * (data_frame[y]  - y_mean))/(len(data_frame) - 1)
    return covariance


def linear_regression(data_frame, x, y):
    a = covariance(data_frame, x, y) / variance(data_frame, x)
    b = data_frame[y].mean() - a * data_frame[x].mean()
    print ("The linear regression model is y = %s * x + %s" % (a, b))


def func(x, a, b):
    return a * x + b


def scipy_curve(data_frame):
    x = data_frame["brain"]
    y = data_frame["body"]
    popt, pcov = curve_fit(func, x, y)
    print("The linear regression model is y = %s * x + %s" % (popt[0], popt[1]))


def scipy_stat(data_frame):
    x = data_frame["brain"]
    y = data_frame["body"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    print("The linear regression model is y = %s * x + %s" % (slope, intercept))


data = load_file()


#References:
#Least-Squares Method formula can be found here: https://en.wikiversity.org/wiki/Least-Squares_Method
'''


if __name__ == "__main__":

    n = 1
    t = timeit.Timer("x = copy.copy(data); linear_regression(x, 'brain', 'body')", setup = setup)
    print "Regular Linear Regression Model   ", t.timeit(n)

    t = timeit.Timer("x = copy.copy(data); scipy_curve(x)", setup = setup)
    print "Scipy Linear Regression(curve_fit)", t.timeit(n)

    t = timeit.Timer("x = copy.copy(data); scipy_stat(x)", setup = setup)
    print "Scipy Linear Regression (lingress)", t.timeit(n)
    



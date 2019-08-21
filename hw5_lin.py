import pandas as pd
import Tkinter
import tkFileDialog


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


if __name__ == "__main__":
    data = load_file()
    print data.head(10)
    linear_regression(data, "brain", "body")


#References:
#Least-Squares Method formula can be found here: https://en.wikiversity.org/wiki/Least-Squares_Method

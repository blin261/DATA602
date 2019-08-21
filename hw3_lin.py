'''Now that we are out of the review phase, you will be providing me with a complete program (no more templates).  Remember, I want to be able to run "Python yourprogram.py" and get the result.  The score will be determined not just on whether or not you get the proper output, but how you get there.

Write a software program that does all of the following:

Loads in the data from cars.data.csv.  The data can be stored anyway you choose, in any data structure you choose (probably a list of some kind).  The data should load on start-up by referencing a file path, or even better, a file picker dialog box.
In the main portion of your program you should run the following operations and print the result to the console (except number 4).  How you achieve this is up to you.  However, operations need to be performed on the data itself (don't hard code the solution).
Print to the console the top 10 rows of the data sorted by 'safety' in descending order
Print to the console the bottom 15 rows of the data sorted by 'maint' in ascending order
Print to the console all rows that are high or vhigh in fields 'buying', 'maint', and 'safety', sorted by 'doors' in ascending order.  Find these matches using regular expressions.
Save to a file all rows (in any order) that are: 'buying': vhigh, 'maint': med, 'doors': 4, and 'persons': 4 or more.  The file path can be a hard-coded location (name it output.txt) or use a dialog box.  
Your code needs to be able to handle exceptions.  It should handle all data as specified by the data definition document from Lesson 2, and throw some kind of error when it encounters data that doesn't match that format.  To test this, I will add the line 'vlow, vlow, 1, 1, vbig, vhigh' to the .csv file.  Your program should gracefully handle this line in all cases from the previous part.
Going forward, code style will count a little bit.  So make sure it is readable and I can understand it.  Also, there are a few ways you can approach this assignment.  Ideally, you will create functions that can return the data in different ways, not just do what I am asking for in part 2.  For example, consider if I asked for something in a different order, how hard would it be to make that change in your code?
'''

import re
import Tkinter
import tkFileDialog
import csv

class CarEvaluation:
    carCount = 0
    def __init__(self, buying, maint, doors, persons, lug_boot, safety, class_distribution):
        self.buying = buying
        self.maint = maint
        self.doors = doors
        self.persons = persons
        self.lug_boot = lug_boot
        self.safety = safety
        self.class_distribution = class_distribution
        CarEvaluation.carCount = CarEvaluation.carCount + 1

safety = {"low": 1, "med": 2, "high": 3}
maint = {"low": 1, "med": 2, "high": 3, "vhigh": 4}
doors = {"2": 1, "3": 2, "4": 3, "5more": 4}



def read_csv():
    root = Tkinter.Tk()
    root.withdraw()
    root.update()

    filename = tkFileDialog.askopenfilename(parent = root)
    car_list = []
    valid_data = []
    raw_data = open(filename)
    try:
        cars = csv.reader(raw_data, delimiter = ",")
        for car in cars:
            car_list.append(CarEvaluation(car[0],car[1],car[2],car[3],car[4],car[5],car[6]))

        raw_data = open(filename)
        cars = csv.reader(raw_data, delimiter = ",")
        valid_data = filter(lambda car: (car[0] == "vhigh" or "high" or "med" or "low")
                            and (car[1] == "vhigh" or "high" or "med" or "low")
                            and (car[2] == "2" or "3" or "4" or "5more")
                            and (car[3] == "2" or "4" or "more")
                            and (car[4] == "small" or "med" or "big")
                            and (car[5] == "low" or "med" or "high")
                            and (car[6] == "unacc" or "acc" or "good" or "vgood"), cars)
            
        if len(car_list) == len(valid_data):
            return car_list
        else:
            print len(car_list), len(valid_data)
            print ('csv contains invalid values')

    except IOError:
        print "Please enter a correct CSV file"



def sortbysafety(car_evaluation, order, rows):
    
    if order == "asc":
        if rows >= 0:
            temp = sorted(car_evaluation, key=lambda car: safety[car.safety])[0:row]
            for i in temp:
                print i.buying, i.maint, i.doors, i.persons, i.lug_boot, i.safety, i.class_distribution
        else:
            temp = sorted(car_evaluation, key=lambda car: safety[car.safety])[rows:]
            for i in temp:
                print i.buying, i.maint, i.doors, i.persons, i.lug_boot, i.safety, i.class_distribution

                                
    elif order == "desc":
        if rows >= 0:
            temp = sorted(car_evaluation, key=lambda car: safety[car.safety], reverse=True)[0:rows]
            for i in temp:
                print i.buying, i.maint, i.doors, i.persons, i.lug_boot, i.safety, i.class_distribution
        else:                                                   
            temp = sorted(car_evaluation, key=lambda car: safety[car.safety], reverse=True)[rows:]
            for i in temp:
                print i.buying, i.maint, i.doors, i.persons, i.lug_boot, i.safety, i.class_distribution



def sortbymaint(car_evaluation, order, rows):
                                
    if order == "asc":
        if rows >= 0:
            temp = sorted(car_evaluation, key=lambda car: maint[car.maint])[0:rows]
            for i in temp:
                print i.buying, i.maint, i.doors, i.persons, i.lug_boot, i.safety, i.class_distribution
        else:
            temp = sorted(car_evaluation, key=lambda car: maint[car.maint])[rows:]
            for i in temp:
                print i.buying, i.maint, i.doors, i.persons, i.lug_boot, i.safety, i.class_distribution

                                
    elif order == "des":
        if rows >= 0:
            temp = sorted(car_evaluation, key=lambda car: maint[car.maint], reverse=True)[0:rows]
            for i in temp:
                print i.buying, i.maint, i.doors, i.persons, i.lug_boot, i.safety, i.class_distribution
        else:
            temp = sorted(car_evaluation, key=lambda car: maint[car.maint], reverse=True)[rows:]
            for i in temp:
                print i.buying, i.maint, i.doors, i.persons, i.lug_boot, i.safety, i.class_distribution



def subset(car_evaluation, pattern, order):

    output = filter(lambda car: re.search(pattern, car.buying) and re.search(pattern, car.maint) and re.search(pattern, car.safety), car_evaluation)
    
    if order == "asc":
        temp = sorted(output, key=lambda car: doors[car.doors])
        for i in temp:
            print i.buying, i.maint, i.doors, i.persons, i.lug_boot, i.safety, i.class_distribution               
    elif order == "desc":
        temp = sorted(output, key=lambda car: doors[car.doors], reverse=True)
        for i in temp:
            print i.buying, i.maint, i.doors, i.persons, i.lug_boot, i.safety, i.class_distribution



def save_file(car_evaluation, dictionary):
    output = []
    for car in car_evaluation:
        sum = 0
        for key, value in dictionary.items():
            if getattr(car, key) == value:
                sum = sum + 1
            if sum == len(dictionary):                    
                output.append(car)
    root = Tkinter.Tk()
    root.withdraw()
    files = tkFileDialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    csv.writer(files).writerows(output)
    files.close()


 
if __name__ == "__main__":

    print ("**********Question 1**********")
    eval1 = read_csv()

    print ("**********Question 2a**********")
    sortbysafety(eval1, "desc", 10)

    print ("**********Question 2b**********")
    sortbymaint(eval1, "asc", -15)

    print ("**********Question 2c**********")
    subset(eval1, "high|vhigh", "asc")

    print ("**********Question 2d**********")
    dictionary = {"buying" : ["vhigh"], "maint":["med"], "doors":["4"], "persons": ["4", "more"]}
    save_file(eval1, dictionary)

    print ("**********Question 3**********")




    

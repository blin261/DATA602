#1. fill in this class
#   it will need to provide for what happens below in the
#	main, so you will at least need a constructor that takes the values as (Brand, Price, Safety Rating),
# 	a function called showEvaluation, and an attribute carCount
class CarEvaluation:
    carCount = 0
    def __init__(self, Brand, Price, SafetyRating):
        self.Brand = Brand
        self.Price = Price
        self.SafetyRating = SafetyRating
        CarEvaluation.carCount = CarEvaluation.carCount + 1
    def showEvaluation(self):
        print "The %s has a %s price and it's safety is rated a %s" % (self.Brand, self.Price, self.SafetyRating)
        
#2. fill in this function
#   it takes a list of CarEvaluation objects for input and either "asc" or "des"
#   if it gets "asc" return a list of car names order by ascending price
# 	otherwise by descending price
def sortbyprice(car_evaluation, order): #you fill in the rest
    result = []
    output = []
    low = [x for x in car_evaluation if x.Price == "Low"]
    med = [y for y in car_evaluation if y.Price == "Med"]
    high = [z for z in car_evaluation if z.Price == "High"]
    if (order == "asc"):
        result.extend(low)
        result.extend(med)
        result.extend(high)
        for n in result:
            output.append(n.Brand)
    elif(order == "des"):
        result.extend(high)
        result.extend(med)
        result.extend(low)
        for n in result:
            output.append(n.Brand)        
    return output
    #return a value
        
#3. fill in this function
#   it takes a list for input of CarEvaluation objects and a value to search for
#	it returns true if the value is in the safety  attribute of an entry on the list,
#   otherwise false
def searchforsafety(car_evaluation, value):#you fill in the rest
    for n in car_evaluation:
        if (n.SafetyRating == value):
            return True
    return False
    #return a value
	
# This is the main of the program.  Expected outputs are in comments after the function calls.
if __name__ == "__main__":	
   eval1 = CarEvaluation("Ford", "High", 2)
   eval2 = CarEvaluation("GMC", "Med", 4)
   eval3 = CarEvaluation("Toyota", "Low", 3)

   print "Car Count = %d" % CarEvaluation.carCount # Car Count = 3

   eval1.showEvaluation() #The Ford has a High price and it's safety is rated a 2
   eval2.showEvaluation() #The GMC has a Med price and it's safety is rated a 4
   eval3.showEvaluation() #The Toyota has a Low price and it's safety is rated a 3

   L = [eval1, eval2, eval3]
   print sortbyprice(L, "asc"); #[Toyota, GMC, Ford]
   print sortbyprice(L, "des"); #[Ford, GMC, Toyota]
   print searchforsafety(L, 2); #true
   print searchforsafety(L, 1); #false


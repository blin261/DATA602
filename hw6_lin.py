import numpy
import timeit
import time
import copy

setup = '''
import numpy
import copy

def sortwithloops(input):
    output = list(input)
    for i in range(len(output)-1):
        for j in range(i, len(output)):
            if output [j] < output [i]:
                temp = output [j]
                output[j] = output [i]
                output [i] = temp
    return output

def sortwithoutloops(input):
    output = list(input)
    output.sort()
    return output

def sortwithnumpy(input):
    return numpy.sort(input)



def searchwithloops(input, value):
    for element in input:
        if element == value:
            return True
        return False


def searchwithoutloops(input, value):
    if value in input:
        return True
    return False


def searchwithnumpy(input, value):
    output = input
    return numpy.any(output[:] == value)

L = [5,3,6,3,13,5,6]
nl = numpy.array(L);
'''

if __name__ == "__main__":
    n = 100000
    t = timeit.Timer("x = copy.copy(L); sortwithloops(x)", setup = setup)
    print "Sort With Loops:     ", t.timeit(n) 
    t = timeit.Timer("x = copy.copy(L); sortwithoutloops(x)", setup = setup)
    print "Sort Without Loops:  ", t.timeit(n)
    t = timeit.Timer("x = copy.copy(nl); sortwithnumpy(x)", setup = setup)
    print "Sort With Numpy:     ", t.timeit(n)


    t = timeit.Timer("x = copy.copy(L); searchwithloops(x, 13)", setup = setup)
    print "Search With Loops:   ", t.timeit(n)
    t = timeit.Timer("x = copy.copy(L); searchwithoutloops(x, 13)", setup = setup)
    print "Search Without Loops:", t.timeit(n)
    t = timeit.Timer("x = copy.copy(nl); searchwithnumpy(x, 13)", setup = setup)
    print "Search With Numpy:   ", t.timeit(n)
    


    






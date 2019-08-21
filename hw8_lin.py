'''
First, download the image package attached to this lesson.  On each image you will count the number of objects in the image and find their center points.
The images in order of complexity are circles.png, objects.png and peppers.png. Using Python's built-in functionality, scipy, or any other module, perform the following tasks:

Thresholding: First convert the image to a binary image.  This is done with a technique called thresholding, which is covered in the reading.  There are functions for it in scipy,
although it is very easy to do manually.  Essentially read each pixel and if it above a specified gray level make it white, otherwise make it black.
Count objects:  Count the number of objects in the image.  If you are interested in how this is done, refer to the additional readings.  An object will be a group of white pixels
surrounded by black pixels.  Doing this by hand is also fairly easy, but try to use functions found in the modules available.
Find center points: For each object, find the center point in terms of x,y coordinates.  As with part 3, you can do this directly, but it's better to use something from a module.


'''
import scipy.ndimage as ndimage
import scipy.misc as misc
import numpy as np
import skimage.filters as skif
import matplotlib.pyplot as plt


def threshold(directory, image_name, cutoff):
    np_array = misc.imread(directory)
    img = ndimage.gaussian_filter(np_array, cutoff)
    plt.imshow(img)
    plt.show()
    print "Type of Image: %s" % (type(img))
    print (img.shape)
    print "Type of Data: %s" % img.dtype
    print "Darkest Point: %s" % img.max()
    print "Lightest Point: %s" % img.min()
    thres = img > img.mean()
    misc.imsave(image_name, thres)

def adaptive_threshold(directory, image_name, block_size):
    np_array = misc.imread(directory, flatten = True)
    block_size = block_size
    plt.imshow(np_array)
    plt.show()
    adaptive_threshold = skif.threshold_local(np_array, block_size, method= 'mean', offset = 0)
    binary_threshold = np_array > adaptive_threshold
    misc.imsave(image_name, binary_threshold)

def count_objects(directory):
    np_array = misc.imread(directory)
    labels, count = ndimage.label(np_array)
    return labels, count

def get_center(directory):
    np_array = misc.imread(directory)
    labels, count = ndimage.label(np_array)
    centers = ndimage.measurements.center_of_mass(np_array, labels, range(1, count))
    return centers

if __name__ == "__main__":
    objects_url = "C:/Users/blin261/Desktop/DATA602/objects.png"
    circles_url = "C:/Users/blin261/Desktop/DATA602/circles.png"
    peppers_url = "C:/Users/blin261/Desktop/DATA602/peppers.png"

    print("-----------Regular Threshold----------")
    threshold(objects_url, "objects.png", 2)
    labels, count = count_objects(objects_url)
    print "The Number of Objects are %s" % (count)
    centers = get_center(objects_url)
    for i in range(0, count):
        print "Center of Mass %s:" % (i+1), centers[i - 1][0:2]


    print ("")    
    print ("----------Adaptive Threshold----------")
    adaptive_threshold(objects_url, "objects.png", 55)
    labels, count = count_objects(objects_url)
    print "The Number of Objects are %s" % (count)
    centers = get_center(objects_url)
    for i in range(0, count):
        print "Center of Mass %s:" % (i+1), centers[i - 1][0:2] 


    print ("")
    print("-----------Regular Threshold----------")
    threshold(circles_url, "circles.png", 2)
    labels, count = count_objects(circles_url)
    print "The Number of Circles are %s" % (count)
    centers = get_center(circles_url)
    for i in range(0, count):
        print "Center of Mass %s:" % (i+1), centers[i - 1][0:2]

    print ("")    
    print ("----------Adaptive Threshold----------")
    adaptive_threshold(circles_url, "circles.png", 55)
    labels, count = count_objects(circles_url)
    print "The Number of Circles are %s" % (count)
    centers = get_center(circles_url)
    for i in range(0, count):
        print "Center of Mass %s:" % (i+1), centers[i - 1][0:2]


    print ("")
    print("-----------Regular Threshold----------")
    threshold(peppers_url, "peppers.png", 2)
    labels, count = count_objects(peppers_url)
    print "The Number of Peppers are %s" % (count)
    centers = get_center(peppers_url)
    for i in range(0, count):
        print "Center of Mass %s:" % (i+1), centers[i - 1][0:2] 


# -*- coding: utf-8 -*-
"""
This program determines if a given 3 sides can create a valid triangle, and then 
classifies it as equilateral, isoceles, scalene, or right. 

@author: Samantha Inneo
"""

import unittest
from xml.etree.ElementTree import TreeBuilder     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    ''' Setting the variables in size order for ease later'''
    if a <= b and a <= c:
        newA = a
        if b <= c:
            newB = b
            newC = c
        else: 
            newB = c
            newC = b


    if b <= c and b <= a:
        newA = b
        if c <= a:
            newB = c
            newC = a
        else: 
            newB = a
            newC = c

    if c <= a and c <= b:
        newA = c
        if a <= b:
            newB = a
            newC = b
        else: 
            newB = b
            newC = a


    pyth = newA**2 + newB**2
    # Note: This code is completely bogus but demonstrates a few features of python
    if newA == newB == newC:
        return 'Equilateral'
    elif newA == newB or newB == newC or newA == newC:
        return 'Isoceles'
    elif pyth == newC**2:
        return 'Right'
    elif (newA + newB) < newC:
        return 'Scalene'
    else:
        return 'NotATriangle'
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Isoceles')
        

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    # runClassifyTriangle(10,10,10)
    
    #unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
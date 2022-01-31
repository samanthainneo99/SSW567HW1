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
    #print("A: " + str(newA) +  " B: " +str(newB) + " C: " + str(newC))

    #pyth = one side of pythagorean theorem to check if it is a right triangle later
    pyth = newA**2 + newB**2


    #Here, I am actually checking for the criteria of each type of triangle
    
    if (newA + newB) <= newC:
        return 'NotATriangle'
    elif newA == newB == newC:
        return 'Equilateral'
    elif (newA == newB) or newB == newC or newA == newC:
        return 'Isoceles'
    elif pyth == newC**2:
        return 'Right'
    elif (newA + newB) > newC:
        return 'Scalene'
    
       
    
        
        
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
        
    #I made this set to be all NotEqual
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertNotEqual(classifyTriangle(1,1,2),'Equilateral','1,1,2 should be NotATriangle')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertNotEqual(classifyTriangle(15,15,30),'Scalene', '10, 15, 30 should be Isosceles')

    def testMyTestSet3(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','12,12,12 should be equilateral')
        self.assertEqual(classifyTriangle(10,10,20),'NotATriangle','10,10,20 should be NotATriangle')
        self.assertEqual(classifyTriangle(10,10,100),'NotATriangle','10,10,20 should be NotATriangle')
        self.assertEqual(classifyTriangle(10,15,30),'NotATriangle', '10, 15, 30 should be NotATriangle')
        self.assertEqual(classifyTriangle(5,4,3),'Right', '3,4,5 should be Right')
        self.assertEqual(classifyTriangle(10,10,18),'Isoceles', '10, 10, 18 should be Isoceles')
        self.assertEqual(classifyTriangle(10,10,18),'Isoceles', '5.5, 5.5, 10 should be Isoceles')
        self.assertEqual(classifyTriangle(2,5,6),'Scalene','2,5,6 should be Scalene')
        self.assertEqual(classifyTriangle(2,5,6),'Scalene','2.5,5.5,6.5 should be Scalene')



        

if __name__ == '__main__':
    # examples of running the code
    # runClassifyTriangle(1,2,3)
    # runClassifyTriangle(1,1,1)
    #runClassifyTriangle(1,5,4)
    
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
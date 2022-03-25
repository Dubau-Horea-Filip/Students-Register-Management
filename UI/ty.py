"""
Write the specification, Python code and test cases for a recursive function that calculates the greatest common divisor
of the numbers found on odd positions of a list, using the divide and conquer method. For the input
[2, 35, 5, 65, 10, 20, 5] the greatest common divisor is between 35, 65 and 20 and its value is 5.
You may divide the implementation into several functions according to best practices. Specify and test all functions [4p].
"""

"""
specification: the function recevis as input a list that whold be divided in 2 lists until there are only 4 and then makes the gretest commen divefer between these 2 and sends it back trough recursive 

"""


def gcd(a, b):
    """
    gcd recives as parameters 2 numbers a and be and finds recursivly the greatest common devider by the method of succesive subtractions
    parameters: a and b
    returs:  the gcd of a and b
    """
    if a == 0 or b ==0 :
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


def devide (list):
    """
    the function takes a kist and devides it in 2 over and over again until we have list of 4 where we take the 2
    numbers in odd positions and maks the gcd between these 2 and then takes the results from the 2 parts and
    makes the gcd betten these 2 until we go all over the list
    :param list:
    :return: the gcd of the numbers on odd positions
    """
    if len(list) == 4:

        x= gcd(list[1],list[3])
        return x

    mid= len(list)//2
    part1= devide(list[:mid])
    part2= devide(list[mid:])
    y=gcd(part1,part2)
    return y

import unittest

class Test(unittest.TestCase):

    def test1(self):
        x=gcd(5,10)
        self.assertEqual(5,x)
        v=[1,5,2,10,3,15,4,20]
        y= devide(v)
        self.assertEqual(v,5)

x=Test()
x.test1()

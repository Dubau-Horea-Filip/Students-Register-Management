

def functie(n):
    '''
    the function checks if n is prime
    :param n : the nuber to be verifyed if is prime
    :return:  false if it isnt prime and true if it is
    '''
    d=2
    while d < n-1 and n%d >0:
     d+=1
    return d>=n-1

#PyUnit tests

import unittest

class Test(unittest.TestCase):
    def test(self):
        n=7

        self.assertTrue(functie(n))
        self.assertFalse(functie(6))
        self.assertEqual(True,functie(n))



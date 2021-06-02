import math
import unittest

def wallis(n):
    prod = 1
    for i in range(1,n+1):
        a = (4*(i**2))/((4*(i**2)) - 1)
        prod*=a
    return(2*prod)

from random import *
def monte_carlo(n):
    nod_circle = 0      # number of dots inside cirle
    nod_square = 0      # number of dots inside square
    for i in range(n):
        x = random()
        y = random()
        if (x**2 + y**2)<=1:
            nod_circle+=1
            nod_square+=1
        else:
            nod_square+=1

    return(4*nod_circle/nod_square)

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
@@ -28,27 +50,7 @@ def test_accuracy(self):
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


def wallis(n):
    prod = 1
    for i in range(1,n+1):
        a = (4*(i**2))/((4*(i**2)) - 1)
        prod*=a
    return(2*prod)

from random import *
def monte_carlo(n):
    nod_circle = 0      # number of dots inside cirle
    nod_square = 0      # number of dots inside square
    for i in range(n):
        x = random()
        y = random()
        if (x**2 + y**2)<=1:
            nod_circle+=1
            nod_square+=1
        else:
            nod_square+=1

    return(4*nod_circle/nod_square)
    
if __name__ == "__main__":
    unittest.main()

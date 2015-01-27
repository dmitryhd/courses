#!/usr/bin/env python2

import math
import unittest


def f(x):
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    step_number = int((stop - start)/step)
    amount = 0
    for step_num in range(step_number):
        amount += f(start + step_num*step)*step
    return amount


class TestRadiation(unittest.TestCase):
    def test_from_lecture(self):
        self.assertAlmostEqual(radiationExposure(0, 5, 1), 39.10318784326239)
        self.assertAlmostEqual(radiationExposure(5, 11, 1), 22.94241041057671)
        self.assertAlmostEqual(radiationExposure(0, 11, 1), 62.0455982538)
        self.assertAlmostEqual(radiationExposure(40, 100, 1.5), 0.434612356115)


if __name__ == '__main__':
    unittest.main()

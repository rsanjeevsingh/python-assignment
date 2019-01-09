'''
Title - Command Line Argument
Description  - This program will accept input from Command LIne
Program - 5
'''
from sys import argv

import Modules as mod

try:
    scriptName, a, b, c, d, e = argv
    print scriptName, '\n', a, '\n', b, '\n', c, '\n', d, '\n', e
    print "Largest Number among: ", a, b, c, 'is', mod.findLargestNumber.compareValues(a, b, c)

except ValueError, ex:
    print "Give at least 5 inputs", ex

except Exception, e:
    print "Unexpected error.", e

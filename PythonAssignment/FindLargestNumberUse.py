'''
Title - FindLargestNumberUse
Description - This program will find largest number
Program - #2,13
'''
import Modules as module

try:
    print ' Find Largest Number '
    comp = input('How many numbers would you like to compare? (By default 3 and Max. 5)?\n')
    if(comp>5):
        ex='Comparisions limit exceed'
        raise Exception(ex)

    a = input('Enter the value of a = ')
    b = input('Enter the value of b = ')
    c = input('Enter the value of c = ')
    d,e=0,0
    if(comp==4 or comp==5):
        d = input('Enter the value of d = ')
    if(comp==5):
        e = input('Enter the value of e = ')
    print 'Largest Number among ', a, b, c, d, e, 'is', module.findLargestNumber.compareValues(a, b, c, d, e)

except NameError, ex:
    print "You have entered a string value", ex

except Exception, ex:
    print "Unexpected error.", ex

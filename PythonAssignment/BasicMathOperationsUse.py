'''
    Title - Basic math operations
    Description - This program will perform basic math operations (including complex numbers) #use j
    Program #1,9
'''

import Modules as module

try:
        print ' Basic Math Operations '
        a=input('Enter the value of a = ')
        b=input('Enter the value of b = ')

        print 'Addition of ',a,'and',b,'=',module.mathOperations.addition(a,b)
        print 'Subtraction of ',a,'and',b,'=',module.mathOperations.subtraction(a,b)
        print 'Multiplication of ',a,'and',b,'=',module.mathOperations.multiplication(a,b)
        print 'Division of ',a,'and',b,'=',module.mathOperations.division(a,b)

except NameError, e:
    print "You have entered a string value", e

except ZeroDivisionError, e:
    print "Cannot divide a number by 0 ", e

except Exception,e:
    print "Unexpected error.",e


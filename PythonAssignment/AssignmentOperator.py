'''
Title - Assignment Operators
Description - This program will perform Addition, Subtraction, Multiplication, Division, Modulus, Exponent and Floor Division operations.
Program - 10
'''
try:
    a = 50
    b = 40
    c = 0

    c += a
    print "Addition ", c

    b -= a
    print "Subtraction ", b

    c *= a
    print "Multiplication", c

    c /= a
    print "Division ", c

    c = 2
    c %= a
    print "Modulus ", c

    c **= a
    print "Exponenet ", c

    c //= a
    print "Floor Division", c

except Exception, ex:
    print 'Unexpected error.', ex

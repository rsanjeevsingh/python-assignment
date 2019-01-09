'''
Title - Bitwise Operators
Description - This program will all bitwise operators present in Python.
Program - 11
'''
try:

    a = 30
    b = 20
    c = 0

    c = a & b;
    print "Bitwise AND ", c

    c = a | b;
    print "Bitwise OR ", c

    c = a ^ b;
    print "Bitwise XOR ", c

    c = ~a;
    print "Bitwise One's complement ", c

    c = a << 2;
    print "Binary left shift ", c

    c = a >> 2;
    print "Binary right shift ", c

except Exception,ex:
    print 'Unexpected error',ex
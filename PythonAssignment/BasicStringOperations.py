'''
Tilte - Basic String Operaitons
Description - This program will perform basic string operations like printing each character seperately, slicing etc
Program - 6
'''
try:
    str=raw_input("Please enter a string: ")
    print 'Print each character seperately'
    for x in str:
        print x
    print 'Slicing the input string...'
    print str[0:len(str)/2],'\n',str[len(str)/2:-1]

    print "Repeat string 100 times"
    print str*100

    print "Concatenation operation..."
    a=raw_input("Input string 1: ")
    b = raw_input("Input string 2: ")
    print a+b

except TypeError, ex:
    print "Please check the input", ex

except Exception, ex:
    print "Unexpected error.", ex

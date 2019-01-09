''''
    Title: Odd Even
    Description: This program will find whether the given input number is an odd number or an even number.
    Program - 3
'''

try:
    num=input('Enter any number: ')
    if(num%2==0):
        print num,' is an even number'
    else:
        print num, ' is an odd number'

except NameError, ex:
    print "You have entered a string value", ex

except Exception, ex:
    print "Unexpected error.", ex
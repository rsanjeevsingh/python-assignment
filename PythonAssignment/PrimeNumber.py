'''
Tilte : Prime Number
Description : This program will check whether the given input number is prime number or not
Program - 4
'''
try:
    num = input('Enter a positive number: ')
    if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print num,'is not a prime number'
                    break
            else:
                print num,'is a prime number'
    else:
        print num, 'is not a prime number'

except NameError, ex:
    print "You have entered a string value", ex

except Exception, ex:
    print "Unexpected error.", ex
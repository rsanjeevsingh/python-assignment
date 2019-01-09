'''
           Tilte : Prime Number in Range
           Description : This program will return prime numbers between 1 and given input
           Program - 16
'''
try:
    a = input('Enter a positive number: ')
    if a > 1:

        for num in range(1, a + 1):

            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print num
    else:
        print a, 'is not a prime number'

except NameError, ex:
    print "You have entered a string value", ex

except Exception, ex:
    print "Unexpected error.", ex

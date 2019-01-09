'''
Title - Smallest LArgest
Description - This porgram will find max and min value using funitons
Program #17
'''

try:
    print('Find smallest and largest number')
    number = raw_input('Enter number:')
    numbers = []
    while number!= '':
        numbers.append(int(number))
        number = raw_input('Enter number:')

    print 'Max value in ',numbers,'is',max(numbers)
    print 'Min value in ',numbers,'is',min(numbers)

except ValueError,e:
    print 'Enter a numeric value',e
except Exception,e:
    print 'Unexpected error',e
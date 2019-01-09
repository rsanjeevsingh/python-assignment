'''
Tilte : Find Largest Number
Description : This program will find the largest of given input numbers
'''

class findLargestNumber:
    @classmethod
    def compareValues(self,a,b,c,d=0,e=0):
        if (a > b and a > c and a > d and a > e):
            return a
        elif (b > a and b > c and b > d and b > e):
            return b
        elif (c > a and c > b and c > d and c > e):
            return c
        elif (d > a and d > b and d > c and d > e):
            return d
        else:
            return e




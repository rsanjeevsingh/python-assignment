'''
Tilte - Basic Tuple Operaitons
Description - This program will perform basic tuple operations like printing each element of list seperately, slicing etc
Progrm - 8
'''
from __future__ import print_function
try:
    tup=(10,20,30,40,50,60,70,80,90,100)
    print('Print tuple elements in new line...')
    print(*tup,sep="\n")
    print('Slicing operation on tuple...')
    print (tup[1:3])
    print('Repetition tuple..')
    print (tup*3)
    tup1 = ['a', 'b', 'c', 'd', 'e', 'f']
    print ('concatenation of tuple')
    print (tup+tup1)

except Exception, ex:
    print('Unexpected exception',ex)
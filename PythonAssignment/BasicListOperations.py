'''
Tilte - Basic LIST Operaitons
Description - This program will perform basic list operations like printing each element of list seperately, slicing etc
Prgram - 7
'''
from __future__ import print_function
try:
    lst=[10,20,30,40,50,60,70,80,90,100]
    print('Print list elements in new line...')
    print(*lst,sep="\n")
    print('Slicing operation on list...')
    print (lst[1:3])
    print('Repetition list..')
    print (lst*3)
    lst1 = ['a', 'b', 'c', 'd', 'e', 'f']
    print ('concatenation of lists')
    print (lst+lst1)

except Exception, ex:
    print('Unexpected exception',ex)
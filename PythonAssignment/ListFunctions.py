''''
Title - List Functions
Description -This program will demonstrate few functions related to list
Program - 14,15
'''

class listFunction:
    def displayElementList(self,x,y,index):
        return x[index],y[index]

    def repeatList(self,x,times):
        return x*times

    def concatenateList(self,x,y):
        return x+y

empList=['Emp1','Emp2','Emp3','Emp4','Emp5','Emp6','Emp7','Emp8','Emp9','Emp10',]
empNum=['000','001','002','003','004','005','006','007','008','009']

try:
    print 'Employee list contains: ',empList
    index=input('Enter index values in between 0-9: ')
    ob=listFunction()
    print 'Emp name and number:',ob.displayElementList(empList,empNum,index)
    print 'Emp names from 4th to 9th positon',empList[4:9]
    print 'Emp names from 3rd to last position',empList[3:]
    times=input('How many times do you want to repeat list?')
    print ob.repeatList(empList,times)
    print 'Concatenate list: ',ob.concatenateList(empList,empNum)

    for x in range(len(empList)):
        print empList[x],empNum[x]

    print 'Check if Emp2 exist in list - Using member operator'
    if 'Emp2' in empList:
            print 'Exist'
    else:
            print 'Does not exist'

    print 'Without using member operator'
    for x in empList:
        if('Emp2'==x):
            print 'Exist'

    print 'List in reverse order',empList[::-1]

except NameError, e:
    print 'Input a number.',e
except SyntaxError, e:
    print 'Input cannot be blank',e
except Exception,e:
    print 'Unexpected error',e

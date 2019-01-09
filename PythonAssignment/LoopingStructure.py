'''
Title - Looping Structure
Program - 18,19,20
'''
try:

    print 'Numbers ranging between 1 to 100 using for loop'
    for i in range(1,101):
        print i
    print 'Numbers ranging between 100 to 1 using for loop'
    for i in range(100,0,-1):
        print i
    print 'Numbers ranging between 1 to 100 using while loop'
    i=1
    while i<101:
        print i
        i+=1
    print 'Numbers ranging between 100 to 1 using while loop'
    i=100
    while i>0:
        print i
        i -= 1

    mystring="Hello world"
    print '\nPrint each character of Hello World in seperate line:\n'
    l=len(mystring)
    for i in range(l):
        print mystring[i]


    print '\n\n\n ++++++++++++++++++++ Print Even Numbers - Using For Loop +++++++++++++++++++++++++++++ '

    print '\nUse of break - For Loop\n'
    for i in range(1,101):
        if(i%2==0):
            if(i==50):
                break
            print i
            pass

    print '\nUse of continue - For loop \n'
    for i in range(1, 101):
        if (i % 2 == 0):
            if (i == 10 or i == 20 or i == 30 or i == 40 or i==50):
                continue
            print i
            i+=1
            pass

    print '\n\n\n ++++++++++++++++++++ Print Even Numbers - Using While Loop +++++++++++++++++++++++++++++ '

    print '\nUse of break - while Loop\n'
    i=1
    while i<101:
        if (i % 2 == 0):
            if (i == 90):
                break
            print i
            pass
        i+=1

    print '\nUse of continue - while loop \n'
    i=1
    while i<101:
        if (i % 2 == 0):
            if (i == 60 or i == 70 or i == 80 or i == 90):
                i+=1
                continue
            print i
            pass
        i+=1

    print '+++++++++++++ Filbonacci Series ++++++++++++++'

    n = int(input("How many terms? "))
    n1 = 0
    n2 = 1
    count = 0

    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto", n, ":")
        print(n1)
    else:
        print("Fibonacci sequence upto", n, ":")
        while count < n:
            print n1
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

except Exception,e:
    print 'Unexpected error',e
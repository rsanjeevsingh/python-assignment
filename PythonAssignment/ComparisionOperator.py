'''
Title - Comparision OPerator
Description - This program will find average of given input numbers
Program - 12

'''
try:

    num = int(input('How many numbers: '))
    total_sum = 0
    lst=[]
    for n in range(num):
        numbers = float(input('Enter number : '))
        lst.append(numbers)
        total_sum += numbers
    avg = total_sum/num
    print('Average of ', num, ' numbers is :', avg)

    gr=0
    val_gr=[]
    lr=0
    val_lr=[]
    eq=0
    val_eq=[]

    for a in lst:
        if(a>avg):
            gr+=1
            val_gr.append(a)
        elif(a<avg):
            lr+=1
            val_lr.append(a)
        elif(a==avg):
            eq+=1
            val_eq.append(a)

    print 'Total values Less than average: ',lr,val_lr
    print 'Total values greater than average: ',gr,val_gr
    print 'Total values equal to average: ',eq,val_eq


except NameError, e:
    print "You have entered a string value", e

except ZeroDivisionError, e:
    print "Cannot divide a number by 0 ", e

except Exception,e:
    print "Unexpected error.",e
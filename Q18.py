#18. Input a n and print even ns up to that n

def evenRec(num):
    if (num>0 and num%2==0):
        print(num)
        evenRec(num-2)
    elif(num>0 and num%2!=0):
        #print(num-1)
        evenRec(num-1)



#main
num=eval(input("Input n: "))
evenRec(num)
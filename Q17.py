#17. Input a n and Print ns up to that n in reverse

def recFun(num):
    if (num>0):
        print(num)
        recFun(num-1)

#main
num=eval(input("Enter limit: "))
print("\n")
recFun(num)

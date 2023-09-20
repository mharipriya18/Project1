a=int(input("Enter a num:"))
count=0
if a>0:
    for i in range(1,a+1):
        if(a%i==0):
            count=count+1
    if count==2:
        print("It is a prime nos")
    else:
        print("It is not a prime nos")

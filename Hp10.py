x=int(input("Enter my_age:"))
y=int(input("Enter your_age:"))
z=x-y
if x-y==1 or y-x==1:
    print("1 year difference between myage and yourage")
if x-y==0 or y-x==0:
    print("You both are same age")
if x-y>=2 or y-x>=2:
    print(z,"years difference between myage and yourage")

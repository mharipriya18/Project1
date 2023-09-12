m1=int(input("Tamil:"))
m2=int(input("English:"))
m3=int(input("Maths:"))
m4=int(input("Physics:"))
m5=int(input("Chemistry:"))
m6=int(input("Computer Science:"))
tot=m1+m2+m3+m4+m5+m6
avg=tot/6
print("The total is:",tot)
print("The percentage is:",avg)
if m1>=40 and m2>=40 and m3>=40 and m4>=40 and m5>=40 and m6>=40:
    res="PASS"
else:
    res="FAIL"
print("Result:",res)
if res=="PASS" and avg>=85:
    print("You secured A grade")
elif res=="PASS" and avg>=75:
    print("You secured B grade")
elif res=="PASS" and avg>=65:
    print("You secured C grade")
elif res=="PASS" and avg>=41:
    print("You secured D grade")
else:
    print(":( You failed in this exam")
                
        

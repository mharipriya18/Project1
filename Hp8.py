m1=int(input("Tamil mark:"))
m2=int(input("English mark:"))
m3=int(input("Maths mark:"))
m4=int(input("Physics mark:"))
m5=int(input("Chemistry:"))
m6=int(input("Computer Science mark:"))
if m1<m2 and m1<m3 and m1<m4 and m1<m5 and m1<m6:
    print("Minimum mark is:",m1)
elif m2<m3 and m2<m4 and m2<m5 and m2<m6:
    print("Minimum mark is:",m2)
elif m3<m4 and m3<m5 and m3<m6:
    print("Minimum mark is:",m3)
elif m4<m5 and m4<m6:
    print("Minimum mark is:",m4)
elif m5<m6:
    print("Minimum mark is:",m5)
else:
    print("Minimum mark is:",m6)

if m1>m2 and m1>m3 and m1>m4 and m1>m5 and m1>m6:
    print("Maximum mark is:",m1)
elif m2>m3 and m2>m4 and m2>m5 and m2>m6:
    print("Maximum mark is:",m2)
elif m3>m4 and m3>m5 and m3>m6:
    print("Maximum mark is:",m3)
elif m4>m5 and m4>m6:
    print("Maximum mark is:",m4)
elif m5>m6:
    print("Maximum mark is:",m5)
else:
    print("Maximum mark is:",m6)
if(m1>100):
    print("Tamil mark is invalid:",m1)
if(m2>100):
    print("English mark is invalid:",m2)
if(m3>100):
    print("Maths mark is invalid:",m3)
if(m4>100):
    print("Physics mark is invalid:",m4)
if(m5>100):
    print("chemistry mark is invalid:",m5)
if(m6>100):
    print("Computer science mark is invalid:",m6)


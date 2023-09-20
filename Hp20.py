salary=[25000,35000,40000,30000,50000,60000,70000,800000,96000,50500]
midval=int(len(salary)/2)
#print(salary[midval])
sum=0
for i in range(midval):
    sum1=sum+salary[i]
    for j in range(midval,len(salary)):
        sum2=sum+salary[j]
if sum1>sum2:
    print(sum1,"is greater than second half")
else:
    print(sum2,"is greater than first half")
        

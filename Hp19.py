a=[12,56,43,99,32,46,89,22,42,75,97,24,75]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)

a=[12,56,43,99,32,46,89,22,42,75,97,24,75]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)

words=["apple","orange","guava","banana","kiwi","pineapple","pappaya","cherry","date"]
for i in range(len(words)):
    for j in range(i+1,len(words)):
        if words[i]>words[j]:
            words[i],words[j]=words[j],words[i] 
print(words)

words=["apple","orange","guava","banana","kiwi","pineapple","pappaya","cherry","date"]
for i in range(len(words)):
    for j in range(i+1,len(words)):
        if words[i]<words[j]:
            words[i],words[j]=words[j],words[i] 
print(words)








n=int(input("Enter the number of elements = "))
print("Enter list elements= ",end=" ")
a=list(map(int,input().strip().split()))[:n]
i=int(input("Enter the 1st index = "))
j=int(input("Enter the 2nd index = "))
# temp=a[j]
# a[j]=a[i]
# a[i]=teamp
a[i],a[j]=a[j],a[i] 
for item in a:
    print(item,end=" ")
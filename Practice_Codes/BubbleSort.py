def BubbleSort(a):
    n=len(a)
    i=0
    j=0
    for i in range(0,n):
       for j in range(0,n-i-1):
           if a[j]>a[j+1]:
               temp=a[j+1]
               a[j+1]=a[j]
               a[j]=temp
    return a  # Return the sorted list

##main
n=int(input('Enter the number = '))
a=list(map(int,input().strip().split()))[:n]
a=BubbleSort(a)
for i in a:
    print(i,end='')  # Print each element in the sorted list

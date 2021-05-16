a=[]
b=[]
c=[]
n1 = int(input("Enter number of elements of first list : "))
print("Enter the Elements")
for i in range(0, n1):
    element1 = int(input())
    a.append(element1)
    if(a[i]>0):
        c.append(a[i]) 
n2 = int(input("Enter number of elements of second list : "))
print("Enter the Elements")
for i in range(0, n2):
    element2 = int(input())
    b.append(element2)
    if(b[i]>0):
        c.append(b[i])
print("The total Positive Numbers in the two lists are :",c)
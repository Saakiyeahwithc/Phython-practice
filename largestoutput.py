list=[]
n=int(input("enter the number of elements of list:"))
for i in range(0,n):
 l=int(input())
 list.append(l)
print(list)
print("the largest element of this list is=",max(list))
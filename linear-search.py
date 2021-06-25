list=[]
n=int(input("Enter the number="))
for i in range(1,n+1):
    a=int(input())
    list.append(a)
print(list)
b=int(input("Enter the number you want a search="))
count=0
for i in range(len(list)):
    if(b==list[i]):
        count=i+1
print("The number you are searching for is",b,"at position",count)


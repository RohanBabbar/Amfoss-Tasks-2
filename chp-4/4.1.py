list1 = []
print("Enter the number of elements")
a = int(input())
for i in range(a):
    print("Enter Elements")
    b = input()
    list1.append(b)
c = len(list1)
print(c)
for i in range(0,c):
    if(i==(c-1)):
        print(list1[i])
    elif(i!=(c-2)):
        print(list1[i],end=',')
    else:
        print(list1[i],"and ",end="")        
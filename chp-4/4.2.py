import random
def rand(list):
    list=['Heads','Tails']
    jam = random.choice(list)
    return jam
list1=[]    
z = 0
k = 0
for i in range(10):
    jam=rand(list)
    list1.append(jam)
    for j in range(len(list1)):
        if list1[j] == list1[j+1]:
            z =+1
        else:
            z = 0
        if z>=6:
            k=1
            break
# if list1[0]==list1[1]:
#     print('good')
print(list1) 
print(z)  

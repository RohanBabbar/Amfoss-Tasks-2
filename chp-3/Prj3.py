def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print((3*number)+1)
        return 3*number+1
print("Enter an integer")
a=int(input())
c=0
while True:
    if c==0:
        g= collatz(a)
    c=c+1
    if c>0:
        g= collatz(a)
    if g==1:
        break        
    

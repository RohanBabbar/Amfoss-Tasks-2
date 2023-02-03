import random
import time
# import select
totalquestions = 3
i = 0
correct = 0
for question in range(1,totalquestions+1):
    x = random.randint(0,9)
    y = random.randint(0,9)
    print('#%s: %s x %s = ' % (question, x, y))
    try:
        # a = int(input())
        # time.sleep(3)
        while i<3:
            t1 = time.time()
            a = int(input())
            t2 = time.time()
            t = t2-t1
            if t>8:
                print("Out of time")
                break
            elif a == x*y:
                print("Correct")
                correct +=1
                time.sleep(1)
                break
            else:
                print("Wrong")
            i+=1
            break
    except:
        print('Wrong Input')
print("Your Score : %s / %s" % (correct,totalquestions))
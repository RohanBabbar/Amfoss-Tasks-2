grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
NewList=[]
for i in range(6):
    for j in range(9):
        a = grid[j][i]
        NewList.append(a)
    # print("\n")
        # k=0
        # for k in range(9*k):
        #     NewList.insert(k," ")
for k in range(len(NewList)):
    if k%10==0:
        NewList.insert(k,"\n")     
print(''.join(NewList))    
# a = ['1','2','3','4','5']
# print(''.join(a))s
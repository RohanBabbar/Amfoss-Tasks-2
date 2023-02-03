tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(data):
    mxl=[]
    for i in range(len(data)):
        max_len = 1
        for ele in data[i]:
            if len(ele)>max_len:
                max_len = len(ele)
              
        mxl.append(max_len)
    for i in range(len(data[0])):
        for j in range(len(data)):
            # x=0
            print(data[j][i].rjust(mxl[j]), end=' ')
        print("\n")
    
            
printTable(tableData)

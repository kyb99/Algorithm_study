# 08-02 study
from pprint import pprint
# 직사각형이 차지하는 면적

sqr = [list(map(int,input().split())) for _ in range(4)]

blank = [[0]*100 for _ in range(100)]
print(sqr)

count = 0

for s in sqr:
    for i in range(s[0],s[2]):
        for j in range (s[1],s[3]):
            if blank[i][j] == 0:
                blank[i][j] +=1
                count +=1
print(count)
            
    
# 15.	Print a number triangle pattern like this (for n = 4):
# 1
# 1 2
# 1 2 3
# 1 2 3 4


for i in range(1,4+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
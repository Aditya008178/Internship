# 13.	Print a right-angled triangle (same as earlier) using nested loops:
#    *
#   ***
#  *****
# *******

for i in range(4):
    for j in range(2*i+1):
        print("*",end=" ")
    print()
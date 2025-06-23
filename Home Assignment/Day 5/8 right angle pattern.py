# 8.	Print the following right-angle triangle pattern using a for loop:
#    *
#   ***
# *****
# *******
# Take a number n as input and print a triangle with n rows using *


num=int(input("Enter any number of rows: "))
for i in range(1,num+1):
    print("*" * (2*i-1))

# 14 Create a multiplication table from 1 to 5, like:
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 5 x 10 = 50

for i in range(1,6):
    print(f"Table of {i}")
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    
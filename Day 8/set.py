set1 = {1,2,3,4,}
set2 = {3,4,7,8}

print("Both set",set1.union(set2))
print("Set 1 and set 2 without common elements",set1.symmetric_difference(set2))
print("common elements of set1 and set 2",set1.intersection(set2))
print("Elements only in set 1 and not in set 2",set1-set2)
print("Elements only in set 2 and not in set 1",set2-set1)


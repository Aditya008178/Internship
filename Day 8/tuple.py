tup = ("Python","is","awesome")
length =[]

for word in tup:
    length.append(len(word))
     
print(tuple(length))

























ount_dict = {}

for i in tup:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

# Extract repeated numbers
repeated = [num for num, count in count_dict.items() if count > 1]

print("Repeated numbers:", repeated)
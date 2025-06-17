o_dict = {'a':1,'b':2,'c':1}
i_dict = {}
for k, v in o_dict.items():
    if v in i_dict:
        i_dict[v].append(k)
    else:
        i_dict[v] = [k]
print(i_dict)



# output:- {1:['a','c'],2:['b']}
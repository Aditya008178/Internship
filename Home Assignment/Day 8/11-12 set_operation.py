# 11.	Given:
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# Perform and print:
# •	Union of a and b
# •	Intersection of a and b
# •	Difference: a - b and b - a
# 12.	Remove an element from a set using remove() and discard().
# •	Try removing an element that doesn’t exist using both.]

#11
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union of a and b: ", a.union(b)) 
print("Intersection of a and b: ", a.intersection(b))
print("Difference of a and b: ", (a-b))
print("Difference od b anda: ", (b-a))


#12
demo_set = {10, 20, 30, 40, 50, 60, 70}
print("\nSet before removing a element :", demo_set)
demo_set.remove(20)
demo_set.discard(50)
print("Set after removing a element :", demo_set)


#demo_set.remove(50) #It will show an error. KeyError: 50
demo_set.discard(20) #Removing an element which does not exist in the set using discard()
                     #It does not show any error

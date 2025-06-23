# 7.	Write a function get_min_max(numbers) that:
# o	Accepts a list
# o	Returns a tuple (min, max)

def get_min_max(numbers):
    maxi = max(numbers)
    mini = min(numbers)
    return (maxi, mini) #or  return (max(numbers), min(numbers))

demo_list = [15, 65, 231, 5, 656, 532]
max_min_tuple = get_min_max(demo_list)
print(f"Maximum  value: {max_min_tuple[0]}") 
print(f"minimum value: {max_min_tuple[1]}")

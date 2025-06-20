# 3.	List Index Validation
# colors = ["red", "blue", "green"]
# o	Ask user to input an index and print the color at that index.
# o	Catch IndexError.

try:
    colors = ["red", "blue", "green"]
    index = int(input("Enter an index to get the color: "))
    print(f"The color at index {index} is {colors[index]}.")

except IndexError as e:
    print(f"IndexError: {e}")

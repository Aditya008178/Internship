# List Access and Conversion
# Instructions:
# Create a list: data = [10, 20, 30]
# Ask the user for an index.
# Access that index and convert it to a float.
# Catch both IndexError and ValueError

data = [10, 20, 30,]
try:
    index = int(input("Enter an index: "))
    value = data[index]
    float_value = float(value)
    print(f"The float valueis: {float_value}")
# except IndexError:
#     print("Index out of range")
# except ValueError:
#     print("Value cannot be converted to float")

except(IndexError , ValueError) as e:
    print("Index out of range",e)
    print("Value cannot be converted to float",e)
#if statement
# age = int(input("Enter Your age: "))
# if(age>18):
#    print("You are eligible for Driving License")

#if else statement
# age=int(input("Enter your age:"))
# if age>=18:
#    print("You are eligible for vote")
# else:
#   print("you are not eligible for vote")


     
# if-elif-else statement
# age=int(input("Enter your age:"))
# if age>=18:
#     print("You are eligible for vote") 
# elif:
#     print("you are not eligible for vote")
# else:
#     print("invalid input")


#Nested if statement

# x= int(input("Enter any number:"))
# if x>0:
#     if x%2==0:
#         print("Number is greater than 0 and Even")
#     else:
#         print("Number is greater than 0 and Odd")
    
# else:
#     print("Number is less than 0")

#graetest Number

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))

# if a>b and a>c:
#     print(f"{a} is greater number")
# elif b>a and b>c:
#     print(f"{b} is greater number")
# else:
#     print(f"{c} is greater number")

# Weather

# raining=input("Is raining: Yes/No: ")
# if raining=="yes":
#     print("Take umbrella")
# else:
#     print("wear sunglasses")


# grade calculator

# s1=int(input("Enter subject 1 mark: "))
# s2=int(input("Enter subject 2 mark: "))
# s3=int(input("Enter subject 3 mark: "))

# total=s1+s2+s3
# per= total/300*100

# print("\n  Result..")
# print(f"Subject 1 mark: {s1}")
# print(f"Subject 2 mark: {s2}")
# print(f"Subject 3 mark: {s3}")
# print(f"Total  mark: {total}")
# print(f"Percentage: {per}")

# if (per >= 80 and per<=100):
#     print("A grade")

# elif(per>= 60 and per<=79):
#     print("B grade")

# elif(per>=40 and per<=59):
#     print("C grade")

# else:
#     print("Fail")


#shopping bill

item_name = input("Enter a Product name : ")
quantity = int(input("Enter the Quantity of product : "))
price = float(input("Enter a price of product : "))

print("\n\n------ Shopping Bill------ ")

print("Product name: ",item_name)
print("Product Quantity: ",quantity)
print("Product price: ",price)

Total = quantity*price

discount= (Total/100)*10
t=Total-discount*0.18



print(f"Your bill is : {Total}")
print(f"Discount on Bill: {discount}")
print(f"Discounted Bill: {t}")
#print(f"GST on Bill: {gst}")
#print(f"Total Bill: {tb}")

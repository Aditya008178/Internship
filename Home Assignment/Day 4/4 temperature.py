# Part B: If-Elif-Else
# 4.	Take temperature as input and:
# o	If temp > 35, print "Too Hot"
# o	If 25–35, print "Normal Weather"
# o	If 15–24, print "Cool"
# o	Else, print "Too Cold"


temperature = float(input("Enter the temperature: "))

if temperature > 35:
    print("Too Hot")
elif temperature >= 25 and temperature <= 35:
    print("Normal Weather")
elif temperature >= 15 and temperature < 25:
    print("Cool")
else:
    print("Too Cold")

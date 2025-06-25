# 5.	Math Helper Class
# o	Create a class MathHelper with static methods:
# 	is_prime(num) – Returns True if the number is a prime.
# 	gcd(a, b) – Returns the greatest common divisor.
# 	lcm(a, b) – Returns the least common multiple.
# o	Test with different inputs.

class MathHelper:
    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        return (a * b) // MathHelper.gcd(a, b)
    
 
print(MathHelper.is_prime(48))  

print(MathHelper.gcd(48, 18))  

print(MathHelper.lcm(48, 18)) 


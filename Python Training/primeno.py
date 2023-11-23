# A python program to find if the input is a prime or not
#  In the context of checking for prime numbers, you only need to check potential divisors up to the square root of the number. 
#  If a number has a divisor greater than its square root, it must also have a corresponding divisor smaller than the square root.

user_input = int(input("Enter a number : "))

# conditions for a prime number
# 1. Greater than 2
# 2. Should not be zero
# 3. Should not be a product of 2 numbers where one is not 1

def is_prime(user_input):
    
    if user_input < 2 :
        return False
    
    for i in range(2, int(user_input ** 0.5) + 1):
        if user_input % i == 0:
            return False
    
    return True

answer = is_prime(user_input)

print(answer)
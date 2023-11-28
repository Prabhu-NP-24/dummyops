# A program to find the factorial of a number

user_input = int(input("Enter a number : "))

def factorial(user_input):
    
    if user_input == 0 or user_input == 1 :
        return 1
    
    else : 
        
        fac = user_input * factorial(user_input - 1)
        return fac

print(factorial(user_input))
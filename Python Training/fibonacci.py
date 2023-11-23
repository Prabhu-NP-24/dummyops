# A program to generate the fibonacci series

user_input = int(input("Enter a number : "))

def fibonacci(user_input):
    
    # declare the first 2 variables of the fibonacci series    
    base_fibo = [0,1]
    
    while len(base_fibo) < user_input:
        
        # add the last 2 elements and add those till while loop ends
        base_fibo.append(base_fibo[-1] + base_fibo[-2])
    
    return base_fibo

fibo = fibonacci(user_input)

print(fibo)
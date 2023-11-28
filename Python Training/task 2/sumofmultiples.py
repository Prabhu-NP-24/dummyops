multiple = int(input("Enter the chosen multiple : "))
limit = int(input("Enter the limit value : "))

def sum_of_multiples(multiple, limit):
    
    return sum(num for num in range(limit) if num % multiple == 0)

print(sum_of_multiples(multiple, limit))
user_input = int(input("Enter the Number : "))

def list_of_squares(user_input):
    
    squares_list = [x ** 2 for x in range(1, user_input)]
    return squares_list
    
print(list_of_squares(user_input))
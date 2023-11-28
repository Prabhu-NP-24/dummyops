# A program to check if a given phrase is a palindrome or not

user_input = input("Enter the phrase : ")

def is_palindrome(input):
    
    new = ''.join(car.lower() for car in input if car.isalnum())
    
    return new == new[:: -1]

print(is_palindrome(user_input))
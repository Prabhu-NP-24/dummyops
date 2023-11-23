# A program to check if a given phrase is a palindrome or not

user_input = input("Enter the phrase : ")

def is_palindrome(input):
    
    clean_phrase = ''.join(char.lower() for char in input if char.isalnum())
    
    return clean_phrase == clean_phrase[:: -1]

print(is_palindrome(user_input))
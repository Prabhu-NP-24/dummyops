from utility import *

# So my friend has given me a set of 30 numbers. He says that there is a sentence hidden in it. So generate a python code 
# to convert all 30 numbers into possible alphabets and group the alphabets into possible words and group the words into possible sentences.

user_input = input("Enter the numbers : ")

ransom = RansomNote()

# Step 1 : Convert the string of numbers to possible combinations
resulting_numbers = ransom.split_numbers_string(user_input)
print("Resulting numbers are ---> ",resulting_numbers)

# Step 2 : Convert the numbers to aplhabets
resulting_alphabets = ransom.numbers_to_alphabets(resulting_numbers)
print("Resulting alphabets are ---> ", resulting_alphabets)

# Step 3 : Generate word combinations
resulting_combos = ransom.generate_word_combinations(resulting_alphabets)
print(resulting_combos)


# Example usage:
#numbers_string = "2089"

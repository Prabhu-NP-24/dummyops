sentence = "tiubsjblksbavibfsjkbfvjebdfjvkdskjvkj"

# Initialize an empty dictionary to store occurrences
alphabet_count = {}

# Iterate through each character in the sentence
for char in sentence:
    # Check if the character is an alphabet
    if char.isalpha():
        # Convert the character to lowercase to make the count case-insensitive
        char = char.lower()

        # Update the count in the dictionary
        alphabet_count[char] = alphabet_count.get(char, 0) + 1

# Print the occurrences of each alphabet
for alphabet, count in alphabet_count.items():
    print(f"{alphabet}: {count}")

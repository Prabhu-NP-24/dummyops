import itertools

class RansomNote():

    def split_numbers_string(self, numbers_string):
        # Convert the string of numbers to possible combinations
        numbers = []
        i = 0

        while i < len(numbers_string):
            # Check if the current character is part of a two-digit number
            if i + 1 < len(numbers_string) and int(numbers_string[i:i+2]) <= 26:
                numbers.append(int(numbers_string[i:i+2]))
                i += 2
            else:
                # If not a two-digit number, consider it as a single-digit number
                numbers.append(int(numbers_string[i]))
                i += 1

        return numbers

    def numbers_to_alphabets(self, numbers):
        # Convert the numbers to alphabets
        alphabet_mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
                            11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
                            21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

        alphabets = [alphabet_mapping[num] for num in numbers]
        return alphabets
    
    def generate_word_combinations(self, shuffled_alphabets):
        # Convert the shuffled alphabets to a list
        alphabets_list = list(shuffled_alphabets)
        
        # Generate all possible permutations of the alphabets
        permutations = itertools.permutations(alphabets_list)
        
        # Convert each permutation to a string and add it to the list of combinations
        combinations = [''.join(permutation) for permutation in permutations]
        
        return combinations
    
    def sentence_to_numbers(self, sentence):
        # Convert a sentence into numbers 
        alphabet_mapping = {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
        numbers = [alphabet_mapping[char.upper()] for char in sentence if char.isalpha()]
        return numbers
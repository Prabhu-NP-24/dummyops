# A program to check if 2 words are anagrams 

word_1 = str(input("Enter the first word : "))
word_2 = str(input("Enter the second word : "))

def anagram(first, second):
    
    first_clean = ''.join(str.split(first))
    second_clean = ''.join(str.split(second))
    
    print(sorted(first_clean))
    print(sorted(second_clean))
    
    return sorted(first_clean) == sorted(second_clean)

def reverse_string(word):
    
    return word[:: -1]

print(anagram(word_1, word_2))

print(reverse_string(word_1))
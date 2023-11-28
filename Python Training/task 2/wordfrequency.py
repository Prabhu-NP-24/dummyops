user_sentence = str(input("Enter the Sentence : "))

def word_frequency(sentence):
    
    words = sentence.split()
    word_freq = {}
    
    for word in words :
        word_freq[word] = word_freq.get(word, 0) + 1
    
    return word_freq

print(word_frequency(user_sentence))
        
        
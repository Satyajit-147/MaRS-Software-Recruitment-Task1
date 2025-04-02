#Dictionary to store the morse code values as keys and the converted text as values
mydict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}

morse = input() #taskes in morse code input
words = morse.split('   ')  #splits the words
decoded_words = []

def Morseconverter(words): #function to decode the morsecode
    for word in words:
        letters = word.split()  #splits every letter in word
        decoded_word = ""  
    
        for letter in letters:
            decoded_word += mydict[letter]  #The value of the key(morseletter) is looked up in the dictionary
    
        decoded_words.append(decoded_word)  

    decoded_message = " ".join(decoded_words) 
    print(decoded_message)
Morseconverter(words)

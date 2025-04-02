#Dictionary to store letters as keys and numbers as values
mydict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
#Reverse dictionary (key of dictionary1->value of dictionary 2 and value of dictionary1->key of dictionary 2
reversedict = {value:key for key, value in mydict.items()}
message = input('Enter the text to be decrypted: ').upper() #Encryted message input
letters_encrypted = []
letters_decrypted = []
for char in message:
    letters_encrypted.append(char)
for letter in letters_encrypted:
    letters_decrypted.append(mydict[letter])
for index in range(len(letters_decrypted)):
    letters_decrypted[index] = letters_decrypted[index]-index-1
for index in range(len(letters_decrypted)):
    if letters_decrypted[index]<1:
        letters_decrypted[index]+=26 #If the index is lesser than 1, it is incremented by 26 to ensure that it falls under the range of alphabets
    letters_decrypted[index] = reversedict[letters_decrypted[index]]
print(''.join(letters_decrypted))

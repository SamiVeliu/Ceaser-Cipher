
shift = int(input('Enter a Shift'))
key_word = input('Enter A Word You want to Encrypt (In Capital) ')

letter1 = key_word[0] 
letter2 = key_word[1] 
letter3 = key_word[2] 
letter4 = key_word[3]

if shift >= 0 and shift <= 25:
    letter1 = (ord(letter1)) + shift
    letter2 = (ord(letter2)) + shift
    letter3 = (ord(letter3)) + shift
    letter4 = (ord(letter4)) + shift
    if letter1 > 90:
        letter1 = (letter1 - 26)
        

        
    if letter2 > 90:
        letter2 = (letter2 - 26)
        
        
    if letter3 > 90:
        letter3 = (letter3 - 26)
        
    if letter4 > 90:
        letter4 = (letter4 - 26)
    print(chr(letter1) + chr(letter2) + chr(letter3) + chr(letter4))
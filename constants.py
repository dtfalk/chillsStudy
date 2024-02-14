# define constants relating to background color and text color
backgroundColor = (1,1,1) 
textColor = (0, 0, 0) 


# getting the valid letters and numbers for user to enter for either 
# their name or their user number
def getValidChars():
    validLetters = []
    validNumbers = []
    
    # valid digits (0 - 9)
    for i in range(48, 58):
        validNumbers.append(chr(i))
        
    # valid lowercase letters (a - z)
    for i in range(97, 123):
        validLetters.append(chr(i))
        
    # valid uppercase letters (A - Z)
    for i in range(65, 91):
        validLetters.append(chr(i))
    
    return validLetters, validNumbers

# defining the valid letters and valid numbers as constants
validLetters, validNumbers = getValidChars()

# text to be shown during the study instructions screen
explanationText = 'instructions for the study go here. Press the "c" key to continue'
                


                        
    

 
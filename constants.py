from screeninfo import get_monitors

# define constants relating to background color and text color
background_color = (1,1,1) 
text_color = (0, 0, 0) 


# getting the valid letters and numbers for user to enter for either 
# their name or their user number
def get_valid_chars():
    valid_letters = []
    valid_numbers = []
    
    # valid digits (0 - 9)
    for i in range(48, 58):
        valid_numbers.append(chr(i))
        
    # valid lowercase letters (a - z)
    for i in range(97, 123):
        valid_letters.append(chr(i))
        
    # valid uppercase letters (A - Z)
    for i in range(65, 91):
        valid_letters.append(chr(i))
    
    return valid_letters, valid_numbers

# defining the valid letters and valid numbers as constants
valid_letters, valid_numbers = get_valid_chars()

# text to be shown during the study instructions screen
explanation_text = 'instructions for the study go here. Press the "c" key to continue'
                


                        
    

 
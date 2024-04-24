from psychopy import visual

# define constants relating to background color and text color
backgroundColor = 'white' 
textColor = 'black'
questionSelectedColor = 'red'

# text to be shown during the study instructions screen
explanationText = 'Thank you for taking the time to participate in our experiment.\n\n\
    In this experiment you will watch three videos.\n\n\
    Please press the SPACEBAR when you feel a chill.\n\n\
    Before each video you will see a cross in the middle of the screen for a few seconds.\n\n\
    Please focus on this cross while it is on the screen.\n\n\
    Press the "return" key when you are ready to proceed to your first video.'

# text for the exit screen
exitScreenText = 'Thank you for taking the time to participate in our study.\
    Please inform the experimenter that you are finished.\n\n\n\n\
    (For the experimenter: press the escape key to exit)'

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


# class for the buttons the user will see
class Button:

    instances = [] # keeps track of all instances of buttons

    # initializes an instance of a button
    def __init__(self, win, buttonType, text, i):

        # define the button and the text that goes with it
        winWidth, winHeight = win.size
        windowScale = winWidth / winHeight

        if buttonType == 'option': # creates a box to click and text for questionnaire options
            self.checkbox = visual.Rect(win, width=0.03, height=0.03 * windowScale, color = textColor, pos=(-0.6, 0.1 - 0.1 * i))
            self.text = visual.TextStim(win, text=text, color = textColor, alignText = 'left', pos=(0, 0.1 - 0.1 * i))
        else: # creates the submit button so the user may submit their response
            self.checkbox = visual.Rect(win, width=0.22, height=0.09 * windowScale, color = 'lightgray', pos=(0, -0.8))
            self.text = visual.TextStim(win, text=text, color = textColor, alignText = 'center', pos=(0, -0.8))
        
        self.checked = False # is the checkbox checked or not
        self.buttonType = buttonType # question option vs submit button
        self.instances.append(self) # add to the list of instances of buttons on the screen
        
    # handles button clicks
    def handleClick(self):
        if self.buttonType == 'option':
            self.checked = not self.checked # switch button state
            self.unselectOthers()
            if self.checked: # if selected, change color to red
                self.checkbox.color = questionSelectedColor
            else: # if unselected, change color to black
                self.checkbox.color = textColor 
            
    
    # unselects all other questions
    def unselectOthers(self):
        buttons = Button.instances
        for button in buttons:

            # don't unclick button just clicked or "unclick" the submit button
            if button == self or button.buttonType != 'option':
                continue

            # if something is already checked, then uncheck it
            if button.checked:
                button.checked = False
                button.checkbox.color = textColor
                


                        
    

 
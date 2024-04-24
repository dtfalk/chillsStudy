import os
from pylsl import StreamOutlet, StreamInfo
from psychopy import visual, core, event
import csv
import random
from constants import *

# =========================================================================
# the functions below are for initializing a lab streaming layer (LSL) outlet
# and for pushing samples (presses of the spacebar) to whatever LSL inlet
# we wind up creating
# =========================================================================

# Initializes lab streaming layer outlet
def initializeOutlet():
    infoEvents = StreamInfo(name = 'DataSyncMarker', type = 'Tags', channel_count = 1, 
                            nominal_srate = 0, channel_format ='string', source_id = '12345')
    outlet = StreamOutlet(infoEvents)
    return outlet


# pushes a sample from the LSL outlet to some TBD LSL inlet
def pushSample(outlet, tag):
    outlet.push_sample([tag])

# =========================================================================
# =========================================================================





# =========================================================================
# the functions below are for retrieving a SubjectID and a subject name
# =========================================================================

# gets the subject's name and subject number
def getSubjectInfo(win):
    # get subject name and subject number
    subjectName = getSubjectName(win)
    subjectNum = getSubjectNum(win)
    
    return subjectName, subjectNum
 

# gets the subject's name
def getSubjectName(win):
    namePrompt = 'Subject Name: '
    subjectName = ''
    
    while True:
        keys = event.getKeys()
        for key in keys:
            if key == 'escape':
                win.close()
                core.quit()
                return
            elif key == 'return':
                return subjectName
            elif key == 'backspace':
                if subjectName != '':
                    subjectName = subjectName[:-1]
            elif key == 'space':
                subjectName = subjectName + ' '
            elif key in validLetters:
                subjectName = subjectName + key
        prompt = visual.TextStim(win = win, text = namePrompt + subjectName, height = 0.2, color = textColor)
        prompt.draw()
        win.mouseVisible = False
        win.flip()


# gets the subjectID number
def getSubjectNum(win):
    numPrompt = 'Subject Number: '
    subjectNum = ''
    
    while True:
        keys = event.getKeys()
        for key in keys:
            if key == 'escape':
                win.close()
                core.quit()
                return
            elif key == 'return':
                return subjectNum
            elif key == 'backspace':
                if subjectNum != '':
                    subjectNum = subjectNum[:-1]
            elif key in validNumbers:
                subjectNum = subjectNum + key
        prompt = visual.TextStim(win = win, text = numPrompt + subjectNum, height = 0.2, color = textColor)
        prompt.draw()
        win.mouseVisible = False
        win.flip()

# =========================================================================
# =========================================================================





# =========================================================================
# the functions below are for handling the questionnaire given to users
# after each video.
# =========================================================================

# contains questionnaire questions and displays questionnaire to the subject
def questionnaire(win, mouse):
    win.mouseVisible = True

    # variables to hold all of the questions and their associated response options
    questionsTotal = []
    optionsTotal = []

    # question 1 text and response options
    question1 = visual.TextStim(win, text='How interested were you in this video? Please select an option and then click Submit.', wrapWidth= 1.5, pos=(0, 0.4), color = textColor)
    ResponseOptions1 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    questionsTotal.append(question1)
    optionsTotal.append(ResponseOptions1)

    # question 2 text and response options
    question2 = visual.TextStim(win, text='How chilling did you find this video? Please select an option and then click Submit.', wrapWidth= 1.5, pos=(0, 0.4), color = textColor)
    ResponseOptions2 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    questionsTotal.append(question2)
    optionsTotal.append(ResponseOptions2)

    # question 3 text and response options
    question3 = visual.TextStim(win, text='How intense were your chills from this video? Please select an option and then click Submit.', wrapWidth= 1.5, pos=(0, 0.4), color = textColor)
    ResponseOptions3 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    questionsTotal.append(question3)
    optionsTotal.append(ResponseOptions3)

    # question 4 text and response options
    question4 = visual.TextStim(win, text='How much did you enjoy this video? Please select an option and then click Submit.', wrapWidth= 1.5, pos=(0, 0.4), color = textColor)
    ResponseOptions4 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    questionsTotal.append(question4)
    optionsTotal.append(ResponseOptions4)

    # question 5 text and response options
    question5 = visual.TextStim(win, text='How emotional did you feel while watching this video? Please select an option and then click Submit.', wrapWidth= 1.5, pos=(0, 0.4), color = textColor)
    ResponseOptions5 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    questionsTotal.append(question5)
    optionsTotal.append(ResponseOptions5)

    # question 6 text and response options
    question6 = visual.TextStim(win, text='How likely would you be to watch this video again? Please select an option and then click Submit.', wrapWidth= 1.5, pos=(0, 0.4), color = textColor)
    ResponseOptions6 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    questionsTotal.append(question6)
    optionsTotal.append(ResponseOptions6)

    # question 7 text and response options
    question7 = visual.TextStim(win, text='How likely would you be to share this video? Please click an option and then click submit', wrapWidth= 1.5, pos=(0, 0.4), color = textColor)
    ResponseOptions7 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    questionsTotal.append(question7)
    optionsTotal.append(ResponseOptions7)

    # Final outcome will be a list of lists ("checkboxes") where each sublist is populated with
    # the options for that question ("Button" objects). 
    # 7 questions? Then checkboxes has 7 sublists. 
    # Question 1 has 5 options? Then len(checkboxes[0]) = 5.
    checkboxes = [] 
    for options in optionsTotal:
        curOptions = []
        for j, option in enumerate(options):
            curOptions.append(Button(win, 'option', option, j))
        checkboxes.append(curOptions.copy())
    
    submitButton = Button(win, 'submit', 'Submit', -1) # submit button
    data = [] # for storing answers to each question

    # iterate over each question and display to user
    for options, question in zip(checkboxes, questionsTotal):
        button_was_down = False # keep track if mouse was clicked in previous frame
        while True:
            for key in event.getKeys():
                if key == 'escape': # escape will exit the study
                    win.close()
                    core.quit()

            submitButton.checkbox.draw()
            submitButton.text.draw()
            question.draw() # display the question we show to the user
            current_button_down = mouse.getPressed()[0] # mouse state on current frame
            
            for option in options: # display each option (checkbox + text)
                option.checkbox.draw() # draw the checkbox
                option.text.draw() # draw the associated text
            
            # if the user clicks and releases within the checkbox
            if button_was_down and not current_button_down:
                for option in options: # option button clicks
                    if option.checkbox.contains(mouse.getPos()):
                        option.handleClick()

                if submitButton.checkbox.contains(mouse.getPos()): # submit button clicks
                    answerFound = False
                    for option in options:
                        if option.checked:
                            answerFound = True
                            data.append(option.text.text)
                            submitButton.handleClick()
                    if answerFound:
                        break
             
            button_was_down = current_button_down # update variables
            win.flip()
        win.flip()
    return data


# =========================================================================
# =========================================================================





# =========================================================================
# the functions below are for message screens (e.g. instructions)
# =========================================================================
        
# explains the experiment to the subject
def experimentExplanation(win):
    # text height and preparing the explanation text
    height = 0.07
    prompt = visual.TextStim(win = win, text = explanationText, height = height,
                            color = textColor, wrapWidth = 1.9, alignText = 'center')
    
    # wait for the user to press the "c" key before the experiment continues
    while True:
        keys = event.getKeys()
        for key in keys:

            # pressing escape exits the study
            if key == 'escape':
                win.close()
                core.quit()

            # pressing the "c" key lets the user progress to the videos
            if key == 'return':
                return
        
        # draw the prompt on the screen and display it to the user
        prompt.draw()
        win.mouseVisible = False
        win.flip()

# reminds the user of the instructions between each video
def reminderScreen(win):
    # text height and preparing the explanation text
    height = 0.07
    prompt = visual.TextStim(win = win, text = reminderText, height = height,
                            color = textColor, wrapWidth = 1.9, alignText = 'center')
    
    # wait for the user to press the "c" key before the experiment continues
    while True:
        keys = event.getKeys()
        for key in keys:

            # pressing escape exits the study
            if key == 'escape':
                win.close()
                core.quit()

            # pressing the "c" key lets the user progress to the videos
            if key == 'return':
                return
        
        # draw the prompt on the screen and display it to the user
        prompt.draw()
        win.mouseVisible = False
        win.flip()

# explains the experiment to the subject
def exitScreen(win):
    # text height and preparing the explanation text
    height = 0.07
    prompt = visual.TextStim(win = win, text = exitScreenText, height = height,
                            color = textColor, wrapWidth = 1.9, alignText = 'center')
    
    # wait for the user to press the "c" key before the experiment continues
    while True:
        keys = event.getKeys()
        for key in keys:
            # pressing escape exits the study
            if key == 'escape':
                win.close()
                core.quit()
        
        # draw the prompt on the screen and display it to the user
        prompt.draw()
        win.mouseVisible = False
        win.flip()

# Displays a fixation cross before each video
def fixationCross(win):
    waitTime = 3 # time that fixation cross is on the screen

    # variables for dimension of screen to properly draw/scale fixation cross
    width, height = win.size
    windowScale = width / height
    crossScale = 15

    # size/scaling/specifics of the fixation cross
    fixation = visual.ShapeStim(
        win=win, 
        vertices=((0, -1 * (windowScale / crossScale)), (0, windowScale / crossScale), (0,0), (-1 * (1 / crossScale),0), (1 / crossScale, 0)),  # Define the shape of a cross
        lineWidth = 10,
        closeShape = False,
        lineColor = "black")
    
    # drawing fixation cross
    fixation.draw()
    win.mouseVisible = False
    win.flip()

    # waits the specified amount of time before removing fixation cross and displaying the next video
    core.wait(waitTime)
    return

# =========================================================================
# =========================================================================



# =========================================================================
# the functions below are for presenting stimuli, saving data, or would fall
# into the "other" category relative to the categories of functions described
# above.
# =========================================================================

# randomly selects an unused category of videos and then randomly selects a video from that category
def selectVideo(Conditions):
    
    # stores current directory of the file and the path of stimuli folder where the videos are stored
    curDir = os.path.dirname(__file__)
    stimuliDir = os.path.join(curDir, 'stimuli')

    # variable to keep track of which stimuli have been used according to the "Conditions" dictionary
    unusedConditions = []

    # iterate over the three conditions in the "Conditions" dictionary to see which conditions have not been
    # used so we know which conditions we can randomly draw from
    for condition, used in Conditions.items():
        if not used:
            unusedConditions.append(condition)
    
    # randomly choose an unused condition from the list of unused conditions
    selectedCondition = random.choice(unusedConditions)

    # Given a condition, we randomly select one of the three videos from that condition 
    # (ask Gabe to give you access to the box folder with the videos and check the README to see how to create the file structure for the stimuli)
    selectedVideo = random.choice(os.listdir(os.path.join(stimuliDir, selectedCondition)))

    # create the final path for the selected video
    finalVideoPath = os.path.join(stimuliDir, selectedCondition, selectedVideo)

    # for the condition we selected the video from, set the associated dictionary entry to "True"
    # to reflect that the selected condition has been used
    Conditions[str(selectedCondition)] = True

    # print and return the path to the video (print statement is for testing purposes)
    print('\n\n\nFinal video Path: %s \n\n\n' %finalVideoPath)
    return finalVideoPath

# saves the timestamps of when the user pressed the spacebar
def saveTimestamps(subjectId, timestamps, videoName):
    # define our file paths for where we are going to store the subjec's responses to a questionnaire
    curDir = os.path.dirname(__file__)
    dataFolderPath = os.path.join(curDir, 'data')
    subjectDataFolderPath = os.path.join(dataFolderPath, subjectId)
    dataFilePath = os.path.join(subjectDataFolderPath, str(videoName) + 'Timestamps.csv')

    # create data folder if it does not exist
    if not os.path.exists(dataFolderPath):
        os.mkdir(dataFolderPath)
    
    # create subject's data folder if it does not exist
    if not os.path.exists(subjectDataFolderPath):
        os.mkdir(subjectDataFolderPath)

    # CSV header
    header = ['timestamps (seconds)']

    # write the header and the data to a CSV file in the "data" folder
    with open(file = dataFilePath, mode = 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for timestamp in timestamps:
            writer.writerow([timestamp])
    return

# for a given subject and video, save their responses to the questionnaire to a csv file in the "data" folder
def saveSubjectData(subjectName, subjectId, data, videoName):

    # define our file paths for where we are going to store the subjec's responses to a questionnaire
    curDir = os.path.dirname(__file__)
    dataFolderPath = os.path.join(curDir, 'data')
    subjectDataFolderPath = os.path.join(dataFolderPath, subjectId)
    dataFilePath = os.path.join(subjectDataFolderPath, str(videoName) + '.csv')

    # create data folder if it does not exist
    if not os.path.exists(dataFolderPath):
        os.mkdir(dataFolderPath)
    
    # create subject's data folder if it does not exist
    if not os.path.exists(subjectDataFolderPath):
        os.mkdir(subjectDataFolderPath)

    # CSV header
    header = ['name','question 1', 'question 2', 'question 3', 'question 4', 'question 5', 'question 6', 'question 7']

    # write the header and the data to a CSV file in the "data" folder
    with open(file = dataFilePath, mode = 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow([subjectName] + data)
    return


    
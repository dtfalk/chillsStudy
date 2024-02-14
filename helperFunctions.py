import os
from pylsl import StreamOutlet, StreamInfo
from psychopy import visual, core, event
import csv
from constants import *
import random

# =========================================================================
# the functions below are for initializing a lab streaming layer (LSL) outlet
# and for pushing samples (presses of the spacebar) to whatever LSL inlet
# we wind up creating
# =========================================================================

# Initializes lab streaming layer outlet
def initializeOutlet():
    infoEvents = StreamInfo('eventStream', 'events', 1, 0, 'string')
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
        win.flip()

# =========================================================================
# =========================================================================





# =========================================================================
# the functions below are for handling the questionnaire given to users
# after each video.
# =========================================================================

# contains questionnaire questions and displays questionnaire to the subject
def questionnaire(win):
    width, height = win.size
    windowScale = width / height

    # question 1 text and responses
    question1 = visual.TextStim(win, text='How interested were you in this video? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options1 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    optionStim1 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options1)]
    checkboxes1 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options1))]

    # question 2 text and responses
    question2 = visual.TextStim(win, text='How chilling did you find this video? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options2 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    optionStim2 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options2)]
    checkboxes2 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options2))]

    # question 3 text and responses
    question3 = visual.TextStim(win, text='How intense were your chills from this video? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options3 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    optionStim3 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options3)]
    checkboxes3 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options3))]

    # question 4 text and responses
    question4 = visual.TextStim(win, text='How much did you enjoy this video? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options4 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    optionStim4 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options4)]
    checkboxes4 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options4))]

    # question 5 text and responses
    question5 = visual.TextStim(win, text='How emotional did you feel while watching this video? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options5 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    optionStim5 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options5)]
    checkboxes5 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options5))]

    # question 6 text and responses
    question6 = visual.TextStim(win, text='How likely would you be to watch this video again? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options6 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    optionStim6 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options6)]
    checkboxes6 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options6))]

    # question 7 text and responses
    question7 = visual.TextStim(win, text='How likely would you be to share this video? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options7 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    optionStim7 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options7)]
    checkboxes7 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options7))]

    # overall variables for the multiple different questions
    questionsTotal = [question1, question2, question3, question4, question5, question6, question7]
    optionsTotal = [options1, options2, options3, options4, options5, options6, options7]
    optionStimsTotal = [optionStim1, optionStim2, optionStim3, optionStim4, optionStim5, optionStim6, optionStim7]
    checkboxesTotal = [checkboxes1, checkboxes2, checkboxes3, checkboxes4, checkboxes5, checkboxes6, checkboxes7]

    mouse = event.Mouse(win=win)
    selectedOption = None

    things = zip(questionsTotal, optionsTotal, optionStimsTotal, checkboxesTotal)
    data = []
    for question, options, optionStims, checkboxes in things:
        selectedOption = None
        while selectedOption is None:
            question.draw()
            for optionStim, checkbox in zip(optionStims, checkboxes):
                checkbox.draw()
                optionStim.draw()
            
        
            # Check for mouse clicks
            if mouse.getPressed()[0]:  # If the left mouse button is clicked
                for i, checkbox in enumerate(checkboxes):
                    if mouse.isPressedIn(checkbox):
                        clearCheckboxes(checkboxes)  # Clear all checkboxes (for single-selection)
                        checkbox.fillColor = 'black'  # Fill the clicked checkbox
                        selectedOption = i  # Save the selected option index
                        data.append(options[selectedOption])
                        break

            win.flip()
            core.wait(0.2)
    return data


# Function to clear all checkboxes (for single-selection logic)
def clearCheckboxes(checkboxes):
    for checkbox in checkboxes:
        checkbox.fillColor = None

# =========================================================================
# =========================================================================





# =========================================================================
# the functions below are for presenting stimuli, saving data, or would fall
# into the "other" category relative to the categories of functions described
# above.
# =========================================================================
        
# explains the experiment to the subject
def experimentExplanation(win):
    
    # text height and preparing the explanation text
    height = 0.07
    prompt = visual.TextStim(win = win, text = explanationText, height = height,
                            color = textColor, wrapWidth = 1.9, alignText = 'left')
    
    # wait for the user to press the "c" key before the experiment continues
    while True:
        keys = event.getKeys()
        for key in keys:

            # pressing escape exits the study
            if key == 'escape':
                win.close()
                core.quit()

            # pressing the "c" key lets the user progress to the videos
            if key == 'c':
                return
        
        # draw the prompt on the screen and display it to the user
        prompt.draw()
        win.flip()


# randomly selects an unused category of videos and then randomly selects a video from that category
def selectVideo(Conditions):
    
    # stores current directory of the file and the path of stimuli folder where the videos are stored
    curDir = os.path.dirname(__file__)
    stimuliDir = os.path.join(curDir, 'stimuli')

    # a dictionary that allows us to convert numbers to letters so we can do some math later on in
    # the function to randomly select a video
    numberToLetter = {
        '1' : 'a',
        '2' : 'b',
        '3' : 'c',
        '4' : 'd',
        '5' : 'e',
        '6' : 'f',
        '7' : 'g',
        '8' : 'h',
        '9' : 'i'
    }

    # variable to keep track of which stimuli have been used according to the "Conditions" dictionary
    unusedConditions = []

    # iterate over the three conditions in the "Conditions" dictionary to see which conditions have not been
    # used so we know which conditions we can randomly draw from
    for condition, used in Conditions.items():
        if not used:
            unusedConditions.append(condition)
    
    # randomly choose an unused condition from the list of unused conditions
    selectedConditionOld = random.choice(unusedConditions)

    # Translation of our selected condition's name into an integer (honestly cannot explain this well but it works)
    # (Something to do with indexing from zero in one case vs indexing from one in other cases)
    # (It has to do with the math in the line below and the "numberToLetter" dictionary above so we can randomly choose
    # a video from the selected condition)
    selectedCondition = int(selectedConditionOld.replace('condition', '')) - 1

    # Given a condition, we randomly select one of the three videos from that condition 
    # (ask Gabe to give you access to the box folder with the videos and check the README to see how to create the file structure for the stimuli)
    selectedVideo = str(numberToLetter[str((selectedCondition * 3) + random.randint(1,3))]) + '.mov.mp4'

    # create the final path for the selected video
    #finalVideoPath = os.path.join(stimuliDir, 'condition1', 'aTest.mov.mp4')
    finalVideoPath = os.path.join(stimuliDir, selectedConditionOld, selectedVideo)

    # for the condition we selected the video from, set the associated dictionary entry to "True"
    # to reflect that the selected condition has been used
    Conditions[str(selectedConditionOld)] = True

    # print and return the path to the video (print statement is for testing purposes)
    print('\n\n\nFinal video Path: %s \n\n\n' %finalVideoPath)
    return finalVideoPath


# Displays a fixation cross before each video
def fixationCross(win):

    # time that fixation cross is on the screen
    waitTime = 3

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
    win.flip()

    # waits the specified amount of time before removing fixation cross and displaying the next video
    core.wait(waitTime)
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
    
    
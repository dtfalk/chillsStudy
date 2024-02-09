import os
from pylsl import StreamOutlet, StreamInfo
from psychopy import visual, core, event
import csv
from constants import *
import random

# Initializes lab streaming layer outlet
def initialize_outlet():
    info_events = StreamInfo('event_stream', 'events', 1, 0, 'string')
    outlet = StreamOutlet(info_events)
    return outlet

# pushes a sample to the outlet
def push_sample(outlet, tag):
    outlet.push_sample([tag])
    
# gets the subject's name
# need to check if letter or alpha.
def get_subject_name(win):
    name_prompt = 'Subject Name: '
    subject_name = ''
    
    while True:
        keys = event.getKeys()
        for key in keys:
            if key == 'escape':
                win.close()
                core.quit()
                return
            elif key == 'return':
                return subject_name
            elif key == 'backspace':
                if subject_name != '':
                    subject_name = subject_name[:-1]
            elif key == 'space':
                subject_name = subject_name + ' '
            elif key in valid_letters:
                subject_name = subject_name + key
        prompt = visual.TextStim(win = win, text = name_prompt + subject_name, height = 0.2, color = text_color)
        prompt.draw()
        win.flip()

def get_subject_num(win):
    num_prompt = 'Subject Number: '
    subject_num = ''
    
    while True:
        keys = event.getKeys()
        for key in keys:
            if key == 'escape':
                win.close()
                core.quit()
                return
            elif key == 'return':
                return subject_num
            elif key == 'backspace':
                if subject_num != '':
                    subject_num = subject_num[:-1]
            elif key in valid_numbers:
                subject_num = subject_num + key
        prompt = visual.TextStim(win = win, text = num_prompt + subject_num, height = 0.2, color = text_color)
        prompt.draw()
        win.flip()
                
# gets the subject's name and subject number
def get_subject_info(win):
    
    # get subject name and subject number
    subject_name = get_subject_name(win)
    subject_num = get_subject_num(win)
    
    return subject_name, subject_num, win

# Returns user name, subject number, and path to where
# we will store their data.
def opening_screen(win):
    
    # file extenstion where we save data to
    extension = '.csv'
    
    # current directory
    cur_dir = os.path.dirname(__file__)
    
    # get user's name and user's subject number
    subject_name, subject_number, win = get_subject_info(win)
    
    
    return subject_name, subject_number

# explains the experiment to the subject
def experiment_explanation(win):
    
    # text height and preparing the explanation text
    height = 0.07
    prompt = visual.TextStim(win = win, text = explanation_text, height = height,
                            color = text_color, wrapWidth = 1.9, alignText = 'left')
    
    # wait for the user to press spacebar before the experiment continues
    while True:
        keys = event.getKeys()
        for key in keys:
            if key == 'escape':
                win.close()
                core.quit()
            if key == 'c':
                return
        prompt.draw()
        win.flip()


def record_response(data_save_path, response, response_time, subject_name,
                    subject_number, stimulus_number, first_write):
    data = [str(subject_name), str(subject_number), str(stimulus_number), str(response), str(response_time)]
    
    # if csv file does not exist, then write the header and the data
    if not os.path.exists(data_save_path):
        header = ['subject_name', 'subject_number', 'stimulus_number', 'response', 'response_time']
        with open(data_save_path, 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerow(data)
            file.close()
    # otherwise just write the data
    else:
        if first_write:
            print('\n\n\nYou tried to overwrite an existing file. '\
                  'Please delete the file or pick a new subject number.\n\n\n')
            raise(FileExistsError)
        # check that we are not overwriting an existing file
        with open(data_save_path, 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(data)
            file.close()
    return

# selects a video from the remaining available videos
def selectVideo(Conditions):
    cur_dir = os.path.dirname(__file__)
    stimuli_dir = os.path.join(cur_dir, 'stimuli')
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

    unusedConditions = []

    for condition, used in Conditions.items():
        if not used:
            unusedConditions.append(condition)
    selectedConditionOld = random.choice(unusedConditions)
    selectedCondition = int(selectedConditionOld.replace('condition', '')) - 1
    selectedVideo = str(numberToLetter[str((selectedCondition * 3) + random.randint(1,3))]) + '.mov.mp4'
    #finalVideoPath = os.path.join(stimuli_dir, 'condition1', 'aTest.mov.mp4')
    finalVideoPath = os.path.join(stimuli_dir, selectedConditionOld, selectedVideo)
    Conditions[str(selectedConditionOld)] = True
    print('\n\n\nFinal video Path: %s \n\n\n' %finalVideoPath)
    return finalVideoPath

# Define the fixation cross
def fixationCross(win):
    width, height = win.size
    windowScale = width / height
    crossScale = 15

    fixation = visual.ShapeStim(
        win=win, 
        vertices=((0, -1 * (windowScale / crossScale)), (0, windowScale / crossScale), (0,0), (-1 * (1 / crossScale),0), (1 / crossScale, 0)),  # Define the shape of a cross
        lineWidth = 10,
        closeShape = False,
        lineColor = "black")
    fixation.draw()
    win.flip()

# Function to clear all checkboxes (for single-selection logic)
def clear_checkboxes(checkboxes):
    for checkbox in checkboxes:
        checkbox.fillColor = None

def questionnaire(win):
    width, height = win.size
    windowScale = width / height

    # question 1 text and responses
    question1 = visual.TextStim(win, text='How interested were you in this video? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options1 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    option_stim1 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options1)]
    checkboxes1 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options1))]

    # question 2 text and responses
    question2 = visual.TextStim(win, text='How chilling did you find this video? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options2 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    option_stim2 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options2)]
    checkboxes2 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options2))]

    # question 3 text and responses
    question3 = visual.TextStim(win, text='How intense were your chills from this video? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options3 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    option_stim3 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options3)]
    checkboxes3 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options3))]

    # question 4 text and responses
    question4 = visual.TextStim(win, text='How much did you enjoy this video? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options4 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    option_stim4 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options4)]
    checkboxes4 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options4))]

    # question 5 text and responses
    question5 = visual.TextStim(win, text='How emotional did you feel while watching this video? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options5 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    option_stim5 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options5)]
    checkboxes5 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options5))]

    # question 6 text and responses
    question6 = visual.TextStim(win, text='How likely would you be to watch this video again? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options6 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    option_stim6 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options6)]
    checkboxes6 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options6))]

    # question 7 text and responses
    question7 = visual.TextStim(win, text='How likely would you be to share this video? Please click an option.', wrapWidth= 1.5, pos=(0, 0.4), color = (0,0,0))
    options7 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
    option_stim7 = [visual.TextStim(win, text=opt, color = (0,0,0), alignText = 'left', pos=(0, 0.1 - 0.1 * i)) for i, opt in enumerate(options7)]
    checkboxes7 = [visual.Rect(win, width=0.03, height=0.03 * windowScale, color = (0,0,0), pos=(-0.6, 0.1 - 0.1 * i)) for i in range(len(options7))]


    questionsTotal = [question1, question2, question3, question4, question5, question6, question7]
    optionsTotal = [options1, options2, options3, options4, options5, options6, options7]
    optionStimsTotal = [option_stim1, option_stim2, option_stim3, option_stim4, option_stim5, option_stim6, option_stim7]
    checkboxesTotal = [checkboxes1, checkboxes2, checkboxes3, checkboxes4, checkboxes5, checkboxes6, checkboxes7]

    mouse = event.Mouse(win=win)
    selected_option = None

    things = zip(questionsTotal, optionsTotal, optionStimsTotal, checkboxesTotal)
    data = []
    for question, options, option_stims, checkboxes in things:
        selected_option = None
        while selected_option is None:
            question.draw()
            for option_stim, checkbox in zip(option_stims, checkboxes):
                checkbox.draw()
                option_stim.draw()
            
        
            # Check for mouse clicks
            if mouse.getPressed()[0]:  # If the left mouse button is clicked
                for i, checkbox in enumerate(checkboxes):
                    if mouse.isPressedIn(checkbox):
                        clear_checkboxes(checkboxes)  # Clear all checkboxes (for single-selection)
                        checkbox.fillColor = 'black'  # Fill the clicked checkbox
                        selected_option = i  # Save the selected option index
                        data.append(options[selected_option])
                        break

            win.flip()
            core.wait(0.2)
    return data

# draw black borders while stimuli being presented?
def draw_borders(win, scaled_image_size):
    win.flip()
    
    
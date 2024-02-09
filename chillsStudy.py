from psychopy import visual, core
from random import randint
from helperFunctions import *
from pylsl import local_clock
import csv

def saveSubjectData(subjectName, subjectId, data, videoName):
    curDir = os.path.dirname(__file__)
    dataFolderPath = os.path.join(curDir, 'data')
    subjectDataFolderPath = os.path.join(dataFolderPath, subjectId)
    dataFilePath = os.path.join(subjectDataFolderPath, str(videoName) + '.csv')

    # create data folder if it does not exist
    if not os.path.exists(dataFolderPath):
        os.mkdir(dataFolderPath)
    
    # create subject data folder if it does not exist
    if not os.path.exists(subjectDataFolderPath):
        os.mkdir(subjectDataFolderPath)

    # CSV header
    header = ['name','question 1', 'question 2', 'question 3', 'question 4', 'question 5', 'question 6', 'question 7']

    with open(file = dataFilePath, mode = 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow([subjectName] + data)

    
# The experiment itself
def experiment(outlet, win, subjectName, subjectId):
    
    # path for images folder and image extension label for the videos
    cur_dir = os.path.dirname(__file__)
    stimuli_dir = os.path.join(cur_dir, 'stimuli')
    extension = '.mp4'

    # dictionary of booleans to track which experimental stimuli types have been used
    Conditions = {
        'condition1' : False,
        'condition2' : False,
        'condition3' : False
    }

    start_time = local_clock()

    # video for displaying the window
    #VidWin = visual.Window(fullscr=True, color=(0, 0, 0), units='norm')
    # Loop for handling events
    # Run this loop until the three videos have been shown
    while not all(Conditions.values()):  # Loop until a video from each condition has been shown

        # sorting out how to scale the videos to be full screen
        screenSize = win.size  # This gives you the size of the window in pixels
        screenWidth, screenHeight = screenSize  # Unpacks the size into width and height
        videoPath = selectVideo(Conditions)  # Select a video based on Conditions
        movie = visual.MovieStim(win, videoPath, size=None, loop=False, flipVert = False)
        nativeWidth, nativeHeight = movie.size
        scalingFactorWidth = screenWidth / nativeWidth
        scalingFactorHeight = screenHeight / nativeHeight
        movie.size = (nativeWidth * scalingFactorWidth, nativeHeight * scalingFactorHeight)

        # fixation cross for three seconds
        fixationCross(win)
        core.wait(3)

        # shows the video
        while not movie.isFinished:
            # draw the video on the screen
            movie.draw()
            win.flip()
            for key in event.getKeys():
                if key == 'escape': # escape will exit the study
                    push_sample(outlet, 'ESCP')
                    win.close()
                    core.quit()
                elif key == 'space': # spacebar for lsl stuff
                    print('space bar pressed')
                    push_sample(outlet, 'SPCE')
        movie.stop() # kill the video once it is completed
        print('Stimuli Finished')

        # wait for user to press the continue key ("c")
        win.flip() # clear window
        continuePressed = False
        if (not all(Conditions.values())) and any(Conditions.values()):
            print(Conditions['condition1'])
            print(Conditions['condition2'])
            print(Conditions['condition3'])
            # while not continuePressed:
            #     for key in event.getKeys():
            #         if key == 'c':
            #             continuePressed = True
            # Break screen
            data = questionnaire(win)
            saveSubjectData(str(subjectName), str(subjectId), data, str(os.path.basename(videoPath)[0]))
                # break_text = visual.TextStim(win, text="Take a break. Press 'c' when you are ready to continue.", height=0.1, color=(0, 0, 0))
                # break_text.draw()
                # win.flip()
        else:
            win.close()
            core.quit()

if __name__ == '__main__':
    
    # Create LSL outlet
    outlet = initialize_outlet()
    
    # initialize window and mouse object (set mouse to invisible)
    win = visual.Window(fullscr=True, color=background_color, units='norm')

    mouse = event.Mouse(win = win)
    #mouse.setVisible(False)
    
    # get user info and where to store their results
    subjectName, subjectId = opening_screen(win)
    
    # explain the experiment to the subject
    experiment_explanation(win)
    
    
    # move onto the real experiment
    #experiment(0, outlet, win, 0, 0) # testing purposes
    experiment(outlet, win, subjectName, subjectId)
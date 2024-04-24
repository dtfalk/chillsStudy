# Hello, this experiment was coded by David Falk of the APEX/Nusbaum lab at 
# the University of Chicago (2024). It was coded for Gabe Rodriguez as a 
# part of his research into physiological reactions to media, "chills"
# in particular. I will admit, it is a bit rough and could be improved in 
# many places. Sorry to all future coders!
# Please see the README for more information about this code
# and how to modify it to suit your particular needs.
from psychopy import visual, core
from helperFunctions import *

    
# The experiment itself
def experiment(outlet, win, mouse, subjectName, subjectId):
    
    # dictionary of booleans to track which experimental stimuli types have been used
    Conditions = {
        'condition1' : False,
        'condition2' : False,
        'condition3' : False
    }

    # Loop for handling events
    # This loop runs until the three videos have been shown (until "all conditions are True"... to paraphrase the syntax on the line below)
    while not all(Conditions.values()):  # Loop until a video from each condition has been shown

        # selects a video according to the "selectVideo" function and then scales the video to be full screen
        videoPath = selectVideo(Conditions) 
        movie = visual.MovieStim(win, videoPath, size=None, loop=False, flipVert = False)
        nativeWidth, nativeHeight = movie.size # nativeWidth translates to english as "the original width of the video" (same for nativeHeight)
        scalingFactorWidth = screenWidth / nativeWidth # this line find the ratio to scale the video by to make it seem fullscreen
        scalingFactorHeight = screenHeight / nativeHeight
        movie.size = (nativeWidth * scalingFactorWidth, nativeHeight * scalingFactorHeight) # resize the native values by the scaling factors to get something akin to a fullscreen video

        # shows a fixation cross
        fixationCross(win)

        # shows the video
        tagPushed = False
        while not movie.isFinished:

            # draw the video on the screen and display to the subject
            # also send an LSL tag denoting the start of the video
            if not tagPushed:
                win.callOnFlip(pushSample, outlet, 'VideoStart')
                tagPushed = True
                timestamps = [] # stores timestamps for spacebar presses (Behavorial)
            
            movie.draw()
            win.mouseVisible = False
            win.flip()

            # handles key presses (escape for exiting the experiment, spacebar for sending a timestamped tag to LSL)
            for key in event.getKeys():
                if key == 'escape': # escape will exit the study
                    pushSample(outlet, 'ESCP')
                    win.close()
                    core.quit()
                elif key == 'space': # spacebar for sending an LSL tag and timestamp via the outlet to the TBD inlet
                    timestamp = (movie.getPercentageComplete() / 100) * movie.duration # gets the timestamp in seconds
                    timestamps.append(timestamp)
                    print(timestamp)
                    pushSample(outlet, 'SPCE')
                    
        pushSample(outlet, 'VideoStop')
        movie.stop() # kill the video once it is completed
        win.mouseVisible = False
        win.flip() # clear window 

        # present the questionnaire to the subject and save their responses in a csv within the "data" folder
        # also saves timestamps of user spacebar presses
        saveTimestamps(str(subjectId), timestamps, str(os.path.basename(videoPath)[0]))
        data = questionnaire(win, mouse)
        saveSubjectData(str(subjectName), str(subjectId), data, str(os.path.basename(videoPath)[0]))
    
    # after exiting the while loop (after all videos and questionnaires have been presented), terminate the experiment
    win.close()
    core.quit()
    return


if __name__ == '__main__':
    
    # Create LSL outlet
    outlet = initializeOutlet()
    
    # initialize an experiment window in psychopy
    win = visual.Window(fullscr=True, color=backgroundColor, units='norm')
    screenWidth, screenHeight = win.size  # This gives you the size of the window in pixels as an unpacked tuple (width, height)

    # initialize a mouse object
    mouse = event.Mouse(win = win)
    
    # retrieve user info (subject name and subject ID)
    subjectName, subjectId = getSubjectInfo(win)
    
    # explain the experiment to the subject
    experimentExplanation(win)
    
    # present the experiment (videos + questionnaires) to the subject
    experiment(outlet, win, mouse, subjectName, subjectId)

    # thank the user for their time etc...
    exitScreen(win)
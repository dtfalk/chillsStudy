from psychopy import visual, core
from helperFunctions import *
import csv

    
# The experiment itself
def experiment(outlet, win, subjectName, subjectId):

    # dictionary of booleans to track which experimental stimuli types have been used
    Conditions = {
        'condition1' : False,
        'condition2' : False,
        'condition3' : False
    }

    # variables for sorting out how to scale the videos to be full screen
    screenWidth, screenHeight = win.size  # This gives you the size of the window in pixels as an unpacked tuple (width, height)

    # Loop for handling events
    # This loop runs until the three videos have been shown
    while not all(Conditions.values()):  # Loop until a video from each condition has been shown

        # selects a video according to the "selectVideo" function and then scales the video to be full screen
        videoPath = selectVideo(Conditions) 
        movie = visual.MovieStim(win, videoPath, size=None, loop=False, flipVert = False)
        nativeWidth, nativeHeight = movie.size
        scalingFactorWidth = screenWidth / nativeWidth
        scalingFactorHeight = screenHeight / nativeHeight
        movie.size = (nativeWidth * scalingFactorWidth, nativeHeight * scalingFactorHeight)

        # shows a fixation cross for three seconds
        fixationCross(win)

        # shows the video
        while not movie.isFinished:

            # draw the video on the screen
            movie.draw()
            win.flip()

            # handles key presses (escape for exiting experiment, spacebar for sending a timestamped tag to LSL)
            for key in event.getKeys():
                if key == 'escape': # escape will exit the study
                    push_sample(outlet, 'ESCP')
                    win.close()
                    core.quit()
                elif key == 'space': # spacebar for lsl stuff
                    print('space bar pressed')
                    push_sample(outlet, 'SPCE')

        movie.stop() # kill the video once it is completed
        win.flip() # clear window

        # present the questionnaire to the subject and save their responses in a csv within the "data" folder
        data = questionnaire(win)
        saveSubjectData(str(subjectName), str(subjectId), data, str(os.path.basename(videoPath)[0]))
    
    # after exiting the while loop (after all videos and questionnaires have been presented), terminate the experiment
    win.close()
    core.quit()
    return


if __name__ == '__main__':
    
    # Create LSL outlet
    outlet = initialize_outlet()
    
    # initialize an experiment window in psychopy
    win = visual.Window(fullscr=True, color=background_color, units='norm')

    # initialize a mouse object and make the mouse invisible
    mouse = event.Mouse(win = win)
    mouse.setVisible(False)
    
    # retrieve user info (subject name and subject ID)
    subjectName, subjectId = get_subject_info(win)
    
    # explain the experiment to the subject
    experiment_explanation(win)
    
    # present the experiment (videos + questionnaires) to the subject
    experiment(outlet, win, subjectName, subjectId)
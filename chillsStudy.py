# SEE IF THERE IS AN EASY WAY TO CHECK IF MOUSE RELEASES AS OPPOSED TO WHEN THE MOUSE GETS PRESSED.
# ADD A SUBMIT BUTTON AND MAKE SURE THAT AT LEAST ONE OPTION IS PRESSED BEFORE WE ALLOW THE USER TO SUBMIT
# DO NOT ALLOW MULTIPLE PRESSES OF A BUTTON (E.G THE SUBMIT BUTTON) BY HOLDING DOWN THE CLICK BUTTON 
# (FOR THE ABOVE USE A TIMER OR MAKE SURE THAT THE USER HAS UNCLICKED BEFORE WE ALLOW A CLICK TO BE REGISTERED)
# (TO CHECK IF USER HAS UNCLICKED WE COULD HAVE A BOOLEAN THAT IS SET TO TRUE WHEN CLICKED AND FALSE ONCE UNCLICKED)
# ( AND WE ONLY ALLOW CLICKS TO BE REGISTERED IF IT IS FALSE BUT NEED TO MAKE SURE THE LOGIC FOR SETTING CLICKED = TRUE)
# ( COMES AFTER WE CHECK THE CLICKED VARIABLE'S STATUS??????)
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
        while not movie.isFinished:

            # draw the video on the screen and display to the subject
            movie.draw()
            win.flip()

            # handles key presses (escape for exiting the experiment, spacebar for sending a timestamped tag to LSL)
            for key in event.getKeys():
                if key == 'escape': # escape will exit the study
                    pushSample(outlet, 'ESCP')
                    win.close()
                    core.quit()
                elif key == 'space': # spacebar for sending an LSL tag and timestamp via the outlet to the TBD inlet
                    pushSample(outlet, 'SPCE')

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
    outlet = initializeOutlet()
    
    # initialize an experiment window in psychopy
    win = visual.Window(fullscr=True, color=backgroundColor, units='norm')

    # initialize a mouse object and make the mouse invisible
    mouse = event.Mouse(win = win)
    mouse.setVisible(False)
    
    # retrieve user info (subject name and subject ID)
    subjectName, subjectId = getSubjectInfo(win)
    
    # explain the experiment to the subject
    experimentExplanation(win)
    
    # present the experiment (videos + questionnaires) to the subject
    experiment(outlet, win, subjectName, subjectId)
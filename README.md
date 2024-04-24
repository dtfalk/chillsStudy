Python Chills Study ReadME
================================================

Contact Info
------------------------------------------------
This is the contact info for David Falk, the coder for this experiment
email: dtfbaseball@gmail.com (UPDATE THIS)
cell: 1-413-884-2553

How to install Anaconda and download necessary packages
-------------------------------------------------

**Anaconada:** The first thing you need is a package manager. I would reccomend using Anaconda. Download Anaconda from this link: https://www.anaconda.com/download. If they ask you to provide an email there is a button that will allow you to skip this step. Once Anaconda is downloaded you need to open up the anaconda prompt or open a terminal of some kind. You can also use the Anaconda Navigator, but that is more complicated. Once you open your terminal/Anaconda Prompt use the following code to create an environment, activate your environment, and download the proper Python version.

>
    conda create --name chillsStudy
    conda activate chillsStudy
    conda install python=3.9.18

**Packages:** Now you need to install the required packages for the environment using the code below (make sure your environment is activated):

>   pip install psychopy==2023.2.3 pylsl==1.16.2

Great! You have everything you need now.


Downloading the code and the stimuli
---------------------------------------

1. You can find the code for this experiment on GitHub: https://github.com/dtfalk/chillsStudy. Enter this link in your web browser and you will see a GitHub page. Click on the green **Code** button in the top right of the screen and select **Download ZIP**. This downloads your code as a ZIP file.

2. Extract the folder within this zip file and place it on your desktop or somewhere that you will remember. Rename it **"chillsStudy"**.

3. Now we need to add the stimuli to the **chillsStudy** folder you just created. Go to https://drive.google.com/drive/folders/1BuoxX6frS6lBXdpy0spiSBIXm0sK1YDz to find the stimuli. Download all of these stimuli.

4. Within the **chillsStudy** folder create a new folder called **stimuli**. Within the **stimuli** folder create three folders: **condition1**, **condition2**, and **condition3**. 

5. Place stimuli **a**,**b**, and **c** in **condition1**. Place stimuli **d**,**e**, and **f** in **condition2**. Place stimuli **g**,**h**, and **i** in **condition3**.

Great! you now have the code, the stimuli, and all of the proper packages downloaded!

Running the code
--------------------------------------

If you use VS Code then open VS code. Make sure that you have the **Python** extension downloaded. If you don't, then navigate to the **Extensions** tab (found on the left side of the screen) and download it. Then find the **Command Palette** under the **View** tab. Enter **>Python: Select Interpreter** and choose the **chillsStudy** environment you just created.

Now use the **terminal** in VS Code to run the code. 

> python chillsStudy.py

Now the experiment should run. Hurrah.


Analyzing the data
-----------------------

After a user completes a study there will be a new **data** folder in the **chillsStudy** folder. If you open this folder there will be a subfolder with the subject number you just entered. So if you entered **123** as the subject number, **data** will have **123** as a subfolder. Within this folder there will be six files. Let's assume that the user was served videos **a**, **d**, and **g**. Then you will see **a.csv**, **aTimestamps.csv**, **d.csv**, **dTimestamps.csv**, **g.csv**, and **gTimestamps.csv**. For video a, **a.csv** is the user's response to the questionnaire they were given after finishing the video and **aTimestamps.csv** contains the timestamps of when the user pressed the spacebar while watching the video. If you see a timestamp that says **90**, then the user pressed the spacebar at the 90-second mark in the video. The same follows for videos **d** and **g**. Each user gets a folder whose name is their subject number. Within that folder is their responses to the questionnaires and the timestamps for when they pressed the spacebar for each video. 


How to change some things
-----------------------------

You may want to change a couple of things in the experiment such as the color scheme, the wording of instructions, how many questions there are, etc... So I will go through how to make some of these changes. 

1. **Changing the color scheme:** At the top of the **constants.py** file you will find three variables: **backgroundColor**, **textColor**, and **questionSelectedColor**. **backgroundColor** is the color for the background of the study. It is currently set to white. **textColor** is the color of any text that the user sees. It is currently set to black. **questionSelectedColor** is the color that a questionnaire checkbox changes to when a user selects it. To change any of these, you can set them equal to another color name (look at https://www.w3schools.com/Colors/colors_names.asp for a list of color names). You can enter the RGB value or the hexadecimal value for some other color if it is not on that list. 

2. **Changing the text for various message screens:** There are only three screens that I would imagine you want to change the messages for: the instructions screen, the reminder screen, and the goodbye/exit screen. If you look in **constants.py** and scroll down you will see **explanationText**, **reminderText**, and **exitScreenText**. Change these to your desired wording. You will see **\n\n** in the strings. Each **\n** indicates that we want to insert a line of whitespace. It helps with spacing and making things look cleaner/more readable. The trailing slash you see in the code after the **\n\n** is how you make a variable declaration span more than one line. In my code, each line of the **explanationText**, **reminderText** **exitScreenText** variables is its own line when it gets displayed to the user. If you follow and copy my formatting then you shouldn't have an issue adding and removing lines.

3. **Adding more questions to the questionnaire, changing questionnaire wording, changing wording of the response options:** It is possible that you may want to add more questions, change some wording, or change the options that the user can select from. To do this, first navigate to the **helperFunctions.py** file. Then find the **questionnaire** function. Towards the top of the function you will see code like this...

    >
        # question 1 text and response options
        question1 = visual.TextStim(win, text='How interested were you in this video? Please select an option and then click Submit.', wrapWidth= 1.5, pos=(0, 0.4), color = textColor)
        ResponseOptions1 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']

        # question 2 text and response options
        question2 = visual.TextStim(win, text='How chilling did you find this video? Please select an option and then click Submit.', wrapWidth= 1.5, pos=(0, 0.4), color = textColor)
        ResponseOptions2 = ['Very slightly or not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']

    This is where we define the questions and their responses. If you want to change a question one's wording, then change the **text = ...** entry in the **question1** variable. Just change the stuff within the quotation marks. Similarly, if you want to change one of the options that the user has to choose from, for example the **Very slightly or not at all** option in **ResponseOptions1**, then change the text that says **Very slightly or not at all** to something else (change the stuff within the quotation marks).

    If you would like to add another question, let's call it question 8, then do something like this below the variables for question 7...

    >
        # question 8 text and response options
        question8 = visual.TextStim(win, text='THIS IS THE TEXT FOR QUESTION 8. Please select an option and then click Submit.', wrapWidth= 1.5, pos=(0, 0.4), color = textColor)
        ResponseOptions8 = ['option 1', 'option 2', ... , 'option N']
        questionsTotal.append(question8)
        optionsTotal.append(ResponseOptions8)

    That will do it! You have now added an 8th question!

4. **How to add a new video and/or new condition:** Currently, the experiment is broken up into three conditions (I do not know what the different conditions mean) with three videos per condition. It is possible that you want to add another video or another condition. Let's go through how to do that.

    **Adding a video to an existing condition:** To do this, simply add another video (mp4 preferably) to the condition that you want. That is all that you need to do.

    **Adding a new condition:** This one is slightly more complicated, but just barely. There are currently three conditions in the study. The first thing you need to do to add a fourth condition is create a new folder in **stimuli** and name it **condition4** and add your condition 4 videos to this folder. Then open the **chillsStudy.py** file and find the **experiment** function. You will see is a variable called **Conditions**. It looks like this...

    >
        # The experiment itself
        def experiment(outlet, win, mouse, subjectName, subjectId):
            
            # dictionary of booleans to track which experimental stimuli types have been used
            Conditions = {
                'condition1' : False,
                'condition2' : False,
                'condition3' : False
            }

    Add a line to the **Conditions** variable that says **'condition4' : False'** and make sure to add a comma after the **False** in the **condition3** line. Your modified function will look like this...

    >
        # The experiment itself
        def experiment(outlet, win, mouse, subjectName, subjectId):
            
            # dictionary of booleans to track which experimental stimuli types have been used
            Conditions = {
                'condition1' : False,
                'condition2' : False,
                'condition3' : False,
                'condition4' : False
            }

    You have now added a new condition! That is all you need to do. Congrats.




























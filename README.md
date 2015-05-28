# Disney-Wait
An arduino based project to visually see how long wait lines are at the Disneyland Resort. Using a small Python program, your computer will connect to an API and pull the latest wait time for Disneyland and California Adventure theme parks, and pass the information to the arduino using Py_Serial over USB. The arduino then drives the speed of a continuous servo based on the wait time for the ride (the longer the wait, the slower the speed). You can choose which ride to show via a command prompt.

To make it a little more visually interesting, I built a small ferris wheel using Knex and had the servo spin the ferris wheel.

##Setup
You must have Py_serial installed on your computer. Visit http://pyserial.sourceforge.net for more information. Open your Terminal, navigate to the Python file, and run the command Python DisneyWait.py. You may need to update the Serial connection to whatever your arduino is communicating across. Open the .ino file in the arduino IDE, connect your arduino via USB, and click run (make sure your connection port is either on port 9, or update the code to reflect whatever port you're using).
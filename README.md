# TAU6: A Virtual Coach for Presentation Skills

## How To Set Up TAU6

This program is designed to work on a Windows Machine with a working Kinect. 

1) Clone this repository. 
2) Download the Kinect SDK v1.8 from Microsoft.
https://www.microsoft.com/en-us/download/details.aspx?id=40278
Install every Kinect program in there to make this run smoothly.

Update your python version to Python3.5+.

Download Visual Studio to execute the Kinect code.
https://visualstudio.microsoft.com/downloads/

If you do not have pip, install pip following the instructions at this site: https://pip.pypa.io/en/stable/installing/

Pip install the my-voice-analysis library
$pip install my-voice-analysis

Pip install the sounddevice library
$pip install sounddevice

3) Make edits.
Edit the GUI.py file in the root directory. In line 33, change the path to the tau6 directory that you have cloned this repository into.
In line 24, you can change the number of seconds you want yourself to be recorded. You can also change the output file name and path in lines 29 and 30.

3) Run the program.
Run the program by running the play button in Visual Studio after opening the MainWindow.xaml.cs file inside SkeletonBasics-WPF folder in Visual Studio.
Now, use python to run GUI.py to also run the audio portion of TAU6.

## Code Explanations
This repository will be broken down into two parts. 
Under the folder SkeletonBasics-WPF, we have all the Kinect code contained inside. 
The code inside the SkeletonBasics-WPF folder is mostly C# and can be viewed and executed through Visual Studio.

MainWindow.xaml.cs is the main executable that handles the backend of the project and recognizing the gestures. 
This is the meat of the work where we recognize gestures, change seated status, and handle drawing the skeleton frame.
MainWindow.xaml works as a front end for the UI. The rest of the file are part of the skeleton code that sets up the Visual Studio program to run
our program.
The code here is thoroughly commented, so a regular coder should be able to easily understand what the methods and variables are in the code.

The rest of the code at the root directory are for the voice analysis portion of TAU6.
GUI.py contains the runnable module for the application with comments detailing each section. myspsolution.py contains the slightly edited analysis functions, and uses information from myspsolution.praat.

The different TextGrid and wav files contain either the output data, the ones named output, or samples of the comparison data, the obama, motivational, and news files. The statistics drawn from the comparison files are summarized in the Comparison Data doc.

Pygame EOG Visualization Challenge - 2/5/24
Overview
Create a pygame simulation that transforms EOG (Electrooculography) data into a visual representation. Follow the steps below to set up the project.

Step 1: Download EDF File
Download the required .edf file from PhysioNet.
https://physionet.org/content/sleep-edfx/1.0.0/sleep-cassette/#files-panel

Step 2: Extract EOG Data
Use the provided Python script to extract EOG data from the downloaded .edf file. The script utilizes the MNE library to process the data and save it to a CSV file.

python eogtocsv.py


csv output data
eogdata.csv

Time,EOG Horizontal
0.0,1.650866910866916e-05
0.01,1.601587301587307e-05
0.02,9.609523809523861e-06
0.03,1.7247863247863773e-06
0.04,7.63833943833949e-06
0.05,2.710378510378563e-06
0.06,2.463980463980988e-07
Pygame Simulation
Now, use the extracted EOG data to create a pygame simulation that visually represents the information. Implement your simulation code and visualize the changes in the EOG data over time.
 example simulation 
eyeview1color.py
 
Feel free to customize the visualization to make it more engaging and informative.

Instructions
Download the EDF file.
Run the provided Python script to extract EOG data.
Create a pygame simulation using the extracted data.
Customize and enhance the visualization as desired.
Good luck with the challenge!


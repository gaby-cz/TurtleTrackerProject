#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Gaby Czarniak (gabriella.czarniak@duke.edu)
# Date:   October 2024
#--------------------------------------------------------------

#Create a variable pointing to the data file. Use relative paths to current wd rather than abs path
file_name = './data/raw/sara.txt'

#Create a file object from the file. Analog version would be going into finder and double clicking file and opening it.
file_object = open(file_name,'r')

#Read contents of file into a string. The memory footprint of reading our data one line at a time is smaller.
lineString = file_object.readline()

#Try with a while loop now. Most things under "for" stay the same. Empty string equates to false.
while lineString:
    # Check if line is a data line
    if lineString[0] in ("#","u"):
            lineString = file_object.readline()
            continue #essentially, then skip

    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

    #Update the variable we're evaluating in the line loop. Read next line.
    lineString = file_object.readline()
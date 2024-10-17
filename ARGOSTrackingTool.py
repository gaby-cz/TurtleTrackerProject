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

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file -- now can't access file object bc it's closed.
file_object.close()

#Initialize dictionaries
date_dict = {}
location_dict = {}

# Pretend we read one line of data from the file
for lineString in line_list:
    # Check if line is a data line
    if lineString[0] in ("#","u"):
        continue #essentially, then skip

    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Determine if location class criterion is met
    if obs_lc in ("1", "2", "3"):
        #Add items to dictionaries
        date_dict[record_id] = obs_date # key here is record id bc every line has a unique one, so we can use it to pull out the associated observation date
        location_dict[record_id] = (obs_lat, obs_lon) # same key, with tuple of lat and longitude per record id

    #Print the location of sara
    #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
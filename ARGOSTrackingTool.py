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

#Ask user for a date, specifying the format
user_date = input("Enter a date (M/D/YYYY): ")

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

#Initialize key list for later append. These following commands should run after for loop is completed
keys = []

#Loop through items in date_dict
for key, value in date_dict.items(): # the items are key value pairs so we'll pull them out into separate values
    if value == user_date: # the value in date_dict is the date
        keys.append(key) # add key to list

#Loop through keys and report locations
for key in keys:
    location = location_dict[key]
    lat = location[0]
    lon = location[1]
    print(f"On {user_date}, Sara the turtle was seen at {lat} degrees Latitude, {lon} degrees Longitude.")
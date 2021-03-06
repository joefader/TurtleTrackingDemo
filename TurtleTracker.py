# Task1.py
#
# Description: Parses a line of ARGOS tracking data 
#
# Created by: Joe Fader
# Created on: Oct 2016

# Create a variable pointing to the file with no header
fileName = "V:\\L3_IntroToScripting\\Scripting3\\Scripting3\\SaraNoHeader.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read the first line from the open file object
lineString = fileObj.readline()


# Use a while loop to read each line, one at a time, until the end of the file is reached
while lineString:

    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split("\t")

    # Assign variables to specfic items in the list
    recordID = lineData[0]              # ARGOS tracking record ID
    obsDateTime = lineData[2]           # Observation date and time (combined)
    obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
    obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
    obsLC = lineData[3]                 # Observation Location Class
    obsLat = lineData[5]                # Observation Latitude
    obsLon = lineData[6]                # Observation Longitude

    # Print information to the user
    print "According to record " + recordID, 
    print "Sara was seen at " + obsLat + " d LAT; " + obsLat + " d LON on " + obsDate

    # Read in the next line
    lineString = fileObj.readline()
    
# Close the file object
fileObj.close()
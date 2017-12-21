# Created by: Gavin Zhou
# Created on: D 2017 
# Created for: ICS3U

from enum import Enum

# an enumerated type of days of the week
weekdays = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

day_selected = raw_input('Enter your favourite day: ')

if day_selected in weekdays:
    print('your favourite day is: ' + day_selected)
    
else :
    print("Please enter a right word, don't forget capital")

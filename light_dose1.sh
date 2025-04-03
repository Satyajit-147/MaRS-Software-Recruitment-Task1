#!/bin/bash

mkdir rover_mission # Create a new directory named rover_mission
cd rover_mission # Change the directory to rover_mission
touch log1.txt log2.txt log3.txt # Create 3 text files within the directory
mv log1.txt mission_log.txt # Rename log1.txt file to mission_log.txt
ls *.log # Find all files with .log file extension
cat mission_log.txt # Display the contents of mission_log.txt
grep "ERROR" mission_log.txt # Search for lines containing the word "ERROR" in mission_log.txt and print them
wc -l mission_log.txt # Count the number of lines in mission_log.txt (-l ensures only lines are counted)
date # Display the date and time
top # Display CPU information (q key is used to exit the top command)
sudo shutdown +10 # Shutdown in 10 minutes
chmod +x light_dose1.sh # Give execute permissions to the script



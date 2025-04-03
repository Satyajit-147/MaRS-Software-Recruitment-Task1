mkdir rover_mission #create a new directory named rover_mission
cd rover_mission #changes the directory to rover_mission
touch log1.txt log2.txt log3.txt #create 3 text files within the directory
mv log1.txt mission_log.txt #rename log1.txt file to mission_log.txt
ls *.log #find all files with .log file extension
cat mission_log.txt #display the contents of mission_log.txt
grep "ERROR" mission_log.txt #Searches for lines containing the word "ERROR" in the file mission_log.txt and prints them
wc -l mission_log.txt #word count of the text file mission_log.txt (-l ensures that only the lines are counted)
date #Display the date and the time
top #Displays CPU information (q key is used to exit the top command)
sudo shutdown +10 #Shutdown in 10 minutes





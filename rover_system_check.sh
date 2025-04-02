battery=$((RANDOM % 101)) #battery variable stores a random value from 0 to 100 inclusively
echo "Battery level: $battery%" #Prints the current battery level

if [ "$battery" -lt 20 ]; then #Checks if the battery level is lesser than 20
	echo "Battery low! Return to base!" #Prints the statement is the condition is true
	exit 1 #Exits if the condition is not met
fi

if ! ping -c 1 google.com &> /dev/null; then #Ping google.com to check network connectivity 
	echo "Communication failure!" #Prints the statement is the condition is true
	exit 1 #Exits if the condition is not met
fi

echo "All systems operational!" #Prints this statement if both the if conditions are met
exit 0

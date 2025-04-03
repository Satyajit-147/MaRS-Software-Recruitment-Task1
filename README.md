**#MaRS Task1**

**##Experience and Learnings**

Working with Git and GitHub using Linux commands was a hands-on experience. For this task I successfully initialized a repository, pushed all python files to the repository and authenticated my GitHub using a Personal Access Token (PAT). I've solved 2 easy questions, 5 medium questions and 1 hard question which helped my revise my basic Python programming concepts.
Through this process, I learned:
- How to navigate directories and create new files using Linux commands
- Generate PAT for authentication instead of having to enter the password each time
- Troubleshoot common Git errors (Eg: Incorrect branch name
- Learnt file handling concepts in Python

**##Steps Taken to Push FIles to GitHub**
1. Initialize Git in the repository (Command: git init)

   ![Initializing Git](init.png)
   

   **Description:** Creates a new Git repository within the diretory (if not already initialized)
   

3. Check the Current Git Branch (Command: git branch)

   ![Initializing Git](branch.png)
   
   **Description:** Displays the active branch (main/master). If no branch exists, it's taken as main by default


5. List down the remote repositories (Command: git remote -v)

   ![Initializing Git](remote-v.png)
   
   **Description:** Displays the remote repository URLs linked to your local Git repository, showing both fetch and push destinations.


7. Add files (Command: git add .)

   ![Initializing Git](add.png)
   
   **Description:** Adds all the files in the current directory to the staging area preparing them for commit
   

9. Commit the Changes (Command: git commit -m "Initial commit")

    ![Initializing Git](commit.png)
   
   **Description:** Saves the changes made with a description (message) "Initial commit"
   

10. Link Local Repository to GItHub repository (Command: git remote add origin https://github.com/Satyajit-147/MaRS-Software-Recruitment-Task1.git)

    ![Initializing Git](remote_add_origin.png)
   
   **Description:** This command is to connect local Git repository to a remote GitHub repository


11. Push Files to GitHub (Command: git push -u origin main)

    ![Initializing Git](push.png)
   
   **Description:** The command uploads the commited changes from local repository to the remote repository on GitHub. -u enables pushing to be done without specifying the active branch


**##Bash Scripting**
For this task, I generated a random number between 0 and 100 for the battery level using the command RANDOM%101, followed by two if conditions. The first condition checks if the battery level is below 20% and displays an appropriate error message if the condition is met. The second condition pings google.com to check network connectivity. If both checks pass, the script prints "All systems operational"; otherwise, it exits with an error message.


**#MEDIUM DOSE**

**##Task1**

The task was to determine the adjusted coordinates of the Rover Brick. According to the problem, the rover made a 360-degree turn 55 cm behind the actual mark. To correct its position, I first calculated the direction vector from the initial reference point to the final position. Then, I computed the unit vector, multiplied it by 55, and added the result to the final rover coordinates to obtain the corrected position. The initial reference frame and the rover’s final position before adjustment are taken as input from the user.
   

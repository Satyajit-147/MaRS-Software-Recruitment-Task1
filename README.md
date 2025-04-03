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

   **Description:** Creates a new Git repository within the diretory (if not already initialized)


2. Check the Current Git Branch (Command: git branch)
   
   **Description:** Displays the active branch (main/master). If no branch exists, it's taken as main by default


3. List down the remote repositories (Command: git remote -v)
   
   **Description:** Displays the remote repository URLs linked to your local Git repository, showing both fetch and push destinations.


4. Add files (Command: git add .)
   
   **Description:** Adds all the files in the current directory to the staging area preparing them for commit
   

5. Commit the Changes (Command: git commit -m "Initial commit")
   
   **Description:** Saves the changes made with a description (message) "Initial commit"
   

6. Link Local Repository to GItHub repository (Command: git remote add origin https://github.com/Satyajit-147/MaRS-Software-Recruitment-Task1.git)
   
   **Description:** This command is to connect local Git repository to a remote GitHub repository


7. Push Files to GitHub (Command: git push -u origin main)
   
   **Description:** The command uploads the commited changes from local repository to the remote repository on GitHub. -u enables pushing to be done without specifying the active branch



   

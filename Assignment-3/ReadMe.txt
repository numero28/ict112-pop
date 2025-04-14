Assignment 3:
 
 
🚀 Basic Steps to solve the assignment. 
Note: you have to first create a GitHub account

✅ 1. Fork the Repository 
Go to the GitHub page https://github.com/numero28/ict112-pop.

Click the Fork button (top-right corner). This creates a copy of the repo in your GitHub account.

✅ 2. Clone Your Fork
Open a terminal and run:

git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
Move into the project directory:

cd REPO-NAME
✅ 3. Add the Original Repository as a Remote
This helps you stay in sync with the main repository.

git remote add upstream https://github.com/numero28/ict112-pop.git
✅ 4. Create a New Branch
Always make changes in a separate branch, not main or master.

git checkout -b your-feature-name
✅ 5. Make a copy of the file (solutions.py) in the folder named "Assignment 3".
      Rename the copy using the following format:
        Solutions_<your index number>_2025.py
      Provide solutions to the problem statements in the file and save your work   	

✅ 6. Commit and Push
git add .
git commit -m "A brief description of what you changed"
git push origin your-feature-name

✅ 7. Create a Pull Request (PR)
Go to your forked repo on GitHub.

Click "Compare & pull request".

Add a description of your changes and submit the pull request.
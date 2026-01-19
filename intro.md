## Agenda
1. Set Up the Github --> Repository for commiting our code ---> Working in a team --> Development will be in sync.
- Here we will setup the new environment.
- Decide a mini-project structure ---> We will discuss abt setup.py(its importance).
- requirements.txt

2. Src folder and build the package.

- Go create a repo at github, no need to add reamdme file.

- Now we need to sync with our github repositroy over here.
- Open the terminal:
- Enter the Github Commands:
- create a new repository on the command line:
- echo "# MLOPS-P3" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/Amritanshu888/MLOPS-P3.git
- git push -u origin main


-  push an existing repository from the command line
- git remote add origin https://github.com/Amritanshu888/MLOPS-P3.git
- git branch -M main
- git push -u origin main

- We will get these commands when we create a new repo.

- To see the status w.r.t the commit we use : git status

- To check if its synced or not : git remote -v

- git pull : We use this command when we do some changes in our github repo and want that same changes to happen/update in my current working directory.

# Process

## Virtual environment and install packages

### Create a virtual environment to work in windows

python -m venv \<env_name>  

### Activate the virtual environment

.\<env_name>\Scripts\activate

### Deactivate the virtual environment

deactivate

### Add all python libraries in one file

[requirements.txt]{"..\requirements.txt"}

### Install all packages listed in requirements.txt file

pip install -r requirements.txt

## Create git repository for a project and branch it

1. git init -> Initialize a git respository  
   - git init \<project-directory> -> Initialize in the given directory

2. Clone repository example -> by clone a repository url

   1. git clone \<repo-url> -> Cloning an exiting repository

      - You can use git SSH protocol using git@HOSTNAME:USERNAME/REPONAME.git

   2. git add .| git add \<file-name> and git commit -m "Message" -> Save changes to the repository

   3. git push -- Save changes from local to github

3. Bare repository example -> without clone direct from local to remote repository

   1. git init --bare
   2. git clone --bare

   3. git config --global user.email "you\@example.com" or git config --global user.name "your name" -> adding --local we only set the names for the current local repository.

      1. git config --list -- List all the settings made
         - git config --list --show-origin

      2. git remote add <remote_name> <remote_repo_url>

      3. git push -u <remote_name> <local_branch_name>

4. Branching

   1. git checkout -b \<branch-name>  -> git branch \<branch-name> | git checkout \<branch-name>

      Switched to a new branch \<branch-name> copying from main branch

      - git branch -M \<branch-name> -> Rename the current branch

   2. git branch -d \<branch-name> -> Delete branch

   3. git checkout \<branch-name-1>
      git merge \<branch-name-2> -> Merge branch-name-2 into branch-name-1
      git branch -d \<branch-name-2> -> After merging you can delete the branch

   4. git checkout -b \<branch-name> \<existing-branch-name>

      Switched to a new branch \<branch-name> copying from the existing branch

   5. Checkout a remote branch

      git fetch --all
      git checkout \<remote-branch> | git checkout \<remote-branch> origin/\<remote-branch>

   6. Resolve merge conflict

      1. git checkout \<branch-name-1>
         git merge \<branch-name-2>
      2. git status
      3. cat merge.txt
      4. git diff -> Check differences between states of a repository
      5. git merge --abort

   7. git branch -M master

   8. git push -u origin master

5. git push --all origin -> push all branches to remote

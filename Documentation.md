# Git Workshop Assignment

## Assignment: Git Commands and Concepts

### Scenario 1: Conflict Resolution
**Task:** Imagine you and your teammate are working on the same file, `project.txt`. Both of you make changes to the same lines and commit them. Let’s say your teammate’s changes are merged first. And now when you try to merge your changes, a merge conflict occurs.

**Commands Used:** 
```
mkdir "TASK - 1"
git branch user1
git branch user2
cd "TASK-1"
```
```
//My changes as user1
touch project.txt
git checkout user1
echo "This is the content by user 1" > project.txt
git add . && commit -m "Created project.txt and added some content to it."
```
```
//My FRIEND's changes as user2

touch project.txt
git checkout user2
echo "This is the content by user 2" > project.txt
git add . && commit -m "Created project.txt and added some content to it."
```
```
git checkout master

//Merging my branch to main

git merge user1

//**no conflict yet**

//Merging FRIEND's conflicts to main
git merge user2

**conflict occured
```
![](/TASK%20-%201/merge-conflict.png)

***Apparently, To solve the issue occured here, we need to review the user2 changes. If nothing collides with user1 changes, we have to mark this as resolved by staging and committing the changes.***

   ```
   git add .
   git commit -m "accepted the merge changes from user 2"

   ```
***And therefore the file's content now is :***

![](/TASK%20-%201/project.txt%20snapshot.png)

**Steps taken:**

I took the following steps: 

1. Reviewed the conflict message thorougly to implement its resolution, i.e to merge the two changes from users.

2. Checked if changes from user2 replaces changes from user1, if not proceed to next step

3. Marked the conflict as resolved by adding the files to staging.
4. Finally, committing the changes and confirming whether the changes have been made or not.

### Scenario 2: Add Files and Commit Together
**Task:** You have worked on multiple files and want to add them and commit using a single command.

**Steps:**
1. Created 3 python code files.
2. Created Python files for Addition, Subtraction and Multiplication of 2 numbers.
3. Adding the Files for tracking
   ```
   git commit "Added python files for TASK - 2"
   ```
4. Further modifying multiple files to implement the code logic.
5. Added for staging and Committed the changes using a single command :
   ```
   git commit -am "Modified Python files for Addition, Subtraction and Multiplication"
   ```
![](/TASK%20-%202/Files.png)

### Scenario 3: Include Additional Commit in the Previous Commit Message
**Task:** You have just made a commit but realize you forgot to include a file and make a small typo correction. Instead of creating a new commit, you can amend the last commit to include these changes without altering the commit message. Also verify the amended commit by checking the commit log.

**Steps:**
1. Created Instructions.txt with instructions to create a python program for Fibonacci series.
2. Programmed the Python file according to instructions.
3. Added to tracking and Staging.
4. Committed the changes.
      ```
      git commit -am "Added Instructions and Python program file for fibonacci series"
      ```
![](/TASK%20-%203/Initial%20commit.png)

5. Typo error discovered at line 1 of Instruction file, resolved it
6. Amended to existing commit
   ```
   git add Instructions.txt
   git commit --amend
   ```
![](/TASK%20-%203/Final%20Commit.png)

### Scenario 4: Stash Command
**Task:** You are working on a feature but need to quickly switch to another task without committing your current changes.

**Steps:**
1. checking if working tree is clean
   ```
   git status
   ```
2. Creating a blank python program file for random number generation and also adding it for tracking and committing the changes.
   ```
   touch random_num.py
   git commit -am "added the python program file for random numbers."
   ```
3. Checking if working tree is clean or not, using `git status`
4. adding the actual code to file, i.e. modifying the current file. Therefore the changes are not staged and committed. In this case I want to work on a different file and don't want my incomplete changes to be committed, therefore, I'll use a stash to store my current changes.
   ```
   git stash
   // checking if the working tree asks to stage or commit
   git status
   ```
![](/TASK%20-%204/git%20stash.png)

5. Once i'm done working with the higher priority tasks, its time to complete the stashed task followed by staging and committing it. For that first I need to retrieve my stored changes in stash.
   ```
   git stash pop
   //this removes the topmost change stored in stash stack.
   ```
![](/TASK%20-%204/git%20stash%20pop.png)

6. Experimentation with `git stash list` and `git stash drop`
![](/TASK%20-%204/git%20stash%20list.png)

![](/TASK%20-%204/git%20stash%20drop.png)

### Scenario 5: Use of .gitignore
**Task:** You have files in your project that should not be tracked by Git, such as log files or build artifacts.

**Steps:**
1. Created `tracked_file.txt`, `ignored_file.log` and .gitignore.
   ```
   touch tracked_file.txt ignored_file.log .gitignore
   ``` 
2. Adding `tracked_file.txt` & `.gitignore` for tracking, EXCEPT `ignored_file.log`, resulting to a warning of untracked file.
   ```
   git add tracked_file.txt .gitignore
   ```
   ![](/TASK%20-%205/not%20ignoring.png)
3. Adding `ignored_file.log` to .gitignore for it to be ignored for tracking. Also adding .gitignore for staging.
   ```
   echo "ignored_file.log" >> .gitignore 
   git add .gitignore
   ```
4. Verifying if `ignored_file.log` is ignored for tracking or not.
   ![](/TASK%20-%205/ignoring.png)
   *Hence, it is no longer being tracked*

``Explain real-life use cases of a ".gitignore". What type of files are included in it?``
   ```
   A .gitignore file prevents unnecessary or sensitive files from being tracked in a Git repository. Typical files include:

   - Sensitive configuration: .env
   - System-specific files: .DS_Store, Thumbs.db
   - Build artifacts: dist/, *.class, *.o
   - Dependencies: node_modules/, vendor/
   - Logs: *.log
   - Temporary files: *.tmp, *.swp
   - IDE config: .vscode/, .idea/, *.iml
   - Runtime data: *.pid, coverage/
```

### Scenario 6: Revert to Previous Commits
**Task:** You made a mistake in a recent commit and need to revert the changes.

**Steps:**
1. Created `pyramid.py`, added code to it.
   ```
   touch pyramid.py
   ```
2. Added `pyramid.py` to tracking and committed the changes.
   ```
   git add .
   git commit -m "Created pyramid.py and added working code in it."
   ```
   ![](/TASK%20-%206/1st%20commit.png)
3. Made some other changes and committed the new changes.
   ```
   git commit -am "Update the initial code for pyramid.py"
   ```
   *Realised a mistake in the code, making it unable to execute*

   ![](/TASK%20-%206/mistake%20commit.png)

4. Reverting the most recent commit.
   ```
   //checking the commit's ID
   git log

   git revert 987f56395977f1eddfb807f728d45eccfcb8c799
   ```
   *Checking if the revert was successful i.e. code is complete or not in pyramid.py*
   ![](/TASK%20-%206/reverted%20commit.png)

### Scenario 7: Create a Pull Request
**Task:** You have made changes on a feature branch and want to merge them into the main branch via a pull request.

**Steps:**
1. Adding a remote to this this repository
   
   ```
   git remote
   git remote add origin https://github.com/mShubham18/GIT-ASSIGNMENT-3.git
   ```
2. Creating `primenum.py` and adding program code to it. Also adding it for tracking and committing changes.
   ```
   touch primenum.py
   //adding content manually through GUI
   git add primenum.py
   git commit -m "Added primenum.py"
   ```
3. Pushing the local repository `master` branch to remote repository
   ```
   git push origin master
   ```
4. Creating a `feature` branch and creating `factorial.py` with its code

   ```
   git branch feature
   touch factorial.py
   git add .
   git commit -m "Added Factorial.py for factorial program"
   ```
5. Pushing the feature branch into remote repository.
   ```
   git push origin feature
   ```
*Visiting the Remote repository to verify notification*

*Recieved Push notification*

![](/TASK%20-%207/push%20notification.png)

*Describing the changes done*

![](/TASK%20-%207/changes%20description.png)

*Creating a Pull Request (PR)*

![](/TASK%20-%207/Creating%20PR.png)

*Confirming merge*

   ![](/TASK%20-%207/Confirming%20merge.png)

*Proceeding with merging*

   ![](/TASK%20-%207/confirmed%20merge.png)

*Validating Merging of changes*

   ![](/TASK%20-%207/Verifying%20merge.png)

By completing these tasks, you'll gain hands-on experience with essential Git commands and concepts.

## Questions:

Please answer the following questions briefly by providing use cases.

1. Why do we create branches in a repository and why do we create pull requests instead of merging directly?

   ```
   Branches: We create branches in Git repositories to work on features or fixes without affecting the main codebase. It isolates changes for review and testing.
   
   Pull Requests: Instead of merging directly, pull requests allow contributors to propose changes. They facilitate code review, feedback, and integration into the main branch with controlled merging.
   ```

2. What is the difference between `git add .` and `git add <filename>`? What will we use when we have changes in multiples but we are not required to add some files?
   ```
   git add .: Adds all changes in the current directory and subdirectories to the staging area.
   
   git add <filename>: Adds specific file changes to the staging area.
   
   Use case: When you have changes in multiple files but don't want to add all of them, use git add -p to selectively stage changes within files.
   ```
3. What is the difference between `git fetch` and `git pull`?
   ```
   git fetch only downloads changes; git pull also integrates them into your working branch.
   ```
4. What is a head in a repository and what does it do?
   ```
   Head: In Git, "HEAD" (uppercase) refers to the currently checked-out branch or commit. It points to the latest commit of the branch you are working on.
   
   Function: HEAD determines where your next commit will go and serves as a reference to the state of your working directory.
   ```

5. What is the `.git` folder in a repository?
   ```
   The .git directory is at the root of a Git repository and contains all the metadata and object database for the repository. It stores configuration settings, commit history, object references, etc.
   ```
6. What are commit hashes and its use cases?
   ```
   Commit hashes: Unique identifiers for commits in Git, generated based on the commit's content.
   
   Use cases: Identify specific commits for referencing in commands (git checkout <hash>), reverting changes, merging branches, and viewing commit history.
   ```
7. Different ways of syncing a branch with origin.
   ```
   3 ways :

   git push <remote> <branch>: Push local commits to the remote branch.
   
   git pull <remote> <branch>: Fetch changes from the remote branch and merge them into the current branch.
   
   git fetch <remote> followed by git rebase <remote>/<branch>: Fetch changes and reapply local commits on top.

   ```

   *ps - previously this file was "Git-Workshop-Part-3.md"*
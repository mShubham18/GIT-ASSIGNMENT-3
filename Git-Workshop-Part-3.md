# Git Workshop Assignment

## Objective
Complete the following tasks using Git. Document each step with a screenshot in the markdown file and provide the commands used along with a brief explanation. If you encounter commands that were not covered in the sessions, refer to the provided resources and include them in your documentation.

## Assignment: Git Commands and Concepts

### Scenario 1: Conflict Resolution
**Task:** Imagine you and your teammate are working on the same file, `project.txt`. Both of you make changes to the same lines and commit them. Let’s say your teammate’s changes are merged first. And now when you try to merge your changes, a merge conflict occurs.

**Expected result:** 
Changes from both branches should be included in the file in the main branch. The changes should be included in the sequence: first your teammate’s changes and then the changes made by you.

**Steps to create a conflict:**
1. Create a repository and add a file named `project.txt`.
2. Create two branches in the repository.
3. Make changes to the same line and in the same file in both branches.
4. Commit the changes in both branches.
5. Merge one branch into the main first and then try to merge the second branch.
6. Understand the message that appears when you try to merge the second branch and explain that message. In case of conflicts explain the steps taken to resolve the conflict.

### Scenario 2: Add Files and Commit Together
**Task:** You have worked on multiple files and want to add them and commit using a single command.

**Steps:**
1. Add all files to the staging area and commit them with a single command.
2. Verify the commit by checking the commit log.

### Scenario 3: Include Additional Commit in the Previous Commit Message
**Task:** You have just made a commit but realize you forgot to include a file and make a small typo correction. Instead of creating a new commit, you can amend the last commit to include these changes without altering the commit message. Also verify the amended commit by checking the commit log.

**Steps:**
1. Create and commit initial files.
2. Make additional changes.
3. Stage the changes and amend the last commit.
4. Verify the amended commit by checking the commit log.

### Scenario 4: Stash Command
**Task:** You are working on a feature but need to quickly switch to another task without committing your current changes.

**Steps:**
1. Make changes to a file but do not commit them.
2. Stash the changes.
3. Verify that your working directory is clean.
4. Apply the stashed changes back.
5. Experiment with other stash commands like `stash list`, `stash pop`, and `stash drop`.

**References:**
- [Git Stash Documentation](https://git-scm.com/docs/git-stash)
- [Working with Git Stash - Medium](https://medium.com/@artisingh656/working-with-git-stash-bb363b006e)

### Scenario 5: Use of .gitignore
**Task:** You have files in your project that should not be tracked by Git, such as log files or build artifacts.

**Steps:**
1. Create a new repository with files that should and should not be tracked (`tracked_file.txt`, `ignored_file.log`).
2. Create a `.gitignore` file and add patterns to exclude the appropriate files.
3. Verify that the ignored files are not tracked by Git.
4. Explain real-life use cases of `.gitignore`. What type of files are included in it?

### Scenario 6: Revert to Previous Commits
**Task:** You made a mistake in a recent commit and need to revert the changes.

**Steps:**
1. Create a file and commit changes to the file.
2. Make another commit with a mistake.
3. Revert to the previous commit, undoing the mistake.
4. Verify the state of the repository to ensure the revert was successful.

### Scenario 7: Create a Pull Request
**Task:** You have made changes on a feature branch and want to merge them into the main branch via a pull request.

**Steps:**
1. Create a new branch from the main branch and make changes.
2. Push the branch to the remote repository.
3. Create a pull request to merge your feature branch into the main branch.
4. Describe the changes in the pull request.

By completing these tasks, you'll gain hands-on experience with essential Git commands and concepts.

## Questions:

Please answer the following questions briefly by providing use cases.

1. Why do we create branches in a repository and why do we create pull requests instead of merging directly?
2. What is the difference between `git add .` and `git add <filename>`? What will we use when we have changes in multiples but we are not required to add some files?
3. What is the difference between `git fetch` and `git pull`?
4. What is a head in a repository and what does it do?
5. What is the `.git` folder in a repository?
6. What are commit hashes and its use cases?
7. Different ways of syncing a branch with origin.

## Additional Learning Resources
To further explore Git commands and concepts, such as creating and applying patches, you can refer to the following resources:

**Official Git Documentation:**
- [Git Documentation](https://git-scm.com/docs) provides comprehensive guides and references for all Git commands and features.

**Creating and Applying Patches:**
- [Git Tools - Patches from the Pro Git book](https://git-scm.com/book/en/v2/Git-Tools-Patchwork) explains how to create and apply patches in Git.
- [Creating and Applying Patches tutorial from Atlassian](https://www.atlassian.com/git/tutorials/saving-changes/git-patch) offers step-by-step instructions.

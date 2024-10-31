Git Common Commands
-------------------

This section will cover common `git` commands that you will use frequently.

* ``git init``: Initializes a new Git repository. You should run this command in the root directory of your project.
* ``git clone <repository-url>``: Clones a remote repository to your local machine. You should run this command in the directory where you want to store the repository.
* ``git status``: Shows the status of your working directory and staging area.
* ``git add <file>``: Adds a file to the staging area.
* ``git commit -m "<message>"``: Commits the changes in the staging area to the repository.
* ``git push``: Pushes your changes to the remote repository.
* ``git pull``: Pulls changes from the remote repository to your local repository.
* ``git log``: Shows the commit history of the repository.
* ``git branch``: Shows the branches in the repository.
* ``git checkout <branch-name>``: Switches to the specified branch.
* ``git checkout -b <branch-name>``: Creates a new branch and switches to it.
* ``git merge <branch-name>``: Merges the specified branch into the current branch.
* ``git remote -v``: Shows the remote repositories associated with your local repository.
* ``git remote add <name> <url>``: Adds a new remote repository to your local repository.
* ``git remote remove <name>``: Removes a remote repository from your local repository.
* ``git fetch``: Fetches changes from the remote repository.
* ``git reset --hard HEAD~1``: Resets the working directory and staging area to the commit before the last commit.
* ``git reset --soft HEAD~1``: Resets the staging area to the commit before the last commit.
* ``git reset --hard <commit-hash>``: Resets the working directory and staging area to the specified commit.
* ``git blame <file>``: Shows the commit history of a file, including who made each change.
* ``git diff``: Shows the differences between the working directory and the staging area.
* ``git diff --staged``: Shows the differences between the staging area and the repository.
* ``git stash``: Stashes changes in the working directory and staging area.
* ``git stash pop``: Applies the most recent stash to the working directory and staging area.
* ``git stash list``: Shows a list of stashes.
* ``git tag <tag-name>``: Creates a tag for the current commit.
* ``git tag -a <tag-name> -m "<message>"``: Creates an annotated tag for the current commit.
* ``git tag``: Shows the tags in the repository.
* ``git push --tags``: Pushes tags to the remote repository.
* ``git push origin --delete <branch-name>``: Deletes a remote branch.
* ``git branch -d <branch-name>``: Deletes a local branch.
* ``git config --global user.name "Your Name"``: Configures your Git username.
* ``git bisect``: Helps you find the commit that introduced a bug.

These are just a few of the many `git` commands available. You can find more commands and options in the `git documentation <https://git-scm.com/doc>`_.

What's Next? Now that you have learned the basics of `git`, you can move on the next section to learn our team `git` usage specifics.
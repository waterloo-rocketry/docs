Git Best Practices
==================

**For developing features**

1. Prirotize using rebasing over merging. This will help keep the commit history clean and linear.
2. Only the PR owner should merge the PR. (Unless the PR owner is unavailable, then the PR owner should assign another team member to merge the PR.)
3. Feature Branch name rule should be descriptive and follow the structure: `<watid>/<feature-name>`. For example, `j7zang/pic18f26k83-i2c-master-driver`.
4. Open a draft PR as soon as new feature branch is created, and set it as a draft PR, and only remove draft status of the PR when the PR is ready for review.

**For reviewing PR**

1. If you have any concerns or questions about the PR, please discuss them with the PR owner before approving the PR.
2. Make sure you are following the project's revelant standards and guidelines(electrical standard/firmware standard) when reviewing the PR.
3. Provide constructive feedback and suggestions for improvement in the PR comments.
4. Every PR should be reviewed within 3 days of being opened. If you are unable to review the PR within this time frame, please let the PR owner know.

**Specific to software**

1. For every commit message, you should follow the `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ specification. This will help us generate changelogs and version releases automatically.
2. Please configure the develop environment to run the code and test the changes before approving the PR.   

**Contents of a Git repository**

1. `.gitignore` files should be used to exclude files and directories that should not be tracked by Git.
2. `.github/CODEOWENERS` files should be used to specify who is responsible for reviewing and approving changes to specific parts of the codebase. This will help ensure that changes are reviewed by the appropriate team members.

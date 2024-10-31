Team Git Usage Specification
=============================

**Note: This section is for every team member working on a project.**

1. For every commit message, you should follow the `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ specification. This will help us generate changelogs and version releases automatically.
2. Prirotize using rebasing over merging. This will help keep the commit history clean and linear.
3. `.gitignore` files should be used to exclude files and directories that should not be tracked by Git. You can find examples of `.gitignore` files for different languages and frameworks on `Templet <https://www.toptal.com/developers/gitignore>`_.
4. `CODEOWENERS` files should be used to specify who is responsible for reviewing and approving changes to specific parts of the codebase. This will help ensure that changes are reviewed by the appropriate team members.
5. Feature Branch name rule should be descriptive and follow the structure: `<watid>/<feature-name>`. For example, `j7zang/add-git-usage`.
6. Pull requests should be reviewed by at least one other team member before merging. This will help catch bugs and ensure that changes are consistent with the project's coding standards.
7. Only the PR owner should merge the PR. (Unless the PR owner is unavailable, then the PR owner should assign another team member to merge the PR.)

**Note: This section is for code reviewers.**

1. Make sure you are in the `CODEOWNERS` file for the code you are responsible for reviewing.
2. Please configure the develop environment to run the code and test the changes before approving the PR.
3. Make sure you are following the project's coding standards and guidelines when reviewing the code.
4. Provide constructive feedback and suggestions for improvement in the PR comments.
5. Every PR should be reviewed within 3 days of being opened. If you are unable to review the PR within this time frame, please let the PR owner know.
6. If you have any concerns or questions about the PR, please discuss them with the PR owner before approving the PR.
7. Project Lead should decide who and how many reviewers are required for a project.
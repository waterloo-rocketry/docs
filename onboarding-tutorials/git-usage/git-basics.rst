Git Basics
==========

**Note: Git is not Github, they are two different things.**

Git is a distributed version control system, but Github is a web-based platform
based on Git to host our codebase. 

Introduction to Git
-------------------

Git is a distributed version control system that allows you to track changes in
our codebase. It is a powerful tool that can people to work together on the same
codebase without stepping on each other's toes.

There are three main areas where you will interact with Git:

1. **Your local repository** - This is where you will make changes to the codebase.

3. **The staging area** - This is where you will prepare your changes to be committed.

2. **The remote repository** - This is where the codebase is stored and where you will push your changes.

.. graphviz::

    digraph git_flow {
         rankdir=LR;
         node [shape=rectangle];
         Local_Repository -> Staging_Area -> Remote_Repository;
    }


Sometimes you need to collaborate with others on the same codebase. In this case,
we will introduce the concept of branches. A branch is a separate line of development
that allows you to work on a feature without affecting the main codebase. Once you
are done with your feature and reviewed by peer developers, you can merge your branch
back into the main codebase. This is called a **pull request (PR)**.

.. graphviz::

    digraph git_flow {
        rankdir=LR;
        node [shape=circle, style=filled, fontcolor=white, width=0.5, fixedsize=true];

        // Define nodes for the develop branch (yellow)
        Develop1 [label="", color="#FFD700"];
        Develop2 [label="", color="#FFD700"];
        Develop3 [label="", color="#FFD700"];

        // Define nodes for the feature branch (pink)
        Feature1 [label="", color="#FF69B4"];
        Feature2 [label="", color="#FF69B4"];
        Feature3 [label="", color="#FF69B4"];

        // Labels for branches without background
        FeatureLabel [shape=plaintext, label="Feature", fontcolor="#FF69B4"];
        DevelopLabel [shape=plaintext, label="Develop", fontcolor="#FFD700"];
        
        // Arrange labels at the top and align nodes in the same rank
        {rank=same; FeatureLabel -> Feature1 [style=invis]}
        {rank=same; DevelopLabel -> Develop1 [style=invis]}
        {rank=same; Feature1 -> Feature2 -> Feature3}
        {rank=same; Develop1 -> Develop2 -> Develop3}

        // Connect nodes to show the commit flow
        edge [style=solid, color=black];
        Develop1 -> Feature1 [arrowhead=normal];
        Feature3 -> Develop2 [arrowhead=normal];
    }

That's it! You now have a basic understanding of Git and how to use it to work
on a codebase.

Installing Git
--------------

To get started with Git, you will need to install Git on your machine. 

* Windows users
    1. You can download Git from the `official Git website <https://git-scm.com/downloads/win>`_.
    2. Run the installer and follow the instructions.
    3. Once installed, you can open Git Bash to start using Git.
    4. You can verify that Git is installed by running:
         ``git --version``

* Mac users
    1. Run the following command in your terminal:
       ``xcode-select --install``
    2. xcode-select will prompt you to install the command line developer tools. Click "Install".
    3. Command line developer tools include Git. You can verify this by running:
         ``git --version``

* Linux users
    1. Run the following command in your terminal:
       ``sudo apt-get install git``
    2. You can verify that Git is installed by running:
         ``git --version``

Once you have Git installed, you need to configure your Git username and email.
This is important because every Git commit will use this information to identify
you as the author of the commit.

To configure your Git username and email, run the following commands:

.. code-block:: bash

    git config --global user.name "Your Name"
    git config --global user.email "

Now you are ready to start using Git!

Github Repository
-----------------

We use Github to host our codebase. Github is a web-based platform that allows
you to store and manage your codebase. It also provides tools for collaboration
such as pull requests, issues, and project boards.

To connect your local repository to the remote repository on Github, you will
need to create a Github account and get upload your public SSH key to Github.

To create a Github account, go to the `Github website <https://github.com>`_ and
follow the instructions to create an account.

SSH Key is a secure way to connect to Github without having to enter your
username and password every time. To generate an SSH key, run the following
command in your terminal:

.. code-block:: bash

    ssh-keygen -t rsa -b 4096 -C "github-verify-ssh"

This command will generate an SSH key pair. You will be prompted to enter a
passphrase. You can leave it blank if you don't want to enter a passphrase.

Once the SSH key is generated, you can add it to your SSH agent by running:

.. code-block:: bash

    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_rsa

Now you can copy the public SSH key to your clipboard by running:

.. code-block:: bash

    cat ~/.ssh/id_rsa.pub | pbcopy

Now you can add the SSH key to your Github account. Go to your Github account
settings, click on "SSH and GPG keys", and click on "New SSH key". Paste the
public SSH key into the text box and click "Add SSH key".

Now you are ready to connect your local repository to the remote repository on
Github.

Clone Onboarding Repository
---------------------------

Run the following command to clone the onboarding repository:

.. code-block:: bash

    git clone https://github.com/waterloo-rocketry/software-onboarding.git

Read the README.md file in the repository to get started with the onboarding process.

Congratulations! You have enough knowledge to get started with Git and Github. To check 
out Git Commands, go to the next page.
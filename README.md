# Docs for Waterloo Rocketry Software and Electrical Projects
This repository contains the documentation for the software and electrical projects developed by the Waterloo Rocketry team. The documentation is written in reStructuredText and generated using Sphinx.

## For Developers setting up Sphinx Environment
This guide will help you set up a Sphinx environment for generating project documentation. Sphinx is a powerful tool that converts reStructuredText files into various output formats HTML, we can use it to create professional-looking documentation for our projects.

## Prerequisites
- Python: Ensure Python (3.6 or higher) is installed. 

## Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone --recurse-submodules git@github.com:waterloo-rocketry/docs.git
```

## Step 2: Set up and activate a Virtual Environment
Create a new virtual environment in the project directory:
```bash
python -m venv venv
source venv/bin/activate
```

## Step 3: Install Sphinx and RtD Theme
To install Sphinx, run the following command:
```bash
pip install sphinx
pip install sphinx_rtd_theme
```

## Step 4: Build the Documentation
To generate HTML documentation, use the make html command:
```bash 
make html
```

## Step 5: View the Documentation
Open index.html from the _build/html directory in your web browser:
```bash
open _build/html/index.html
```

## Troubleshooting
- If you encounter missing dependencies or syntax errors, ensure that your Python environment is correctly set up and all necessary packages are installed.

## Bonus: Preview Documentation (VS Code)
To preview the reStructuredText files in VS Code, install the following extension:
- RST Preview: https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext
https://marketplace.visualstudio.com/items?itemName=tht13.rst-vscode

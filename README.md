# basic-python-sample
Learn some basic python, this guide covers the following.
- Environment Setup (Virtual Environment)
- Sample codes
- Executing sample codes
- Python Linters

# pip
It is a package management system used to install and manage packages in Python. For Python3 the command `pip3` is used.

## installing new package/library
Use command `pip3 install <some-package-name>` to install libraries you need in your project. It is advisable that you are in your project's `virtual env` when installing your project dependencies. (section: [virtual env (venv)](#virtual-env-venv))


# virtual env (venv)
Python usually installs project dependencies (packages/libraries) in a shared directory. Virtual env will ensure that your project dependencies are isolated and would not be contaminated with different versions from other projects.

## installing
Use `pip3 install virtualenv` to install virtual environment

## creating project virtual env
If your project environment still does not have the virtual env setup yet, you may use

`virtualenv -p python3 venv`

to generate files needed for virtual env. The files would be located a folder named `venv` but this should be added to `.gitignore` and should NOT be committed.

## activate virtual env
Once (or if) your project's virtual env is already setup, use

`source venv/bin/activate`

to activate virtual env. Once activated, any `python3` or `pip3` commands will run in an isolated environment.

## storing the list of project dependencies
Venv uses `requirements.txt` file to know which packages/libraries does your project need. If on a new python project or have installed new packages for your project, it is usually generated or updated by using the command.

`pip3 freeze > requirements.txt`

That will gather all package name and version installed and store them into the `requirements.txt` file.

## installing project dependencies from requirements.txt
If `requirements.txt` already exist and you just need for the dependencies to be installed on your virtual env, you may use the command

`pip3 install -r requirements.txt`.

## exiting virutal env
Use the command `deactivate` to exit your project's isolated environment.

# running the sample code
We'll use Python 3 with the command `python3`.

Run the sample code with the command `python3 sample/call_service_and_print.py 1`.

This will do a GET request to a public API and print out the result. The number `1` at the end is the ID of the ToDo item, you may replace it with any number.


# python linter
## linter virtual env
It is advisable to have a separate virtual env for linters see section: [virtual env (venv)](#virtual-env-venv).
- Create linter virtual env with the command `virtualenv -p python3 lintervenv`.
- Activate the linter venv with the command `source lintervenv/bin/activate`
- If you've updated the linter library, save it with the command `pip3 freeze > linterrequirements.txt`
- Otherwise to install the linter libraries while in your lintervenv execute `pip3 install -r linterrequirements.txt`

## bandit
Bandit is a tool designed to find common security issues in Python code. https://pypi.org/project/bandit/

To install (if not yet in linterrequirements.txt) `pip3 install bandit`

Run bandit with `bandit -r sample`

## flake8
Flake8 is a style linter tool to make sure your codes looks clean. http://flake8.pycqa.org/en/latest/

To install (if not yet in linterrequirements.txt) `pip3 install flake8`

Run flake8 with `flake8 sample`

DeepGameEngine
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/davidkastner/deepgameengine/workflows/CI/badge.svg)](https://github.com/davidkastner/deepgameengine/actions?query=workflow%3ACI)
[![Documentation Status](https://readthedocs.org/projects/deepgameengine/badge/?version=latest)](https://deepgameengine.readthedocs.io/en/latest/?badge=latest)



## Table of Contents
1. **Overview**
2. **Installation**
    * Creating python environment
    * Installing games
    * Setup developing environment
3. **What is included?**
    * File structure
    * Command line interface
4. **Documentation**
    * Update documentation
    * Examples
5. **Developer Guide**
    * GitHub refresher


## 1. Overview
DeepGameEgine (dge) is an artificial intelligence for playing simulated games.

## 2. Installation
Install the package by running the follow commands inside the repository.
This will perform a developmental version install.
It is good practice to do this inside of a virtual environment.
A yaml environmental file has been created to automate the installation of dependencies.

### Setup developing environment
Remember to update your GitHub [ssh keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

```
git clone git@github.com:davidkastner/deepgameengine.git
cd DeepGameEngine
```


### Creating python environment
All the dependencies can be loaded together using the prebuilt environment.yml.
Compatibility is automatically tested for python versions 3.8 and higher.
Installing all packages together via the yaml will produce a more robust and efficient environment.

```
conda env create -f environment.yml
conda activate dge # You may need to use source activate qa
```

### Install pyQMMM package
Next, we will perform an development install:

```
python -m pip install -e .
```

## 3. What is included?
### File structure
This is the the package structure for reference and its included modules.

```
.
|── cli.py          # Command-line interface entry point
├── docs            # Readthedocs documentation site
├── dge             # Directory containing the playable simulations
│   ├── game_1
│   ├── game_2
│   ├── game_3
│   └── game_4
└── ...
```

### Command Line Interface
The contents of the library are designed to be navigated through the commandline interface.
Add the following line to your bash.rc

```
alias dge='python /the/path/to/deepgameegine/cli.py'
```

Now you can call the DeepGameEngine package CLI from anywhere with:
```
dge
```


## 4. Documentation
### Update documentation
Run the following commands to update the ReadTheDocs site:

```bash
make clean
make html
```


## 5. Developer guide
### GitHub refresher for those who would like to contribute
#### Push new changes

```
git status
git pull
git add -A .
git commit -m "Change a specific functionality"
git push -u origin main
```

#### Making a pull request
```
git checkout main
git pull

# Before you begin making changes, create a new branch
git checkout -b new-feature-branch
git add -A
git commit -m "Detailed commit message describing the changes"
git push -u origin new-feature-branch

# Visit github.com to add description, submit, merge the pull request

# Once finished on github.com, return to local
git checkout main
git pull

# Delete the remote branch
git branch -d new-feature-branch
```

#### Handle merge conflict

```
git stash push --include-untracked
git stash drop
git pull
```

### Copyright
Copyright (c) 2022, David W. Kastner


#### Acknowledgements
[MolSSI](https://github.com/molssi/cookiecutter-cms) version 1.1.

# Table of Contents

1. [Setup](#setup-and-run)
2. Create a issue ticket with a feature or bug.
3. Create a branch called ``feature/[feature]``, ``bugfix/[bug]`` to add changes on the code.
4. Update ``feature/[feature]`` or ``bugfix/[bug]`` and commit with the issue number reference, e.g.:
> git commit -m "solves commit #5"
5. [Pre PR](#run-tests,-check-pep8-and-check-for-security-issues)
6. After ``Pre PR``, push your modifications to your branch and send a *PR* (Pull Resquest) to master.


## Setup and run

- Tools required:
  - [Python3.7](https://www.python.org/downloads/)


- Using virtualenv and setuptools:

```bash
python3 -m venv venv
source venv/bin/activate
(venv) pip install -e .[dev]
(venv) findex
```

## Run tests, check PEP8 and check for security issues

```
(venv) pytest core
(venv) flake8 core
(venv) bandit core -r
```

## Authors

- Dayanne Fernandes:
  - Github : [@Dayof](https://github.com/Dayof)
  - E-mail : dayannefernandesc@gmail.com

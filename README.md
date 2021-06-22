# GENERIC  APP 1.0

## Contacts

Developer: Gabriele Murara: gabriele@murara.computer

## Introduction

GENERIC APP is the start point for implement a python project with arguments
parser, logging and database connection.

## Requirements

PYTHON = 3.6.9 to be run as a script.

## Installation

Create a virtualenv for Python 3.6.9 and start it eg.:

```
$ python3 -m venv yourprojectname_venv
$ cd yourprojectname_venv
$ . bin/activate
```

Install dependences with pip:

```
$ pip install -r requitements.txt
```

It will install:
* wheel
* python-json-logger==0.1.11
* requests
* mysql-connector-python==8.0.25

## Configuration:

Configuration files must be stored in settings/ folder

There are 3 files with configuration values:

1) _settings/constants.py_: is the file that contains constants about app
informations;
2) _settings/defaults.py_: is the file that contains values about logging;
3) _settings/sample.py_: is the file that contains samples and overwrites
_settings/defaults.py_;

#### Personalization:

1) change values in _settings/constants.py_ with your favourites;
2) copy _settings/sample.py_ to _settings/your_setting_filename.py_ and
valorize with your real values ("your_setting_filename" is the value that will
be passed when you start the app);

## Implementation:

The _main.py_ is the starting point for your app. The last two rows instance
and run the App class. You can create your own class o extend the existing
_App_ class.
In the _getOptions()_ function you can add arguments and options retrieved by
shell and implement the logic.

#### Personalization:

If you dont need a database connection you can remove:

1) _mysql-connector-python_ from _requirements.txt_;
2) _import mysql.connector_ from _config.py_;
3) the _init_db_connection() and the _get_db_connection() from _config.py_;
4) the call to _init_db_connection() into the _init_configuration() function;

## Execution

Run with:

```
$ python main.py --help
```

for the full list of options

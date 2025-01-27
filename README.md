# LoggingUtil Python 
A custom made python logging utility, designed for Discord.py/Py-Cord 


## Requirements
> python-dotenv==1.0.1

## How to setup
This system uses a .ENV style configuration, however I will be adding a .JSON, or a .INI configuration option later in the project's timeline. 

### EXAMPLE `.ENV`
```
# Logging Configeration
# The path must be accesable, by default the path is set to logging/logs folder, you can change it to any path you want as long as it is accesable.

LOG_PATH = "logging_\logs"
# If you don't want to log the database queries, set this to False, by default it is set to True
LOG_DATABASE = True 
```

### Basic Usage

Non-Class Usage.
```
from logging_.logger import Logger

logs = Logger()

# Debug On
#logs.DEBUG = True
# Debug Off
# Debug is by default turned off in the Logger File itself, to change this un comment the `logs.DEBUG = True` to activate console logging by default.

# Log To File with no print

# This will display a output like so [{datetime.datetime.now()}][{function}][{user}] {message}
logs.log("I am logging a message", "main_system", "Administrator", False)

# Log to File with Print Enabled

# This will display a output like so [{datetime.datetime.now()}][{function}][{user}] {message}
logs.log("I am logging a message to console and file", "main_system", "Administrator", True)

####### ERROR LOGGING #######


# Log a Error to File with no Print

# This will display a output like so ERROR: [{datetime.datetime.now()}][{function}][{user}] {message}
# Errors do not log to console unless requested 
logs.log("I am logging a message that is a error", "main_system", "Administrator", False, True)

# Log a Error to File with Print

# This will display a output like so ERROR: [{datetime.datetime.now()}][{function}][{user}] {message}
# Errors do not log to console unless requested 
logs.log("I am logging a message that is a error", "main_system", "Administrator", True, True)

####### Secondary Logging #######

# The logging controller contains a secondary logging system, this can be accessed by placing default=False in the log params


# This will display a output like so ERROR: [{datetime.datetime.now()}][{function}][{user}] {message}
# Errors do not log to console unless requested 
# This will log to a second file outside of the default file.
logs.log("I am logging a message that is a error", "main_system", "Administrator", True, True, default=False)

```
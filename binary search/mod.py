#modules:is basically a file containing python code.
# A module can define functions, classes, and variables that can be reused in other python programs.
# To use a module, you need to import it using the import statement.
# In this example, we will create a module called mod.py and import it in another file.
#in python thre are two types of modules:
# 1. built-in modules: these are modules that come with python and can be used without installing any additional packages.
# 2. user-defined modules: these are modules that you create yourself and can be used in your own programs.
# In this example, we will create a user-defined module called mod.py and import it in another file.
# This is a user-defined module called mod.py

import datetime
from datetime import date
import time






# Function to get the current time
def current_time():
    """Returns the current time."""
    return datetime.datetime.now().time()
print("Current time:", current_time())
# Function to get the current date
def current_date():
    """Returns the current date."""
    return date.today()
print("Current date:", current_date())
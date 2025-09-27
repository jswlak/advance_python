## What are Modules?
    A module is just a Python file containing code — functions, classes, variables — that you can reuse in other Python scripts

## What are Packages?
    A package is a folder containing Python modules, plus a special __init__.py file (can be empty) that tells Python “this is a package”

Folder structure:
    my_package/
        __init__.py
        math_utils.py
        string_utils.py


## What is __init__.py?

    __init__.py is the initializer for a package.

    It marks a folder as a package.

    You can control what is imported when someone does from my_package import *.

    Can contain package-level code.
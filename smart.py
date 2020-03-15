#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
from importlib import import_module
import imported_libs
import app


# the app module is loaded dynamically, we do not build this module by pyinstaller
# for this reason, all the modules imported by app should be imported by this file again
# NEVER FORGOT !!!

sys.path.append(os.path.dirname(sys.argv[0]))
app = import_module('app')

if __name__ == '__main__':
    app.main()

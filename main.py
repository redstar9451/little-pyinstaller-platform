#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from importlib import import_module
import imported_libs


# the app module is loaded dynamically, we do not build this module by pyinstaller
# for this reason, all the modules imported by app should be imported by this file again
# NEVER FORGOT !!!

sys.path.append(os.path.dirname(sys.argv[0]))
app_name = sys.argv[1]
app = import_module('app.' + app_name)

if __name__ == '__main__':
    app.main()

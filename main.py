#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from importlib import import_module
import imported_libs


# the app module is loaded dynamically, we do not build this module by pyinstaller
# for this reason, all the modules imported by app should be imported by this file again
# NEVER FORGOT !!!

if __name__ == '__main__':
    if len(sys.argv) == 1:
        raise Exception("missing module name")
    
    current_dir = os.path.dirname(sys.argv[0])
    app_dir = os.path.join(current_dir, 'app', sys.argv[1])
    sys.path.extend([current_dir, app_dir])
    app_name = sys.argv[1]
    app = import_module('app.' + app_name)
    sys.argv = sys.argv[1:]

    app.main()
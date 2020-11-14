#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import os
from child_folder.test import func_in_child_folder

def main():
    print(sys.argv)
    print(sys.path)
    print(os.getcwd())

    print('hello world')
    func_in_child_folder()


if __name__ == '__main__':
    main()

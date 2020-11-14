#!/usr/bin/env python
#-*- coding; utf8 -*-
import os
import sys

if __name__ == '__main__':
    python_file = sys.argv[1]
    while True:
        try:
            import imported_libs
            break
        except ModuleNotFoundError as e:
            print(f'remove not found module {e.name}')
            os.system(f"sed -E -i '/\s*from\s+{e.name}(\.|\s)+/d' {python_file}")
            os.system(f"sed -E -i '/\s*import\s+{e.name}(\.|\s|$)+/d' {python_file}")
        except ImportError as e:
            name = e.msg.split()[-1].strip("'")
            print(f'remove not found module {name}')
            os.system(f"sed -E -i '/\s*from\s+{name}(\.|\s)+/d' {python_file}")
            os.system(f"sed -E -i '/\s*import\s+{name}(\.|\s|$)+/d' {python_file}")

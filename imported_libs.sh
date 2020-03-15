#!/bin/sh

target_dir=app

[ -f ./imported_libs.py ] && rm ./imported_libs.py
grep -E '^\s*import\s+\S+\s*$' ${target_dir}/ -R -h -o | sort | uniq > ./imported_libs.py
grep -E '^\s*from\s+\S+\s+import\s+\S+\s*$' ${target_dir}/ -R -h -o | sort | uniq >> ./imported_libs.py
# remove local import code lines, this method is not perfect, only erase the lines like 'from .xxx import yyy'
sed -E -i '/from \s*\./d' imported_libs.py

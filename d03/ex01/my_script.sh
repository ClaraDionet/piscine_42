#!/bin/sh

pip --version
pip install -t local_lib --upgrade git+https://github.com/jaraco/path.py.git > log_install.log

python3 my_program.py
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess

SUCCESS = True

# Python check
try:
    print(sys.version, file=sys.stderr)
    # Require Python 3.13 or higher
    if sys.version_info < (3, 13):
        raise ValueError("Error: This script requires Python 3.13+.")
except ValueError as e:
    print(e, file=sys.stderr)
    SUCCESS = False

# Pandas check
try:
    import pandas as pd
    print('pandas dataframe:')
    print(
        pd.DataFrame({
            "Greeting": ["Hello", "Bonjour", "Hola"],
            "Target": ["World", "Monde", "Mundo"]
        })
    )
    print()
except ImportError as e:
    print(e, file=sys.stderr)
    SUCCESS = False

# Samtools check
try:
    subprocess.check_output('which samtools', shell=True)
    print('samtools output:')
    print(
        subprocess.check_output('samtools --help', shell=True).decode()
    )
    print()
except subprocess.CalledProcessError as e:
    print(e, file=sys.stderr)
    SUCCESS = False


if SUCCESS:
    print("All dependencies installed!")
    sys.exit(0)
else:
    print("Missing dependencies")
    sys.exit(1)


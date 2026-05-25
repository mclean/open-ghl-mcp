"""Launcher that ensures the project root is on sys.path so `src.main` resolves
regardless of the caller's working directory.
"""

import os
import runpy
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
os.chdir(ROOT)

runpy.run_module("src.main", run_name="__main__")

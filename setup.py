#!/usr/bin/python3
from setuptools import setup, find_packages

setup(
    name="TurtleFixLexer",
    version="0.1",
    packages=find_packages(),
    entry_points="""
[pygments.lexers]
turtle-fix = turtle-fix:TurtleFixLexer
""",
)

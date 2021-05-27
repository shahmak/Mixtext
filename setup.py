import os
import io

from setuptools import setup,find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
with io.open('./README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name = "Mixext",
    version = "0.0.1",
    author = "Jiaao Chen",
    description = ("Linguistically-Informed Interpolation of Hidden Space for Semi-Supervised Text Classification"),
    license = "MIT",
    keywords = "Mixtext",
    url = "https://github.com/shahmak/Mixtext.git",
    packages=find_packages(),
#     long_description=read('README.md'),
    
)

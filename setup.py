import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "MixText",
    version = "0.0.1",
    author = "Jiaao Chen"
    author_email = "jchen896@gatech.edu",
    description = ("Linguistically-Informed Interpolation of Hidden Space for Semi-Supervised Text Classification"),
    license = "MIT",
    keywords = "MixText",
    url = "https://github.com/shahmak/Mixtext.git",
    packages=['code'],
    long_description=read('README.md'),
    
)
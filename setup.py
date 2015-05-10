import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mete",
    version = "0.0.1",
    author = "Gerrit Giehl",
    author_email = "gerrit.giehl@email-versand.net",
    description = (""
                   ""),
    license = "AGPL",
    keywords = "mete",
    url = "https://github.com/r4mp/mete_python_cherrypy_jinja2",
    packages=['mete', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: AGPL License",
    ],
)

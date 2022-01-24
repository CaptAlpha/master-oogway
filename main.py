#!/usr/bin/env python3
"""
Automated Directory Structure Builder, By The Grace of Master Oogway

Usage: main.py project_name --type project_type
"""

__authors__ = "Arhit Bose Tagore, Priyanshu Kumar"
__version__ = "0.1.0"
__license__ = "MIT"

import sys
import os
import click


def flask(name):
    """ Flask entry point of the app """
    cwd = os.getcwd()
    directory = name
    path = cwd + "/" + directory

    try:
        if not os.path.exists(path):
            os.makedirs(path)

        if not os.path.exists(path + '/templates'):
            os.makedirs(path + '/templates')

        if not os.path.exists(path + '/templates/auth'):
            os.makedirs(path + '/templates/auth')

        if not os.path.exists(path + '/templates/blog'):
            os.makedirs(path + '/templates/blog')

        if not os.path.exists(path + '/static'):
            os.makedirs(path + '/static')

        file = open(path + "/__init__.py", "w")
        file.write("""
from setuptools import setup

setup(
    name='yourapplication',
    packages=['yourapplication'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)


        """)
        file.close()

        file = open(path + "/app.py", "w")
        file.write("""
from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
        """)

        file.close()


    except OSError as error:
        print(error)


def django(name):
    """ Django entry point of the app """
    cwd = os.getcwd()
    directory = name
    path = cwd + "/" + directory

    try:
        if not os.path.exists(path):
            os.makedirs(path)

        if not os.path.exists(path + '/docs'):
            os.makedirs(path + '/docs')

        if not os.path.exists(path + '/scripts'):
            os.makedirs(path + '/scripts')

        if not os.path.exists(path + '/' + name):
            os.makedirs(path + '/' + name)

        if not os.path.exists(path + '/' + name + '/apps'):
            os.makedirs(path + '/' + name + '/apps')

        if not os.path.exists(path + '/' + name + '/apps/accounts'):
            os.makedirs(path + '/' + name + '/apps/accounts')

        if not os.path.exists(path + '/' + name + '/settings'):
            os.makedirs(path + '/' + name + '/settings')

        if not os.path.exists(path + '/static'):
            os.makedirs(path + '/static')

        if not os.path.exists(path + '/templates'):
            os.makedirs(path + '/templates')

        if not os.path.exists(path + '/tests'):
            os.makedirs(path + '/tests')

        if not os.path.exists(path + '/tmp'):
            os.makedirs(path + '/tmp')

        file = open(path + "/setup.py", "w")
        file.write("""
from setuptools import setup

setup(
    name='yourapplication',
    packages=['yourapplication'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)


        """)
        file.close()

        file = open(path + "/requirements.txt", "w")
        file.write(""" """)
        file.close()

        file = open(path + "/requirements_dev.txt", "w")
        file.write("""  """)
        file.close()

        file = open(path + "/pytest.ini", "w")
        file.write(""" """)
        file.close()

        # file = open(path + "/apps/__init__.py", "w")
        # file.write(""" """)
        # file.close()

        # file = open(path + "/settings/__init__.py", "w")
        # file.write(""" """)
        # file.close()

        # file = open(path + "/settings/production.py", "w")
        # file.write(""" """)
        # file.close()

        # file = open(path + "/settings/development.py", "w")
        # file.write(""" """)
        # file.close()

        # file = open(path + '/' + name + "/__init__.py", "w")
        # file.write(""" """)
        # file.close()

        # file = open(path + '/' + name + "/urls.py", "w")
        # file.write(""" """)
        # file.close()

        # file = open(path + '/' + name + "/wsgi.py", "w")
        # file.write(""" """)
        # file.close()

    except OSError as error:
        print(error)

# def react(lst):
#     pass

# def angular(lst):
#     pass

@click.command()
@click.argument('name')
@click.option('--type', type=str, help="The type of project you are going to work on.")
def run(type, name):
    """ This is executed when run from the command line """
    # lst = sys.argv

    if type.casefold() == 'flask':
        flask(name)

    if type.casefold() == 'django':
        django(name)

    if type.casefold() == 'react':
        react(name)


if __name__ == "__main__":
    run()

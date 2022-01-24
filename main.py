#!/usr/bin/env python3
"""
Automated Directory Structure Builder, By The Grace of Master Oogway

Usage: main.py project_name --type project_type
"""

__authors__ = "Arhit Bose Tagore, Priyanshu Kumar"
__version__ = "0.1.0"
__license__ = "MIT"

# TODO:
# initialise all the .py files in django

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

        arr_flask = ['/templates', '/templates/auth', '/templates/blog', '/static']

        for i in arr_flask:
            if not os.path.exists(path + i):
                os.makedirs(path + i)

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

        arr_django1 = ['/docs', '/scripts', '/static', '/templates', '/tests', '/tmp']

        for i in arr_django1:
            if not os.path.exists(path + i):
                os.makedirs(path + i)

        if not os.path.exists(path + '/' + name):
            os.makedirs(path + '/' + name)

        arr_django2 = ['/apps', '/apps/accounts', '/settings']

        for i in arr_django2:
            if not os.path.exists(path + '/' + name + i):
                os.makedirs(path + '/' + name + i)

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

        arr_django3 = ['/requirements.txt','/requirements_dev.txt','/pytest.ini']

        for i in arr_django3:
            file = open(path + i, "w")
            file.write(""" """)
            file.close()

        # Haven't added .py files in loop as we need to initialise all these with code

        file = open(path + "/apps/__init__.py", "w")
        file.write(""" . """)
        file.close()

        file = open(path + "/settings/__init__.py", "w")
        file.write(""" . """)
        file.close()

        file = open(path + "/settings/production.py", "w")
        file.write(""" . """)
        file.close()

        file = open(path + "/settings/development.py", "w")
        file.write(""" . """)
        file.close()

        file = open(path + '/' + name + "/__init__.py", "w")
        file.write(""" . """)
        file.close()

        file = open(path + '/' + name + "/urls.py", "w")
        file.write(""" . """)
        file.close()

        file = open(path + '/' + name + "/wsgi.py", "w")
        file.write(""" . """)
        file.close()

    except OSError as error:
        print(error)


def react(name):
    """ React entry point of the app """
    cwd = os.getcwd()
    directory = name
    path = cwd + "/" + directory

    try:
        if not os.path.exists(path):
            os.makedirs(path)
        arr_react1 = ['/common','/feed','/profile']

        for i in arr_react1:
            if not os.path.exists(path + i):
                os.makedirs(path + i)

        arr_react2 = ['/common/Avatar.js', '/common/Avatar.css', '/common/APIUtils.js',
                      '/common/APIUtils.test.js', '/feed/index.js', '/feed/Feed.js',
                      '/feed/Feed.css', '/feed/FeedStory.js', '/feed/FeedStory.test.js',
                      '/feed/FeedAPI.js', '/profile/index.js', '/profile/Profile.js',
                      '/profile/ProfileHeader.js', '/profile/ProfileHeader.css', '/profile/ProfileAPI.js']

        for i in arr_react2:
            file = open(path + i, "w")
            file.write(""" . """)
            file.close()

    except OSError as error:
        print(error)


def angular(name):
    """ Angular entry point of the app """
    cwd = os.getcwd()
    directory = name
    path = cwd + "/" + directory

    try:
        if not os.path.exists(path):
            os.makedirs(path)

        arr_react1 = ['/src','/node_modules','/src/app','/src/assets','/src/environments']

        for i in arr_react1:
            if not os.path.exists(path + i):
                os.makedirs(path + i)

        arr_react2 = ['/.editorconfig', '/.gitignore', '/README.md',
                      '/angular.json', '/package.json', '/package-lock.json',
                      '/tsconfig.json', '/src/index.html', '/src/main.ts',
                      '/src/polyfills.ts', '/src/styles.sass', '/src/test.ts',
                      '/src/app/app.component.ts', '/src/app/app.component.html', '/src/app/app.component.css',
                      '/src/app/app.component.spec.ts','/src/app/app.module.ts']

        for i in arr_react2:
            file = open(path + i, "w")
            file.write(""" . """)
            file.close()

    except OSError as error:
        print(error)

# def flutter(lst):
#     pass

# def rubyonrails(lst):
#     pass

# def vue(lst):
#     pass

# def laravel(lst):
#     pass

# def meteor(lst):
#     pass

# def express(lst):
#     pass

# def spring(lst):
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

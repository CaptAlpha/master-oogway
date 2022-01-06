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
    path = cwd+"/"+directory

    try:
        if not os.path.exists(path):
            os.makedirs(path)
        
        if not os.path.exists(path+'/templates'):
            os.makedirs(path+'/templates')
        
        if not os.path.exists(path+'/templates/auth'):
            os.makedirs(path+'/templates/auth')
        
        if not os.path.exists(path+'/templates/blog'):
            os.makedirs(path+'/templates/blog')

        if not os.path.exists(path+'/static'):
            os.makedirs(path+'/static')

    except OSError as error:
        print(error)
        
# def django(lst):
#     pass

# def react(lst):
#     pass

# def angular(lst):
#     pass

@click.command()
@click.argument('name')
@click.option('--type',type=str,help="The type of project you are going to work on.")
def run(type,name):
    """ This is executed when run from the command line """
    #lst = sys.argv

    if type.casefold() == 'flask':
        flask(name)


if __name__ == "__main__":
    run()
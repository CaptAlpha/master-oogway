#!/usr/bin/env python3
"""
Automated Directory Structure Builder, By The Grace of Master Oogway

Usage: python main.py flask project_name
"""

__authors__ = "Arhit Bose Tagore, Priyanshu Kumar"
__version__ = "0.1.0"
__license__ = "MIT"

import sys
import os 

def flask(lst):
    """ Flask entry point of the app """
    cwd = os.getcwd()
    directory = lst[2]
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
        



if __name__ == "__main__":
    """ This is executed when run from the command line """
    lst = sys.argv

    if lst[1].casefold() == 'flask':
        flask(lst)
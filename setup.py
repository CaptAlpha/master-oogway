from setuptools import setup

setup(
    name='master-oogway',
    version='0.1.0',
    py_modules=['main.py'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        hello=hello:cli
    ''',
)
# Development guidelines and notes

## Development notes for myself

- Now using pipenv :)
- don't build using pipenv run
- use `python setup.py install` instead
- then it with `aalog --help` or something similar

## Todo

A bunch of things I need to do

### Add user configuration

- using configparser

### Add SQL schema migration create/setup files

### Troubleshooting

_Can't import click or peewee modules?_  Try a pip install
Something is not right with the setup.py and so these modues don't appear to get imported
as expected

_No colour on response?_
No colour seems to be normal when running via aalog_test.py
On windows try _pip install colorama_ for support
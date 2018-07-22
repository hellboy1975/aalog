# Development guidelines and notes

## Development notes for myself:

- Now using pipenv :)
- don't build using pipenv run
- use `python setup.py install` instead
- then it with `aalog --help` or something similar

## Todo:
A bunch of things I need to do
### Add user configuration

- use yaml file

### Add SQL schema migration create/setup files

### Troubleshooting
_Can't import click or peewee modules?_  Try a pip install
Something is not right with the setup.py and so these modues don't appear to get imported
as expected


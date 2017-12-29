"""
Contains the entry points for the aalog cli
"""
import click
# from . import db as db # tried and failed
# from . import dbconf as dbconf
# from aalog.dbconf import *
from . import dbconf
from . import create_tables

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    """
    The aaLog CLI interface gives you a range of commands that are
    used in interact with the aalog Database.
    """
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@cli.command()
def init():
    """ (sometimes) Initialises aaLog """
    click.echo("Initialising aaLog...")

    # TODO: Check to see if aaLog has been initialised previously

    # TODO: check the schema version, and see if we need to update
    # message = db.create_database()
    click.echo('database file: %s' % dbconf.DATABASE)

    create_tables.create_database()

    

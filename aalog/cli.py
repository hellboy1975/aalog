"""
Contains the entry points for the aalog cli
"""
__version__ = '0.1.1'
__author__ = 'Matt Smith'

import click

# from . import db as db # tried and failed
# from . import dbconf as dbconf
# from aalog.dbconf import *
from . import dbconf
from . import create_tables

from .config import SystemConfig, UserConfig

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--debug/--no-debug', default=False)
@click.option('--force', '-f', multiple=True, help="Forces an overwrite if a DB already exists")
def cli(debug, force):
    """
    The aaLog CLI interface gives you a range of commands that are
    used in interact with the aalog Database.
    """
    # click.echo('Debug mode is %s' % ('on' if debug else 'off'))
    pass


@cli.command('init', short_help="Initialises aaLog")
def init():
    """ Initialises aaLog.  Run this the first time you attempt to use aaLog """
    click.echo("Initialising aaLog...")

    # TODO: Check to see if there is a system.ini config file (there should always be!)
    # if not we can create one using the defaults
    click.echo("System configuration: ", nl=False)
    system_config = SystemConfig()
    if not system_config.config:
        click.secho("Not found - aborting!", color="red")
        return False

    click.secho("OK", fg='green')

    # Check to see if there is a user.ini config file
    # if not we can create one, prompting the user for some info
    user_config = UserConfig(
        system_config.parser['default']['UserSettingsFile'])
    click.echo("User configuration: ", nl=False)
    if not user_config.config:
        click.secho("Not found", fg="red")
        # TODO: user the user_config class to prompt user for details
        return False
    else:
        click.secho("OK", fg='green')
    
    # TODO: check the schema version, and see if we need to update
    click.echo('Initialise Database...')

    create_tables.create_database()

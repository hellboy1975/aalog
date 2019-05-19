"""
A collection of functions designed to create and initialise the database
"""
import click
from pathlib import Path

from . import region
from . import site

from . import dbconf as dbconf

DB_CREATE_DB_EXISTS = 1
DB_CREATE_SUCCESS = 2
DB_CREATE_OVERWRITE = 3

create_tables_error_codes = {
    1: 'Database file already exists.  Use -f to force an overwrite',
    2: 'Database created',
    3: 'Database created (existing DB overwritten)',
}


def database_exists():
    """ checks for the existence of a database file """
    db_file = Path(dbconf.DATABASE)
    return db_file.is_file()

def create_database():
    """ Create the database """

    click.echo('DB file exists:', nl=False)

    # check if the tables exist first
    if database_exists():
        # TODO: check for the -f flag.  
        # if so then we can create the table anyway
        
        # else return an error message
        click.secho("OK", fg='green')
        click.secho("DB already exists, use the -f flag if you want replace this", fg='yellow')
        return DB_CREATE_DB_EXISTS
    
    click.secho("No", fg='red')
    click.secho("Creating new DB", fg='yellow')
    
    region.create_table()
    site.create_table()

    click.secho("New database created!", fg='green')

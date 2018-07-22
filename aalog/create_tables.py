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

create_tables_error_codes = {
    1: 'Database file already exists.  Use -f to force an overwrite',
    2: 'Database created',
    3: 'Database created (existing DB overwritten)',
}


def database_exists():
    """ checks for the existence of a database file """
    db_file = Path(dbconf.DATABASE)
    click.echo('Locate existing DB file? %s' % db_file.is_file())
    return db_file.is_file()

def create_database():
    """ Create the database """
    # check if the tables exist first
    if database_exists():
        # TODO: check for the -f flag.  
        # if so then we can create the table anyway
        
        # else return an error message
        return DB_CREATE_DB_EXISTS
    
    region.create_table()
    site.create_table()

    return DB_CREATE_SUCCESS

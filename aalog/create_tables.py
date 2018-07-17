"""
A collection of functions designed to create and initialise the database
"""
from . import region
from . import site


def create_database():
    """ Create the database """
    region.create_table()
    site.create_table()

    return "Database created"

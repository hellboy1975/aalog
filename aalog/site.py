"""
Site is a more specific location within a region.
Examples:
* Caving: A specific cave, or network or entrances
* Canyoning: A cluster of canyons, typically attached to a common water catchment or trail head
* Climbing: A specific crag

Dev Note:
Note super happy with the structure of these files.  I'd like to have a
sub module called "model" and then have each model as a .py file.
However when I attempt this I seem to have problems importing these
files.  Need to do more googling...
"""
from peewee import *
from . import dbconf as dbconf
from .region import Region

DB = SqliteDatabase(dbconf.DATABASE)

class Site(Model):
    """ Model for the Site table """
    id = PrimaryKeyField()
    # TODO: Region import isn't working as I'd expect.  Need to research this!
    region_id = ForeignKeyField(Region)
    code = CharField()
    description = CharField()
    type = CharField()

    class Meta:
        """ define the table metadata """
        database = DB  # This model uses the "aalog.db" database.
        indexes = (
            (('code', 'type'), True),  # Note the trailing comma!
        )

    def load_by_id(self):
        """ TODO: make this function work """
        return "true"


def create_table():
    """
    Create the table for the site model
    """
    # This worked, though I'm not sure I understand why I didn't need to DB.connect() first...
    # DB.connect()
    DB.create_tables([Site])

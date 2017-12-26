"""
Region is a broad area for collecting sites.  It typically is smaller than a state.
Examples:
* Caving: Upper South East, Bungonia or Mole Creek.
* Canyoning:  Blue Mountains
* Climbing: Morialta, Arapiles
"""
from .. import db as dbconf
from peewee import *

DB = SqliteDatabase(dbconf.DATABASE)

class Region(Model):
    """ Model for the Region table """
    id = PrimaryKeyField()
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
    Create the table for the region model
    """
    # This worked, though I'm not sure I understand why I didn't need to DB.connect() first...
    # DB.connect()
    DB.create_tables([Region])

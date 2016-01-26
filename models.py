# peewee ORM quickstart documentation : http://docs.peewee-orm.com/en/latest/peewee/quickstart.html
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
from playhouse.shortcuts import model_to_dict

db = SqliteExtDatabase('weather_database.sqlite')

def init_database():
    db.connect()
    db.create_tables([Weather])

class BaseModel(Model):
    class Meta:
        database = db
    # Model instance to JSON conversion
    def json(self):
        return model_to_dict(self)

# Weather table
class Weather(BaseModel):
    lattitude = CharField(max_length=10)
    longitude = CharField(max_length=10)
    temp = CharField(max_length=10)

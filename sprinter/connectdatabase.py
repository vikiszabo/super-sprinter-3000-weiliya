from peewee import *

class ConnectDatabase:
    db = SqliteDatabase("db.sqlite")

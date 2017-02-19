from sprinter.connectdatabase import ConnectDatabase
from peewee import *


class Status(Model):
    name = CharField()

    class Meta:
        database = ConnectDatabase.db


class UserStory(Model):
    title = CharField()
    description = CharField()
    criteria = CharField()
    business_value = CharField()
    estimation = CharField()
    status = ForeignKeyField(Status, related_name='statuses')

    class Meta:
        database = ConnectDatabase.db


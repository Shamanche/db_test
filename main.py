from peewee import *
from datetime import date

db = SqliteDatabase('backgamon.db')

class Player(Model):
    name = CharField()
    viber_id = CharField()
    bitrix_id = IntegerField()
    is_deleted = BooleanField(default=False)
    class Meta:
        database = db

class Game(Model):
    name = CharField()
    date = DateField()
    winner = ForeignKeyField(Player, related_name='players')
    loser = ForeignKeyField(Player, related_name='players')
    win_type = CharField()
    class Meta:
        Database = db

db.connect()
db.create_tables([Player, Game])

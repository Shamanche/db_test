from peewee import *
import psycopg2

HOST = 'localhost'
USER = 'postgres'
PASSWORD = '620514'
DATABASE_NAME = 'smartdb'
PORT = 5432


db = PostgresqlDatabase(database=DATABASE_NAME,
                        host=HOST,
                        port=PORT,
                        user=USER,
                        password=PASSWORD)


class User(Model):
    first_name = CharField(null=True)
    second_name = CharField(null=True)
    bitrix_id = IntegerField(null=True, default=None)
    viber_id = CharField()
    is_admin = BooleanField(default=False)
    is_deleted = BooleanField(default=False)
    is_registred = BooleanField(default=False)
    class Meta:
        database = db
        table_name = 'Users'

def db_create_tables():
    # db.connect()
    db.create_tables([User])


def db_add_user(first_name, second_name, bitrix_id, viber_id, is_admin):
    # db.connect()
    rec = User(first_name=first_name,
               second_name=second_name,
               bitrix_id=bitrix_id,
               viber_id=viber_id,
               is_admin=is_admin)
    rec.save()





# db_create_tables()
db_add_user('Цветков', 'Евгений', 1, 'aaaaaa', True)
db_add_user('Андреев', 'Антон', 2, 'bbbbbb', False)
db_add_user(None, None, None, 'сссссс', False)
from peewee import SqliteDatabase, Model, TextField, TimeField, DateTimeField, ForeignKeyField, PrimaryKeyField, AutoField

db = SqliteDatabase('sqlite_link.db')

class DB(Model):

    class Meta:
        database = db

class FileClass(DB):
    id = AutoField()
    link = TextField(default=None, null=True)

*** def initialize_db(): ***
    
db.connect()
db.create_tables([FileClass], safe = True)
db.close()










# -*- coding: utf-8 -*- 

from peewee import *

db = SqliteDatabase('tree.db')

class Tree(Model):
    id = IntegerField(primary_key=True)
    trunk = TextField(null=False)
    trunk_img = CharField(null=True, max_length=250)
    sheet = TextField(null=False)
    sheet_img = CharField(null=True, max_length=250)
    flower = TextField(null=False)
    flower_img = CharField(null=True, max_length=250)
    fruit = TextField(null=False)
    fruit_img = CharField(null=True, max_length=250)
    seed = TextField(null=False)
    seed_img = CharField(null=True, max_length=250)
    wood = TextField(null=False)
    wood_img = CharField(null=True, max_length=250)
    other = TextField(null=True)
    other_img = CharField(null=True, max_length=250)
    
    class Meta:
        database = db

db.connect()
db.create_tables([Tree])
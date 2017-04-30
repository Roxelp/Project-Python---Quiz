# -*- coding: utf-8 -*-
# quiz_pw/models.py

from app import baza
from peewee import *


class BaseModel(Model):

    class Meta:
        database = baza


class matma_pyt(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()

class matma_odp(BaseModel):
    pnr = ForeignKeyField(
        matma_pyt, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()
    
class polski_pyt(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()

class polski_odp(BaseModel):
    pnr = ForeignKeyField(
        polski_pyt, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()


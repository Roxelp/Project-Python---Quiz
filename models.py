# -*- coding: utf-8 -*-
# quiz_pw/models.py

from app import baza
from peewee import *


class BaseModel(Model):

    class Meta:
        database = baza

class nazwa(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()
    
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
    

class sieci_pyt(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()

class sieci_odp(BaseModel):
    pnr = ForeignKeyField(
        sieci_pyt, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()
    
    
class fizyka_pyt(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()

class fizyka_odp(BaseModel):
    pnr = ForeignKeyField(
        fizyka_pyt, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()
    
    
class chemia_pyt(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()

class chemia_odp(BaseModel):
    pnr = ForeignKeyField(
        chemia_pyt, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()
    
class biologia_pyt(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()

class biologia_odp(BaseModel):
    pnr = ForeignKeyField(
        biologia_pyt, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()
    
    
class bazy_pyt(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()

class bazy_odp(BaseModel):
    pnr = ForeignKeyField(
        bazy_pyt, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()
    
    
class historia_pyt(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()

class historia_odp(BaseModel):
    pnr = ForeignKeyField(
        historia_pyt, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()
    
class geografia_pyt(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()

class geografia_odp(BaseModel):
    pnr = ForeignKeyField(
        geografia_pyt, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()
    

class angielski_pyt(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()

class angielski_odp(BaseModel):
    pnr = ForeignKeyField(
        angielski_pyt, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()

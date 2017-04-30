# -*- coding: utf-8 -*-
# quiz_pw/main.py

from app import app, baza
from models import *
from views import *
import os

if __name__ == '__main__':
    app.run(debug=True)

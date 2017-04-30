# -*- coding: utf-8 -*-
# quiz_pw/views.py

from flask import render_template, request, redirect, url_for, flash

from app import app
from models import matma_odp, matma_pyt, polski_odp, polski_pyt
import math

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/matematyka', methods=['GET', 'POST'])
def matematyka():
    if request.method == 'POST':
        full = 3
        wynik = 0
        for pid, odp in request.form.items():
            odpok = matma_pyt.select(matma_pyt.odpok).where(
                matma_pyt.id == int(pid)).scalar()
            if odp == odpok:
                wynik += 1
        pr = wynik * 100 / full
        procent = str(pr) + '%'
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(procent), 'sukces')
        #return redirect(url_for('index'))

    pytania = matma_pyt().select().annotate(matma_odp)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania)
    
@app.route('/polski', methods=['GET', 'POST'])
def polski():
    if request.method == 'POST':
        wynik = 0
        for pid, odp in request.form.items():
            odpok = polski_pyt.select(polski_pyt.odpok).where(
                polski_pyt.id == int(pid)).scalar()
            if odp == odpok:
                wynik += 1
        pr = (wynik * 10) / (full / 10)
        procent = str(pr) + '%'
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(procent), 'sukces')
        return redirect(url_for('index'))

    pytania = polski_pyt().select().annotate(polski_odp)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania)


# -*- coding: utf-8 -*-
# quiz_pw/views.py

from flask import render_template, request, redirect, url_for, flash

from app import app
from models import matma_odp, matma_pyt, polski_odp, polski_pyt, sieci_odp, sieci_pyt, fizyka_odp, fizyka_pyt, chemia_odp, chemia_pyt, biologia_odp, biologia_pyt, bazy_odp, bazy_pyt, historia_pyt, historia_odp, geografia_odp, geografia_pyt, angielski_odp, angielski_pyt
import math

@app.route('/')
def index():
    return render_template('index.html')

def sprawdz(cos_pyt):
	full = cos_pyt.select().count()
	wynik = 0
	for pid, odp in request.form.items():
		odpok = matma_pyt.select(matma_pyt.odpok).where(
			matma_pyt.id == int(pid)).scalar()
		if odp == odpok:
			wynik += 1
	return full, wynik

@app.route('/matematyka', methods=['GET', 'POST'])
def matematyka():
    if request.method == 'POST':
        full, wynik = sprawdz(matma_pyt)
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

@app.route('/sieci', methods=['GET', 'POST'])
def sieci():
    if request.method == 'POST':
        full = 3
        wynik = 0
        for pid, odp in request.form.items():
            odpok = sieci_pyt.select(matma_pyt.odpok).where(
                sieci_pyt.id == int(pid)).scalar()
            if odp == odpok:
                wynik += 1
        pr = wynik * 100 / full
        procent = str(pr) + '%'
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(procent), 'sukces')
        #return redirect(url_for('index'))

    pytania = sieci_pyt().select().annotate(sieci_odp)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania)
    
@app.route('/fizyka', methods=['GET', 'POST'])
def fizyka():
    if request.method == 'POST':
        full = 3
        wynik = 0
        for pid, odp in request.form.items():
            odpok = fizyka_pyt.select(fizyka_pyt.odpok).where(
                fizyka_pyt.id == int(pid)).scalar()
            if odp == odpok:
                wynik += 1
        pr = wynik * 100 / full
        procent = str(pr) + '%'
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(procent), 'sukces')
        #return redirect(url_for('index'))

    pytania = fizyka_pyt().select().annotate(fizyka_odp)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania)
    
@app.route('/chemia', methods=['GET', 'POST'])
def chemia():
    if request.method == 'POST':
        full = 3
        wynik = 0
        for pid, odp in request.form.items():
            odpok = chemia_pyt.select(chemia_pyt.odpok).where(
                chemia_pyt.id == int(pid)).scalar()
            if odp == odpok:
                wynik += 1
        pr = wynik * 100 / full
        procent = str(pr) + '%'
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(procent), 'sukces')
        #return redirect(url_for('index'))

    pytania = chemia_pyt().select().annotate(chemia_odp)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania)
    
@app.route('/biologia', methods=['GET', 'POST'])
def biologia():
    if request.method == 'POST':
        full = 3
        wynik = 0
        for pid, odp in request.form.items():
            odpok = biologia_pyt.select(biologia_pyt.odpok).where(
                biologia_pyt.id == int(pid)).scalar()
            if odp == odpok:
                wynik += 1
        pr = wynik * 100 / full
        procent = str(pr) + '%'
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(procent), 'sukces')
        #return redirect(url_for('index'))

    pytania = biologia_pyt().select().annotate(biologia_odp)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania)
    
@app.route('/bazy', methods=['GET', 'POST'])
def bazy():
    if request.method == 'POST':
        full = 20
        wynik = 0
        for pid, odp in request.form.items():
            odpok = bazy_pyt.select(bazy_pyt.odpok).where(
                bazy_pyt.id == int(pid)).scalar()
            if odp == odpok:
                wynik += 1
        pr = wynik * 100 / full
        procent = str(pr) + '%'
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(procent), 'sukces')
        #return redirect(url_for('index'))

    pytania = bazy_pyt().select().annotate(bazy_odp)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania)
    
@app.route('/historia', methods=['GET', 'POST'])
def historia():
    if request.method == 'POST':
        full = 3
        wynik = 0
        for pid, odp in request.form.items():
            odpok = historia_pyt.select(historia_pyt.odpok).where(
                historia_pyt.id == int(pid)).scalar()
            if odp == odpok:
                wynik += 1
        pr = wynik * 100 / full
        procent = str(pr) + '%'
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(procent), 'sukces')
        #return redirect(url_for('index'))

    pytania = historia_pyt().select().annotate(historia_odp)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania)
    
@app.route('/geografia', methods=['GET', 'POST'])
def geografia():
    if request.method == 'POST':
        full = 3
        wynik = 0
        for pid, odp in request.form.items():
            odpok = geografia_pyt.select(geografia_pyt.odpok).where(
                geografia_pyt.id == int(pid)).scalar()
            if odp == odpok:
                wynik += 1
        pr = wynik * 100 / full
        procent = str(pr) + '%'
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(procent), 'sukces')
        #return redirect(url_for('index'))

    pytania = geografia_pyt().select().annotate(geografia_odp)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania)
    
@app.route('/angielski', methods=['GET', 'POST'])
def angielski():
    if request.method == 'POST':
        full = 3
        wynik = 0
        for pid, odp in request.form.items():
            odpok = angielski_pyt.select(angielski_pyt.odpok).where(
                angielski_pyt.id == int(pid)).scalar()
            if odp == odpok:
                wynik += 1
        pr = wynik * 100 / full
        procent = str(pr) + '%'
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(procent), 'sukces')
        #return redirect(url_for('index'))

    pytania = angielski_pyt().select().annotate(angielski_odp)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania)

import sqlite3
from flask import Flask, render_template, url_for
from engine import app


@app.route('/')   #@app.route('/', methods=['GET', 'POST'])
def moves():
    conn = sqlite3.connect(app.config['DATA_BASE'])
    cur = conn.cursor()

    query = "SELECT id, date, time, from_currency, form_quantity, to_currency, to_quantity FROM movimientos;" #"SELECT * FROM movimientos (id, date, time, from_currency, form_quantity, to_currency, to_quantity);"
    lectura = cur.execute(query).fetchall()
   
    conn.close()

    return render_template('index.html', moves=lectura)
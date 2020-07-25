import sqlite3
from flask import Flask, render_template, url_for
from engine import app

def connection():
    conn = sqlite3.connect(app.config['DATA_BASE'])
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')   #@app.route('/', methods=['GET', 'POST'])
def moves():
    #conn = sqlite3.connect(app.config['DATA_BASE'])
    conn = connection()
    cur = conn.cursor()
    query = "SELECT id, date, time, from_currency, form_quantity, to_currency, to_quantity FROM movimientos;" #"SELECT * FROM movimientos (id, date, time, from_currency, form_quantity, to_currency, to_quantity);"
    moves = cur.execute(query).fetchall()

    conn.close()

    return render_template('index.html', moves=moves)
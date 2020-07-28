import sqlite3
from flask import Flask, render_template, url_for, request, redirect
from engine import app
from engine.forms import MyForm

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


@app.route('/purchase', methods=['GET', 'POST'])
def compra():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('purchase.html', form=form)



'''   
    #form = FormConsulta(request.form)
    
    if request.method == 'GET':
        return render_template('purchase.html', form=form) #error_gral=False)
    else:
        if form.validate():
            conn = connection()
            cur = conn.cursor()
            query = "INSERT INTO movimientos (from_currency, to_currency, precio_unidad) values (?, ?, ?);"
            datos = (request.values.get('from_currency'), request.values.get('to_currency'), request.values.get('precio_unidad'))
            try:
                cur.execute(query, datos)
                conn.commit()
            except Exception as e:
                print("INSERT - Error en el acceso a la base de datos: {}".format(e))
                conn.close()
                return render_template('purchase.html', form=form, error_gral='Error en acceso a base de datos: {}'.format(e))
            conn.close()
            return redirect(url_for("/purchase"))
        else:
            return render_template('purchase.html', form=form, error_gral=False)

'''
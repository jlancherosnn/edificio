from flask import app,Flask, render_template, request, redirect, url_for, flash
from config import*
con_bd = EstablecerConexion()

app = Flask(__name__)
app.secret_key = 'hay_alguien_aqui_convida_S0S'

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    crearTablaUsuarios()
    app.run(debug=True)
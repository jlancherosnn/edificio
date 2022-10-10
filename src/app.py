from flask import app,Flask, render_template, request, redirect, url_for, flash
from config import*
con_bd = EstablecerConexion()

app = Flask(__name__)
app.secret_key = 'hay_alguien_aqui_convida_S0S'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logo')
def logo():
    cursor = con_bd.cursor()
    sql = "SELECT*FROM usuarios"
    cursor.execute(sql)
    UsuariosRegistradas = cursor.fetchall()
    return render_template('login.html', usuarios = UsuariosRegistradas)

@app.route('/guardar_usuarios', methods=['POST'])
def agregarUsuarios():
    cursor = con_bd.cursor()
    usuario = request.form['usuario']
    password = request.form['password']

    if  usuario and password:
        sql ="""
            INSERT INTO usuarios( usuario, password)
            VALUES ( %s, %s)
        """
        cursor.execute(sql,(usuario,password))
        con_bd.commit()
        flash("Registro Guardado Correctamente","info")
        return render_template("registro.html")
    else:
        flash("Registro no sea Guardado Correctamente","error")
        return redirect(url_for('login.html'))

def crearTablaUsuarios():
    cursor = con_bd.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS usuarios( 
                        id serial NOT NULL,
                        usuario character(50)  NOT NULL,
                        password character(120)  NOT NULL,
                        CONSTRAINT pk_usuarios_id PRIMARY KEY ("id")
                        );
                """)
    con_bd.commit()
@app.route('/validacion', methods=['GET','POST'])
def validacion():
    cursor = con_bd.cursor()
    usuario = request.form['usuario']
    password = request.form['password']
    sql = """SELECT * FROM usuarios WHERE usuario='Julian' AND password='12345'"""
    cursor.execute(sql)
    con_bd.commit()
    print(cursor.execute(sql, (usuario,password)))
    print(cursor.execute(sql))
    return render_template('index.html')
if __name__ == '__main__':
    crearTablaUsuarios()
    app.run(debug=True)
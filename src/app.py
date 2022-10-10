from flask import app,Flask, render_template, request, redirect, url_for, flash
from config import*
con_bd = EstablecerConexion()

app = Flask(__name__)
app.secret_key = 'hay_alguien_aqui_convida_S0S'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

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
        return redirect(url_for('index'))

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
    sql = """
    SELECT*FROM usuarios
    """
    cursor.execute(sql)
    personas = cursor.fetchall()
    for persona in personas:
        print(persona[1])
        print(persona[2])
        if usuario in persona[1] and password in persona[2]:
            print("USUARIO HALLADO")
            return render_template("index.html")
    return render_template("login.html")

#######################TABLAS###########################################
def crearTablaAgua():
    cursor = con_bd.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS serviceAgua( 
                        id serial NOT NULL,
                        nombre character(50)  NOT NULL,
                        cedula character(120)  NOT NULL,
                        valor character(120)  NOT NULL,
                        mes character(120)  NOT NULL,
                        vencimiento character(120)  NOT NULL,
                        torre character(120)  NOT NULL,
                        grupo character(120)  NOT NULL,
                        CONSTRAINT pk_usuarios_id PRIMARY KEY ("id")
                        );
                """)
    con_bd.commit()

def crearTablaGas():
    cursor = con_bd.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS serviceAgua( 
                        id serial NOT NULL,
                        nombre character(50)  NOT NULL,
                        cedula character(120)  NOT NULL,
                        valor character(120)  NOT NULL,
                        mes character(120)  NOT NULL,
                        vencimiento character(120)  NOT NULL,
                        torre character(120)  NOT NULL,
                        grupo character(120)  NOT NULL,
                        CONSTRAINT pk_usuarios_id PRIMARY KEY ("id")
                        );
                """)
    con_bd.commit()

def crearTablaLuz():
    cursor = con_bd.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS serviceAgua( 
                        id serial NOT NULL,
                        nombre character(50)  NOT NULL,
                        cedula character(120)  NOT NULL,
                        valor character(120)  NOT NULL,
                        mes character(120)  NOT NULL,
                        vencimiento character(120)  NOT NULL,
                        torre character(120)  NOT NULL,
                        grupo character(120)  NOT NULL,
                        CONSTRAINT pk_usuarios_id PRIMARY KEY ("id")
                        );
                """)
    con_bd.commit()



if __name__ == '__main__':
    crearTablaUsuarios()
    crearTablaAgua()
    crearTablaLuz()
    crearTablaGas()
    app.run(debug=True)
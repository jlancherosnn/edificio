from flask import app,Flask, render_template, request, redirect, url_for, flash
from config import*
con_bd = EstablecerConexion()

app = Flask(__name__)
app.secret_key = 'hay_alguien_aqui_convida_S0S'

@app.route('/')
def index():
    cursor = con_bd.cursor()
    sql = """SELECT*FROM serviceluz"""
    cursor.execute(sql)
    datos = cursor.fetchall()
    print(datos)
    return render_template('login.html')

def index1():
    cursor = con_bd.cursor()
    sql = """SELECT*FROM serviceluz"""
    cursor.execute(sql)
    datos = cursor.fetchall()
    print(datos)
    return render_template('index.html',usuarios=datos)

@app.route('/datosLuz')
def datosluz():
    cursor = con_bd.cursor()
    sql = """SELECT*FROM serviceluz"""
    cursor.execute(sql)
    datos = cursor.fetchall()
    print(datos)
    return render_template('tablaluz.html',usuarios=datos)

@app.route('/datosAgua')
def datosagua():
    cursor = con_bd.cursor()
    sql = """SELECT*FROM serviceagua"""
    cursor.execute(sql)
    datos = cursor.fetchall()
    print(datos)
    return render_template('tablaagua.html',usuarios=datos)

@app.route('/datosGaz')
def datosgaz():
    cursor = con_bd.cursor()
    sql = """SELECT*FROM servicegas"""
    cursor.execute(sql)
    datos = cursor.fetchall()
    print(datos)
    return render_template('tablagaz.html',usuarios=datos)

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


@app.route('/guardarrecibo', methods=['POST','GET'])
def guardar():
    cursor = con_bd.cursor()
    #nombre = request.form['nombre']
    #print(f"dato recuperado de {nombre}")
    dato = request.form.get('datos')
    print(f"recibo de {dato}")
    nombre = request.form['nombre']
    cedula = request.form['cedula']
    valor = request.form['valor']
    mes = request.form['mes']
    vencimiento = request.form['fecha1']
    tore = request.form.get('torre')
    piso = request.form.get('piso')
    print(f"datos nombre{nombre} - {cedula} - {valor} - {mes} - {vencimiento} - {tore} - {piso}")
    if nombre and cedula and valor and mes and vencimiento and tore and piso:
        if dato == "Agua":
            sql = """
                    INSERT INTO serviceAgua( nombre, cedula, valor, mes, vencimiento, torre, grupo)
                    VALUES ( %s, %s, %s, %s, %s, %s, %s)
                """
            cursor.execute(sql, (nombre, cedula, valor, mes, vencimiento, tore, piso))
            con_bd.commit()
            flash("Registro Guardado Correctamente", "info")
            return render_template('index.html')
        elif dato == "Energia":
            sql = """
                    INSERT INTO serviceluz( nombre, cedula, valor, mes, vencimiento, torre, grupo)
                    VALUES ( %s, %s, %s, %s, %s, %s, %s)
                """
            cursor.execute(sql, (nombre, cedula, valor, mes, vencimiento, tore, piso))
            con_bd.commit()
            flash("Registro Guardado Correctamente", "info")
            return render_template('index.html')
        elif dato == "Gas":
            sql = """
                    INSERT INTO servicegas( nombre, cedula, valor, mes, vencimiento, torre, grupo)
                    VALUES ( %s, %s, %s, %s, %s, %s, %s)
                """
            cursor.execute(sql, (nombre, cedula, valor, mes, vencimiento, tore, piso))
            con_bd.commit()
            flash("Registro Guardado Correctamente", "info")
            return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/guardar_usuarios', methods=['POST','GET'])
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

@app.route('/eliminar_persona/<int:id_persona>')
def eliminar(id_persona):
    cursor = con_bd.cursor()
    sql = "DELETE FROM serviceAgua WHERE id={0}".format(id_persona)
    cursor.execute(sql)
    sql1 = "DELETE FROM serviceluz WHERE id={0}".format(id_persona)
    cursor.execute(sql1)
    sql2 = "DELETE FROM servicegas WHERE id={0}".format(id_persona)
    cursor.execute(sql2)
    con_bd.commit()
    flash("Registro Eliminado Correctamente","error")
    return redirect(url_for('index'))

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
            sql1= """SELECT * FROM serviceluz"""
            sql2= """SELECT * FROM serviceAgua"""
            sql3="""SELECT * FROM servicegas"""
            cursor.execute(sql1)
            cursor.execute(sql2)
            cursor.execute(sql3)
            datos = cursor.fetchall()
            return render_template("index.html",usuarios=datos)
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
                        CONSTRAINT pk_Agua_id PRIMARY KEY ("id")
                        );
                """)
    con_bd.commit()

def crearTablaGas():
    cursor = con_bd.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS servicegas( 
                        id serial NOT NULL,
                        nombre character(50)  NOT NULL,
                        cedula character(120)  NOT NULL,
                        valor character(120)  NOT NULL,
                        mes character(120)  NOT NULL,
                        vencimiento character(120)  NOT NULL,
                        torre character(120)  NOT NULL,
                        grupo character(120)  NOT NULL,
                        CONSTRAINT pk_gas_id PRIMARY KEY ("id")
                        );
                """)
    con_bd.commit()

def crearTablaLuz():
    cursor = con_bd.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS serviceluz( 
                        id serial NOT NULL,
                        nombre character(50)  NOT NULL,
                        cedula character(120)  NOT NULL,
                        valor character(120)  NOT NULL,
                        mes character(120)  NOT NULL,
                        vencimiento character(120)  NOT NULL,
                        torre character(120)  NOT NULL,
                        grupo character(120)  NOT NULL,
                        CONSTRAINT pk_luz_id PRIMARY KEY ("id")
                        );
                """)
    con_bd.commit()



if __name__ == '__main__':
    crearTablaUsuarios()
    crearTablaAgua()
    crearTablaLuz()
    crearTablaGas()
    app.run(debug=True)
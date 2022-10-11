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
@app.route('/index')
def index1():
    return render_template('index.html')

@app.route('/logo')
def logo():
    cursor = con_bd.cursor()
    sql = "SELECT*FROM usuarios"
    cursor.execute(sql)
    UsuariosRegistradas = cursor.fetchall()
    return render_template('login.html', usuarios = UsuariosRegistradas)
############################## Guardar Usuarios##############################
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
##################### Validacion###############
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
            flash("Registro Guardado Correctamente","info")
            return render_template("index.html")
    flash("Registro no sea Guardado Correctamente","error")
    return render_template("login.html")

#######################TABLAS###########################################
def crearTablaAgua():
    cursor = con_bd.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS serviceagua( 
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

@app.route('/guardar_agua', methods=['POST'])
def agregaragua():
    cursor = con_bd.cursor()
    nombre = request.form['usuario']
    cedula = request.form['password']
    valor = request.form['valor']
    mes = request.form['mes']
    vencimiento = request.form['fecha1']
    torre = request.form['torre']
    grupo = request.form['grupo']
    if  nombre and cedula and valor and mes and vencimiento and torre and grupo:
        sql ="""
            INSERT INTO serviceAgua( nombre,cedula,valor,mes,vencimiento,torre,grupo)
            VALUES ( %s, %s, %s,%s, %s , %s,%s)
        """
        cursor.execute(sql,(nombre,cedula,valor,mes,vencimiento,torre,grupo))
        con_bd.commit()
        flash("Registro Guardado Correctamente","info")
        return render_template("index.html")
    else:
        flash("Registro no sea Guardado Correctamente","error")
        return redirect(url_for('index'))
##################################### tabla gas########################
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

@app.route('/guardar_gas', methods=['POST'])
def agregaragua():
    cursor = con_bd.cursor()
    nombre = request.form['usuario']
    cedula = request.form['password']
    valor = request.form['valor']
    mes = request.form['mes']
    vencimiento = request.form['fecha1']
    torre = request.form['torre']
    grupo = request.form['grupo']
    if  nombre and cedula and valor and mes and vencimiento and torre and grupo:
        sql ="""
            INSERT INTO servicegas( nombre,cedula,valor,mes,vencimiento,torre,grupo)
            VALUES ( %s, %s, %s,%s, %s , %s,%s)
        """
        cursor.execute(sql,(nombre,cedula,valor,mes,vencimiento,torre,grupo))
        con_bd.commit()
        flash("Registro Guardado Correctamente","info")
        return render_template("index.html")
    else:
        flash("Registro no sea Guardado Correctamente","error")
        return redirect(url_for('index'))

############################# tabla luz #########################
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

@app.route('/guardar_luz', methods=['POST'])
def agregaragua():
    cursor = con_bd.cursor()
    nombre = request.form['usuario']
    cedula = request.form['password']
    valor = request.form['valor']
    mes = request.form['mes']
    vencimiento = request.form['fecha1']
    torre = request.form['torre']
    grupo = request.form['grupo']
    if  nombre and cedula and valor and mes and vencimiento and torre and grupo:
        sql ="""
            INSERT INTO serviceluz( nombre,cedula,valor,mes,vencimiento,torre,grupo)
            VALUES ( %s, %s, %s,%s, %s , %s,%s)
        """
        cursor.execute(sql,(nombre,cedula,valor,mes,vencimiento,torre,grupo))
        con_bd.commit()
        flash("Registro Guardado Correctamente","info")
        return render_template("index.html")
    else:
        flash("Registro no sea Guardado Correctamente","error")
        return redirect(url_for('index'))



if __name__ == '__main__':
    crearTablaUsuarios()
    crearTablaAgua()
    crearTablaLuz()
    crearTablaGas()
    app.run(debug=True)
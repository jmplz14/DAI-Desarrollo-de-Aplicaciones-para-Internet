from flask import Flask,  render_template, url_for, send_file, request, session
from PIL import Image
from random import randrange
from pickleshare import *


app = Flask(__name__)
app.secret_key = 'esto-es-una-clave-muy-secreta'

historial = []
db = PickleShareDB('usuarios/datosUsuarios')

def anadirHistorial(pagina):
    if(len(historial) < 3):
        historial.append(pagina)
    else:
        historial.pop(0)
        historial.append(pagina)

def hayUser():
    return  'usuario' in session
def existeUsuario(usuario):
    return  db.keys(usuario)
    
@app.route('/login',methods=['POST'])
def login():
    nombre = request.form['usuario']
    contraseña = request.form['contraseña']
    if existeUsuario(nombre):
        if contraseña == db[nombre]['contraseña']:
            session['usuario'] = nombre
            #session['contraseña'] = contraseña
    return index()


@app.route('/logout',methods=['POST'])
def logout():
    session.clear()
    del historial[:]
    return render_template("index.html")




@app.route("/productos")
def inicio():
    if hayUser():
        anadirHistorial("productos")
        return render_template("productos.html",usuario = session['usuario'],arrayHistorial=historial)
        
    else:
        return render_template("productos.html")

@app.route("/registro",methods=['POST'])
def registro():   
    return render_template("registro.html")
    
@app.route("/registrado",methods=['POST'])
def registrar(): 
    nombre = request.form['nombre']
    contraseña = request.form['contraseña']
    nombreCompleto = request.form['nombreCompleto']
    if nombre != "" and contraseña != "" and nombreCompleto != "":
        if not existeUsuario(nombre):
            session['usuario'] = nombre
            #session['contraseña'] = contraseña
            db[nombre] = {'contraseña': contraseña, 'nombreCompleto': nombreCompleto} 
            return index()
    return render_template("registro.html", cambiado = False)

@app.route("/cambioDatos")
def cambioDatos():   
    if hayUser():
        anadirHistorial("Datos usuario")
        nombre = db[session["usuario"]]['nombreCompleto']
        return render_template("cambioDatos.html",usuario = session['usuario'],arrayHistorial=historial,session = session, nombreCompleto = nombre)
    else:
        return render_template("cambioDatos.html")



@app.route("/cambiados",methods=['POST'])
def cambiados():
    nombre = request.form['nombre']
    contraseña = request.form['contraseña']
    nombreCompleto = request.form['nombreCompleto']
    cambiado = False
    if nombre != session['usuario']:
        if not existeUsuario(nombre):
            db[nombre] = {'contraseña': db[session['usuario']]['contraseña'], 'nombreCompleto': db[session['usuario']]['nombreCompleto']}
            db.pop(session['usuario'])
            session['usuario'] = nombre
            cambiado = True
        if cambiado:
            if contraseña != "":
                db[nombre] = {'contraseña': contraseña, 'nombreCompleto': nombreCompleto} 
        
            if nombreCompleto != db[nombre]['nombreCompleto']:
                db[nombre] = {'contraseña': db[nombre]['contraseña'], 'nombreCompleto': nombreCompleto} 
    else:
        if contraseña != "":
            db[nombre] = {'contraseña': contraseña, 'nombreCompleto': nombreCompleto}
            cambiado = True
        
        if nombreCompleto != db[nombre]['nombreCompleto']:
            db[nombre] = {'contraseña': db[nombre]['contraseña'], 'nombreCompleto': nombreCompleto} 
            cambiado = True

            
    
    if cambiado: 
        return render_template("cambioDatos.html",usuario = session['usuario'],arrayHistorial=historial,session = session, nombreCompleto = nombreCompleto, cambiado = True)
    else:
        return render_template("cambioDatos.html",usuario = session['usuario'],arrayHistorial=historial,session = session, nombreCompleto = nombreCompleto, cambiado = False)
    


@app.route("/inicio")
def productos():
    if hayUser():
        anadirHistorial("inicio")
        return render_template("inicio.html",usuario = session['usuario'],arrayHistorial=historial)
    else:
        return render_template("inicio.html")

@app.route("/")
def index():

    if hayUser():
	    return render_template("index.html",usuario = session['usuario'],arrayHistorial=historial)
    else:
        return render_template("index.html")

@app.errorhandler(404) 
# inbuilt function which takes error as parameter 
def not_found(e): 
# defining function 
  return '''Error 404'''


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
    
@app.route('/login',methods=['POST'])
def login():
    nombre = request.form['usuario']
    contraseña = request.form['contraseña']
    session['usuario'] = nombre
    session['contraseña'] = contraseña
    return index()

@app.route('/logout',methods=['POST'])
def logout():
    session.clear()
    historial = []
    return render_template("index.html")



@app.route('/datos-sesion',methods=['GET'])
def datos_sesion():
    if 'nombre' in session:
        nombre = session['nombre']
    else:
        nombre = ''
     
    if 'apellido' in session:
        apellido = session['apellido']
    else:
        apellido = ''
     
    return 'Datos Sesion: ' + nombre + ' ' + apellido

@app.route("/productos")
def inicio():
    if hayUser():
        anadirHistorial("productos")
        return render_template("productos.html",usuario = session['usuario'],arrayHistorial=historial)
    else:
        return render_template("productos.html")

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


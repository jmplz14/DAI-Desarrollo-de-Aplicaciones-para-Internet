from flask import Flask,  render_template, url_for, send_file, request
from PIL import Image
from random import randrange


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''<html>
                <head>
                    <meta charset="uft-8"/>
                    <title>Hola Mundo en HTML</title>
                    <link rel="stylesheet" href="static/templates/holamundo.css">
                </head>
                <body>
                    <h1>Hola Mundo</h1>
                    <p>Mi primera página en HTML.</p>
                    <img src="static/imagenes/img1.png" border="1" alt="Esto es un fractal">
                </body>
            </html>'''


@app.route('/user/pepe')
def pepe():
    return '''Hola pepe'''

@app.route('/user/zerjillo')
def zerjillo():
    return '''Hola zerjillo'''

@app.route('/user/<name>')
def generico(name):
    return '''Hola {}'''.format(name)


@app.errorhandler(404) 
# inbuilt function which takes error as parameter 
def not_found(e): 
# defining function 
  return '''Error 404'''

@app.route('/fractal')
def fractal():
    xa = float(request.args.get('x1'))
    xb = float(request.args.get('x2'))
    ya = float(request.args.get('y1'))
    yb = float(request.args.get('y2'))
    size = int(request.args.get('size'))
    iter = int(request.args.get('iter'))
    # max iterations allowed 
    maxIt = iter 
    
    # image size 
    imgx = size
    imgy = size
    image = Image.new("RGB", (imgx, imgy)) 
    
    for y in range(imgy): 
        zy = y * (yb - ya) / (imgy - 1)  + ya 
        for x in range(imgx): 
            zx = x * (xb - xa) / (imgx - 1)  + xa 
            z = zx + zy * 1j
            c = z 
            for i in range(maxIt): 
                if abs(z) > 2.0: break
                z = z * z + c 
            image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16)) 
    image.save('static/imagenes/mandelbrot.png')
    return '''<img src="static/imagenes/mandelbrot.png" border="1" alt="Esto es un fractal">'''


"""@app.route('/svg') 
def svg():
    numFiguras = randrange(3) + 1
    imagen = '''"<SVG width="300" height="300">"'''
    for i in range(numFiguras):
        tipo_figura = randrange(3)
        if tipo_figura == 0:
        else if tipo_figura == 1:
        else if tipo_figura == 2:
        

    return '''<h1>The language value is: {}</h1>'''.format(numFiguras)"""
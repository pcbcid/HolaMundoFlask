from flask import Flask, request, session, render_template, url_for, redirect, abort, jsonify

app = Flask(__name__)


app.secret_key='Mi_llave_secreta'

#http://localhost:5000/
@app.route('/')
def inicio():
    if 'username' in session:
        #return 'El usuario ya ha hecho login'
        return f'El usuario que ha hecho login es: {session["username"]}'
    return 'No ha hecho login'
#    app.logger.debug('Mensaje a nivel debug')
#    app.logger.info(f'Entramos al path {request.path} ' )
#    app.logger.warn('Mensaje a nivel warning' )
#    app.logger.error('Mensaje a nivel error' )
#    return 'Hola Mundo desde Flask'


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #Omitimos validacion de ususario y password
        usuario = request.form['username']
        #agregamos el usuario a la session
        session['username']= usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre.upper()}'

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es {edad}'

@app.route('/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html',nombre_llave=nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('inicio'))

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error_404.html',error=error),404

#REST Representational state transfer
@app.route('/api/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_json(nombre):
    valores={'nombre': nombre,'metodo_http': request.method}
    return jsonify(valores)


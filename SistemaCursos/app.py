from flask import Flask
#Hacemos uso de flask
from flask import render_template,request, redirect #envio de informacion recepcionar datos
#Renderizamos los templates
from flaskext.mysql import MySQL
#Nos conectamos a una base de datos MySQL
from datetime import datetime

app= Flask(__name__) #Creamos nuestra aplicacion

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
#Creando referencia hacia el host de MYSQL, los nombres deben estar bien escritos
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='colegio'
#Pasamos las instrucciones para esta BD
mysql.init_app(app) #Creamos conexion con los datos
#Vamos a utilizar parte del modulo de mysql en flaskest

@app.route('/') #Recibe solicitudes mediante URL
#Cuando el usuario escriba en el host / se va a leer index.html
def index():
    return render_template('index.html')

#REFERENCIA 1 PARA COMUNICAR CON EL INDEX HTML TABLA PROFESORES
@app.route('/listarProfesores') #Recibe solicitudes mediante URL
#Cuando el usuario escriba en el host / se va a leer index.html
def listarProfesores():

    sql ="SELECT * FROM `profesores`;" #Seleccionando toda la informacion de una tabla 
    conn= mysql.connect()
    #Hace referencia a la conexion
    cursor=conn.cursor()#Un lugar donde vamos a almacenar todo lo que guardaremos
    cursor.execute(sql) #Ejecuta el codigo SQL
    
    profesores=cursor.fetchall() #Selecciona todos los registros
    print(profesores) #Muestra todos los registros

    conn.commit() #Cierra y guarda los cambios
    return render_template('profesores/index.html', profesores=profesores) #identifica la carpeta profesores y entra al index
                                                    #aca enviamos una variable con el valor de empleados y que sea igual a ella

#Creando ruta para ELIMINACION en la BD
@app.route('/destroy/<int:id_profesor>') #Se elimina por el id
def destroy(id_profesor): 
    conn= mysql.connect()
    cursor=conn.cursor()
    #Estamos indicando que se conecta a la base de datos y que se elimine ese registro
    cursor.execute("DELETE FROM profesores WHERE id_profesor=%s", (id_profesor))
    conn.commit()

    #Redireccionar a la URL original utilizando el redirect del principio (linea 3)
    return redirect('/')


#Creando ruta para EDITAR en la BD
@app.route('/edit/<int:id_profesor>')
def edit(id_profesor):
    conn= mysql.connect()
    cursor=conn.cursor()#Un lugar donde vamos a almacenar todo lo que guardaremos
    cursor.execute("SELECT * FROM profesores WHERE id_profesor=%s", (id_profesor)) #Ejecuta el codigo SQL
    
    profesores=cursor.fetchall() #Selecciona todos los registros
    print(profesores) #Muestra todos los registros
    conn.commit() #Cierra y guarda los cambios
    print(profesores)

    return render_template('profesores/editar.html', profesores=profesores)



#Ruta creada para ACTUALIZAR datos
@app.route('/update', methods=['POST'])
def update():
    _id=request.form['id_profesor']
    _nombrep=request.form['nombre_p']
    _edadp=request.form['edad_p']
    _materiap=request.form['materia']
    _anosexperienciap=request.form['años_experiencia']
    #Me permite generar una instruccion SQL cuando encuentre un ID como el que esten enviando
    #id=request.form["txtId"]

    #app.logger.debug(_id)
    #app.logger.debug("hola33") PARA IMPRIMIR Y LEER VALORES

    sql ="UPDATE profesores SET nombre_p=%s, edad_p=%s, materia=%s, años_experiencia=%s WHERE id_profesor=%s;" #
    
    #Igualamos los datos para que los reciba del formulario
    datos=(_nombrep, _edadp, _materiap, int(_anosexperienciap), int(_id)) # , id  El ultimo id hace referencia al de la linea 76

    conn= mysql.connect()
    cursor=conn.cursor()#Un lugar donde vamos a almacenar todo lo que guardaremos
    cursor.execute(sql, datos) #Ejecuta el codigo SQL
    conn.commit() #Cierra y guarda los cambios

    return redirect('/')



#REFERENCIA 2 PARA CREAR
@app.route('/crear')
def crear():
    return render_template('profesores/crear.html')


#REFERENCIA 3 del metodo post en CREAR
@app.route('/store', methods=['POST'])
def storage():
    _id=request.form['id_profesor']
    _nombrep=request.form['nombre_p']
    _edadp=request.form['edad_p']
    _materiap=request.form['materia']
    _anosexperienciap=request.form['años_experiencia']

    #instrucciones que permiten conectar, insertar y redireccionar
    sql ="INSERT INTO `profesores` (`id_profesor`, `nombre_p`, `edad_p`, `materia`, `años_experiencia`) VALUES (%s, %s, %s, %s, %s);" #%S significa que los valores se acomodaran en el orden de lso datos
    
    #Igualamos los datos para que los reciba del formulario
    datos=(_id, _nombrep, _edadp, _materiap, _anosexperienciap)
    
    conn= mysql.connect()
    #Hace referencia a la conexion
    cursor=conn.cursor()#Un lugar donde vamos a almacenar todo lo que guardaremos
    cursor.execute(sql, datos) #Ejecuta el codigo SQL
    conn.commit() #Cierra y guarda los cambios
    return render_template('profesores/index.html')

@app.route('/listarestudiantes') #Recibe solicitudes mediante URL
#Cuando el usuario escriba en el host / se va a leer index.html
def listarestudiantes():
    sql ="SELECT * FROM `estudiantes`;" #Seleccionando toda la informacion de una tabla 
    conn= mysql.connect()
    #Hace referencia a la conexion
    cursor=conn.cursor()#Un lugar donde vamos a almacenar todo lo que guardaremos
    cursor.execute(sql) #Ejecuta el codigo SQL
    
    estudiantes=cursor.fetchall() #Selecciona todos los registros
    print(estudiantes) #Muestra todos los registros

    conn.commit() #Cierra y guarda los cambios
    return render_template('estudiantes/index.html', estudiantes=estudiantes) #identifica la carpeta profesores y entra al index
                                                    #aca enviamos una variable con el valor de empleados y que sea igual a ella

#Creando ruta para ELIMINACION en la BD
@app.route('/destroyEstudiante/<int:id_estudiante>') #Se elimina por el id
def destroyEstudiante(id_estudiante): 

    app.logger.debug("A message")
    app.logger.debug(id_estudiante)
    app.logger.debug("A message")
    conn= mysql.connect()
    cursor=conn.cursor()
    #Estamos indicando que se conecta a la base de datos y que se elimine ese registro
    cursor.execute("DELETE FROM estudiantes WHERE id_estudiante =%s", (id_estudiante))
    conn.commit()

    #Redireccionar a la URL original utilizando el redirect del principio (linea 3)
    return redirect('/')



#Creando ruta para EDITAR en la BD
@app.route('/editEstudiante/<int:id_estudiante>')
def editEstudiante(id_estudiante):
    conn= mysql.connect()
    cursor=conn.cursor()#Un lugar donde vamos a almacenar todo lo que guardaremos
    cursor.execute("SELECT * FROM estudiantes WHERE id_estudiante=%s", (id_estudiante)) #Ejecuta el codigo SQL
    
    estudiantes=cursor.fetchall() #Selecciona todos los registros
    print(estudiantes) #Muestra todos los registros
    conn.commit() #Cierra y guarda los cambios
    print(estudiantes)

    return render_template('estudiantes/editar.html', estudiantes=estudiantes)



#Ruta creada para ACTUALIZAR datos
@app.route('/updateEstudiante', methods=['POST'])
def updateEstudiante():
    _id_estudiante=request.form['id_estudiante']
    _nombre_e=request.form['nombre_e']
    _edad_e=request.form['Edadestudiante']
    _grado=request.form['Grado']
    _promedio=request.form['Promedio']
    #Me permite generar una instruccion SQL cuando encuentre un ID como el que esten enviando
    #id=request.form["txtId"]

    #app.logger.debug(_id)
    #app.logger.debug("hola33") PARA IMPRIMIR Y LEER VALORES

    sql ="UPDATE estudiantes SET nombre_e=%s, edad_e=%s, grado=%s, promedio=%s WHERE id_estudiante=%s;" #
    
    #Igualamos los datos para que los reciba del formulario
    datos=(_nombre_e, _edad_e, _grado, float(_promedio), int(_id_estudiante)) # , id  El ultimo id hace referencia al de la linea 76

    conn= mysql.connect()
    cursor=conn.cursor()#Un lugar donde vamos a almacenar todo lo que guardaremos
    cursor.execute(sql, datos) #Ejecuta el codigo SQL
    conn.commit() #Cierra y guarda los cambios

    return redirect('/')



#REFERENCIA 2 PARA CREAR
@app.route('/crearEstudiante')
def crearEstudiante():
    return render_template('estudiantes/crear.html')


#REFERENCIA 3 del metodo post en CREAR
@app.route('/storeEstudiante', methods=['POST'])
def storeEstudiante():
    _id_estudiante=request.form['id_estudiante']
    _nombre_e=request.form['nombre_e']
    _edad_e=request.form['Edadestudiante']
    _grado=request.form['Grado']
    _promedio=request.form['Promedio']

    #instrucciones que permiten conectar, insertar y redireccionar
    sql ="INSERT INTO `estudiantes` (`id_estudiante`, `nombre_e`, `edad_e`, `grado`, `promedio`) VALUES (%s, %s, %s, %s, %s);" #%S significa que los valores se acomodaran en el orden de lso datos
    
    #Igualamos los datos para que los reciba del formulario
    datos=(_id_estudiante, _nombre_e, _edad_e, _grado, _promedio)
    
    conn= mysql.connect()
    #Hace referencia a la conexion
    cursor=conn.cursor()#Un lugar donde vamos a almacenar todo lo que guardaremos
    cursor.execute(sql, datos) #Ejecuta el codigo SQL
    conn.commit() #Cierra y guarda los cambios
    return render_template('./index.html')

@app.route('/listarcursos') #Recibe solicitudes mediante URL
#Cuando el usuario escriba en el host / se va a leer index.html
def listarcursos():
    sql ="SELECT * FROM `cursos`;" #Seleccionando toda la informacion de una tabla 
    conn= mysql.connect()
    #Hace referencia a la conexion
    cursor=conn.cursor()#Un lugar donde vamos a almacenar todo lo que guardaremos
    cursor.execute(sql) #Ejecuta el codigo SQL
    
    cursos=cursor.fetchall() #Selecciona todos los registros
    print(cursos) #Muestra todos los registros

    conn.commit() #Cierra y guarda los cambios
    return render_template('cursos/index.html', cursos=cursos) #identifica la carpeta profesores y entra al index
                                                    #aca enviamos una variable con el valor de empleados y que sea igual a ella

#Creando ruta para ELIMINACION en la BD
@app.route('/destroycursos/<int:id_curso>') #Se elimina por el id
def destroycurso(id_curso): 
    conn= mysql.connect()
    cursor=conn.cursor()
    #Estamos indicando que se conecta a la base de datos y que se elimine ese registro
    cursor.execute("DELETE FROM cursos WHERE id_curso=%s", (id_curso))
    conn.commit()

    #Redireccionar a la URL original utilizando el redirect del principio (linea 3)
    return redirect('/')



#Creando ruta para EDITAR en la BD
@app.route('/editcursos/<int:id_curso>')
def editcurso(id_curso):
    conn= mysql.connect()
    cursor=conn.cursor()#Un lugar donde vamos a almacenar todo lo que guardaremos
    cursor.execute("SELECT * FROM cursos WHERE id_curso=%s", (id_curso)) #Ejecuta el codigo SQL
    
    cursos=cursor.fetchall() #Selecciona todos los registros
    print(cursos) #Muestra todos los registros
    conn.commit() #Cierra y guarda los cambios
    print(cursos)

    return render_template('cursos/editar.html', cursos=cursos)



#Ruta creada para ACTUALIZAR datos
@app.route('/updatecursos', methods=['POST'])
def updatecursos():
    _id_curso=request.form['id_curso']
    _nombre_curso=request.form['nombre_curso']
    _nivel=request.form['Nivel']
    _capacidad=request.form['Capacidad']
    _horario=request.form['Horario']
    
    #Me permite generar una instruccion SQL cuando encuentre un ID como el que esten enviando
    #id=request.form["txtId"]

    #app.logger.debug(_id)
    #app.logger.debug("hola33") PARA IMPRIMIR Y LEER VALORES

    sql ="UPDATE cursos SET nombre_curso=%s, Nivel=%s, Capacidad=%s, Horario=%s WHERE id_curso=%s;" #
    
    #Igualamos los datos para que los reciba del formulario
    datos=(_nombre_curso, _nivel, int(_capacidad), _horario, int(_id_curso)) # , id  El ultimo id hace referencia al de la linea 76

    conn= mysql.connect()
    cursor=conn.cursor()#Un lugar donde vamos a almacenar todo lo que guardaremos
    cursor.execute(sql, datos) #Ejecuta el codigo SQL
    conn.commit() #Cierra y guarda los cambios

    return redirect('/')



#REFERENCIA 2 PARA CREAR
@app.route('/crearcurso')
def crearcurso():
    return render_template('cursos/crear.html')


#REFERENCIA 3 del metodo post en CREAR
@app.route('/storecurso', methods=['POST'])
def storecurso():
    _id_curso=request.form['id_curso']
    _nombre_curso=request.form['nombre_curso']
    _nivel=request.form['Nivel']
    _capacidad=request.form['Capacidad']
    _horario=request.form['Horario']
    

    #instrucciones que permiten conectar, insertar y redireccionar
    sql ="INSERT INTO `cursos` (`id_curso`, `nombre_curso`, `Nivel`, `Capacidad`, `Horario`) VALUES (%s, %s, %s, %s, %s);" #%S significa que los valores se acomodaran en el orden de lso datos
    
    #Igualamos los datos para que los reciba del formulario
    datos=(_id_curso, _nombre_curso, _nivel, _capacidad, _horario)
    
    conn= mysql.connect()
    #Hace referencia a la conexion
    cursor=conn.cursor()#Un lugar donde vamos a almacenar todo lo que guardaremos
    cursor.execute(sql, datos) #Ejecuta el codigo SQL
    conn.commit() #Cierra y guarda los cambios
    return render_template('./index.html')

if __name__== '__main__':
    app.run(debug=True)

    
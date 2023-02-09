from flask import Flask, render_template, request, url_for, redirect, send_file
import glob
app = Flask(__name__)


@app.before_request
def before_request():
   print("Antes de la petivión...")

@app.after_request
def after_request(response):
   print("Despues de la pertición.")
   return response
   

@app.route('/')
def index():
   # return "UskoKruM2010  susbribir"
   libros = [
      {
      'path':'historia',      
      'nombre':'Historia',
        'url':'./static/img/historia.jpg',
      'descripcion': 'La historia es la ciencia social encargada de estudiar los eventos del pasado de la humanidad a través de distintas metodologías que analizan el contexto social, político, económico, geográfico y psicológico del hombre a través de su entorno.'

      }, 
      {
      'path':'arte',      
      'nombre':'Arte',
      'url':'./static/img/arte.jpg',
      'descripcion': ' Es la manifestación o expresión libre de cualquier actividad creativa y estética por parte de los seres humanos, donde se plasman sus emociones, sentimientos y percepciones sobre su entorno, sus vivencias o loque imagina sobre la realidad.'
      },
      {
      'path':'lenguaje',      
      'nombre':'Lenguaje',
       'url':'./static/img/lengua.jpg',
      'descripcion': 'El lenguaje es la capacidad que tiene el ser humano para expresarse y comunicarse, a través de diversos sistemas de signos: orales, escritos o gestuales para llegar al entendimiento común.'
      },
      {
      'path':'ciencia',      
      'nombre':'Ciencia',
      'url':'./static/img/ciencia.jpg',
      'descripcion': ' Conjunto de conocimientos obtenidos mediante la observación y el razonamiento , sistemáticamente estructurados y de los que se deducen principios y leyes generales con capacidad predictiva y comprobables experimentalmente .'
      },
        {
      'path':'psicologia',      
      'nombre':'Psicología',
        'url':'./static/img/psicologia.jpg',
      'descripcion': 'Es la ciencia que estudia de forma teórica y práctica los aspectos, sociales, culturales y biológicos que influyen en el comportamiento humano, tanto a nivel individual como social, y el funcionamiento y desarrollo de la mente humana.'
      },
      {
      'path':'politica',      
      'nombre':'Política',
             'url':'./static/img/politica.jpg',
      'descripcion': 'Es una actividad orientada en forma ideológica a la toma de decisiones de un grupo para alcanzar ciertos objetivos. También puede definirse como una manera de ejercer el poder con la intención de resolver o minimizar el choque entre los intereses de la sociedad. '
      },
      {
      'path':'religion',      
      'nombre':'Religión',
      'url':'./static/img/religion.jpg',
      'descripcion': ' Es un sistema de creencias, costumbres y símbolos establecidos en torno a una idea de la divinidad o de lo sagrado. '
      }, 
       {
      'path':'sociales',      
      'nombre':'Sociales',
        'url':'./static/img/sociales.jpg',
      'descripcion': 'Son un conjunto de disciplinas que estudian fenómenos relacionados con la realidad del ser humano.'
      }]
   data = {
        'titulo':'Index',
        'bienvenidos': 'Saludos!',
        'libros': libros,
        'numero_libros': len(libros)
   }
   return render_template('index.html', data=data)

@app.route('/download')
def download(path):
   return send_file(path, as_attachment=True);

@app.route('/detalle/<string:tipo>')
def detalle(tipo):
   libros = {
      'historia':{
      'nombre':'Historia',
      'url':'./static/img/historia.jpg',
      'pdf': './static/pdf/historia.pdf',
      'descripcion': 'La historia es la ciencia social encargada de estudiar los eventos del pasado de la humanidad a través de distintas metodologías que analizan el contexto social, político, económico, geográfico y psicológico del hombre a través de su entorno.',
      'creacion': '05/010/98',
      'lista': [
         'silvon',
         'simon',
      ]
      }, 
      'arte':{
      'nombre':'Arte',
      'url':'./static/img/arte.jpg',
      'descripcion': ' Es la manifestación o expresión libre de cualquier actividad creativa y estética por parte de los seres humanos, donde se plasman sus emociones, sentimientos y percepciones sobre su entorno, sus vivencias o loque imagina sobre la realidad.'
      },
      'lenguaje':{
      'nombre':'Lenguaje',
       'url':'./static/img/lengua.jpg',
      'descripcion': 'El lenguaje es la capacidad que tiene el ser humano para expresarse y comunicarse, a través de diversos sistemas de signos: orales, escritos o gestuales para llegar al entendimiento común.'
      },
      'ciencia':{
      'nombre':'Ciencia',
      'url':'./static/img/ciencia.jpg',
      'descripcion': ' Conjunto de conocimientos obtenidos mediante la observación y el razonamiento , sistemáticamente estructurados y de los que se deducen principios y leyes generales con capacidad predictiva y comprobables experimentalmente .'
      },
      'psicologia':{
      'nombre':'Psicología',
        'url':'./static/img/psicologia.jpg',
      'descripcion': 'Es la ciencia que estudia de forma teórica y práctica los aspectos, sociales, culturales y biológicos que influyen en el comportamiento humano, tanto a nivel individual como social, y el funcionamiento y desarrollo de la mente humana.'
      },
      'politica':{
      'nombre':'Política',
             'url':'./static/img/politica.jpg',
      'descripcion': 'Es una actividad orientada en forma ideológica a la toma de decisiones de un grupo para alcanzar ciertos objetivos. También puede definirse como una manera de ejercer el poder con la intención de resolver o minimizar el choque entre los intereses de la sociedad. '
      },
      'religion':{
      'nombre':'Religión',
      'url':'./static/img/religion.jpg',
      'descripcion': ' Es un sistema de creencias, costumbres y símbolos establecidos en torno a una idea de la divinidad o de lo sagrado. '
      }, 
      'sociales': {
      'nombre':'Sociales',
        'url':'./static/img/sociales.jpg',
      'descripcion': 'Son un conjunto de disciplinas que estudian fenómenos relacionados con la realidad del ser humano.'
      }}
   return render_template('detail.html', tipo=tipo.lower(), libros=libros);


@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre,edad):
   data={
      'titulo':'Contacto',
      'nombre': nombre,
      'edad': edad
   }
   return render_template('contacto.html', data=data)


def query_string():
   print(request)
   print(request.args)
   print(request.args.get('param1'))
   return "Okay"

def pagina_no_encontrada(error):
   #return render_template('404.html'), 404
   return redirect(url_for('index'))

if __name__ == '__main__':
   app.add_url_rule('/query_string',view_func=query_string)
   app.register_error_handler(404, pagina_no_encontrada)
   app.run(debug=True, port=5000)

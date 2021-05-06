from jinja2 import FileSystemLoader, Environment
from wsgiref.simple_server import make_server


def app(environ, start_response):
    #load folder
  env = Environment(loader=FileSystemLoader("templates"))

  template = env.get_template('index.html')
  
  #generate data
  data = {
      'title' : 'WSGI template render with jinja',
      'username' : 'Takatae, dudmit'
  }

  html = template.render(data)
  headers = [('Content-type','text/html; charset=utf-8')]

  # Response code
  start_response('200 OK', headers)

  return [bytes(html,'utf-8')]

with make_server('localhost',8000, app) as httpd:
    print('Iniciando....')
    httpd.serve_forever() 
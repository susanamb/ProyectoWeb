from wsgiref.simple_server import make_server

def app(environ, start_response):
  header = [('Content-type','text/plain; charset=utf-8')]

  # Response code
  start_response('200 OK', header)

  return ['Mi primer servidor web en python! ;3'.encode('utf-8')]

server = make_server('localhost',8000, app)
server.serve_forever() 
from wsgiref.simple_server import make_server

HTML = ''' 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Susanasweb</title>
</head>
<body>
    <h1>Buenasnoshis</h1>
</body>
</html>
'''



def app(environ, start_response):
  header = [('Content-type','text/html; charset=utf-8')]

  # Response code
  start_response('200 OK', header)

  return [bytes(HTML,'utf-8')]

server = make_server('localhost',8000, app)
print('Iniciando....')
server.serve_forever() 
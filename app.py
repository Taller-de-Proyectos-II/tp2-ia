from sys import argv
import bottle
from bottle import route, run, request
from perceptron import MultiLayer
import numpy as np

bottle.debug(True)

def enable_cors(fn):
  def _enable_cors(*args, **kwargs):
      response.headers['Access-Control-Allow-Origin'] = '*'
      response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
      response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

      if request.method != 'OPTIONS':
          return fn(*args, **kwargs)

  return _enable_cors

@enable_cors
@route('/manifestations', method='POST')
def index():
    body = request.json
    manifestations = body.get('manifestations')
    entrada = np.array([manifestations])
    n = MultiLayer(entrada)
    response = n.response(entrada)
    if response > 0.5:
	    return 'Necesita asignación de prueba'
    else:
        return 'No necesita asignación de prueba'

if __name__ == '__main__':
	run(host='0.0.0.0',port = argv[1])
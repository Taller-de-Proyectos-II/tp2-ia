from sys import argv
import bottle
from bottle import route, run, request
import numpy as np
import tensorflow.keras as k

bottle.debug(True)

# Recrea exactamente el mismo modelo solo desde el archivo
model = k.models.load_model('path_to_my_model.h5')
model_alert = k.models.load_model('path_to_my_model_alert.h5')

def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
        if request.method != 'OPTIONS':
            return fn(*args, **kwargs)
    return _enable_cors

@enable_cors
@route('/', method='GET')
def index():
    return 'Proyecto app-tp2-ia Operativo'

@enable_cors
@route('/manifestations', method='POST')
def getResultManifestation():
    body = request.json
    manifestations = body.get('manifestations')
    entrada = np.array([manifestations])
    response = int(model.predict(entrada).round())
    print(response)
    if response == 1:
        return 'Necesita asignación de prueba'
    else:
        return 'No necesita asignación de prueba'

@enable_cors
@route('/manifestations/training', method='POST')
def trainingManifestation():
    try:
        training_data_aux = []
        target_data_aux = []
        training_data = np.array([], "float32")
        target_data = np.array([], "float32")

        body = request.json
        inputs = body.get('inputs')
        outputs = body.get('outputs')

        for input in inputs:
            training_data_aux.append([int(x) for x in input])
        for output in outputs:
            target_data_aux.append([int(x) for x in output])

        training_data = np.array(training_data_aux, "float32")
        target_data = np.array(target_data_aux, "float32")
        
        scores = model.evaluate(training_data, target_data)
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
        model.save('path_to_my_model.h5')
        return 'Entrenamiento exitoso'
    except:
        return 'Entrenamiento fallido'

@enable_cors
@route('/alerts', method='POST')
def getResultAlert():
    body = request.json
    alerts = body.get('alerts')
    entrada = np.array([alerts])
    response = int(model_alert.predict(entrada).round())
    print(response)
    if response == 0:
        return 'No'
    else:
        return 'Sí'

@enable_cors
@route('/alerts/training', method='POST')
def trainingAlert():
    try:
        training_data_aux = []
        target_data_aux = []
        training_data = np.array([], "float32")
        target_data = np.array([], "float32")

        body = request.json
        inputs = body.get('inputs')
        outputs = body.get('outputs')

        for input in inputs:
            training_data_aux.append([int(x) for x in input])
        for output in outputs:
            target_data_aux.append([int(x) for x in output])

        training_data = np.array(training_data_aux, "float32")
        target_data = np.array(target_data_aux, "float32")
        
        scores = model_alert.evaluate(training_data, target_data)
        print("\n%s: %.2f%%" % (model_alert.metrics_names[1], scores[1]*100))
        model_alert.save('path_to_my_model_alert.h5')
        return 'Entrenamiento exitoso'
    except:
        return 'Entrenamiento fallido'

if __name__ == '__main__':
    run(host='0.0.0.0', port=argv[1])

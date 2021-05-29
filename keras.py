from numpy.lib.function_base import append
import tensorflow as tf
import numpy as np
import csv

Sequential = tf.keras.models.Sequential
Dense = tf.keras.layers.Dense

# Carga de data de entrenamiento (entradas)
training_data_aux = [];
training_data = np.array([], "float32")

with open('training_data_inputs.csv', newline='') as File:
    rows = csv.reader(File)
    for row in rows:
        training_data_aux.append([int(x) for x in row]);

training_data = np.array(training_data_aux, "float32")
# print(training_data);

# Carga de data de entrenamiento (salida)
target_data_aux = [];
target_data = np.array([], "float32")

with open('training_data_outputs.csv', newline='') as File:
    rows = csv.reader(File)
    for row in rows:
        target_data_aux.append([int(x) for x in row]);

target_data = np.array(target_data_aux, "float32")
# print(target_data);

# Creamos el modelo
model = Sequential()
model.add(Dense(16, input_dim=4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])
model.fit(training_data, target_data, epochs=1000)

# Evaluamos el modelo
scores = model.evaluate(training_data, target_data)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# Guardar el Modelo
model.save('path_to_my_model.h5')
import numpy as np
import tensorflow as tf

# Copia aquí la respuesta
predictions = [
    [-7.65669394, -10.1959171, -6.22993946, -7.20177841, -6.69292784, 1.10157645, -4.40913725, 3.29627895, -0.192728877, 5.79238844], 
    [-5.57733583, -17.2078362, 2.20715547, -9.84295, -2.08657098, -34.5174446, -2.68788958, -41.3530312, -11.2888508, -29.2192097], 
    [-5.99404192, 8.86673069, -11.6140099, -3.31085, -3.01104093, -19.0466709, -10.2557392, -18.4010696, -10.3293829, -14.6171398]
]

# Convertir las puntuaciones en probabilidades
probabilities = tf.nn.softmax(predictions).numpy()

# Encontrar las clases predichas
predicted_classes = np.argmax(probabilities, axis=1)

# Mostrar los resultados
for i, (pred, prob) in enumerate(zip(predicted_classes, probabilities)):
    print(f"Ejemplo {i + 1}:")
    print(f"Clase predicha: {pred}")
    print(f"Probabilidades: {prob}")
    print()




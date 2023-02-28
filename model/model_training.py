from tensorflow import keras
import tensorflow as tf
import matplotlib.pyplot as plt


class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


def prepare_data():
  print("Loading data...")
  fashion_mnist = keras.datasets.fashion_mnist
  (train_images, train_labels), (test_images,
                                 test_labels) = fashion_mnist.load_data()

  # scale the values to 0.0 to 1.0
  train_images = train_images / 255.0
  test_images = test_images / 255.0

  # reshape for feeding into the model
  train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
  test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

  print(f"\nTrain_images.shape: {train_images.shape}, of {train_images.dtype}")
  print(f"Test_images.shape: {test_images.shape}, of {test_images.dtype}")

  return train_images, train_labels, test_images, test_labels


def train_model(train_images, train_labels):
  model = keras.Sequential([
      keras.layers.Conv2D(input_shape=(28, 28, 1), filters=8, kernel_size=3,
                          strides=2, activation='relu', name='Conv1'),
      keras.layers.Flatten(),
      keras.layers.Dense(10, name='Dense')
  ])
  model.summary()

  model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(
                    from_logits=True),
                metrics=[keras.metrics.SparseCategoricalAccuracy()])
  history = model.fit(train_images, train_labels, epochs=5)

  plt.xlabel('Epoch Number')
  plt.ylabel("Loss Magnitude")
  plt.plot(history.history['loss'])
  plt.show()

  return model


def evaluate_model(model, test_images, test_labels):
  test_loss, test_acc = model.evaluate(test_images, test_labels)
  print(f"\nTest accuracy: {test_acc}")
  print(f"\nTest loss: {test_loss}")

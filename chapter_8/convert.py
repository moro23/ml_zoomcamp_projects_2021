import tensorflow as tf
from tensorflow import keras 

## lets load the keras model
model = keras.models.load_model('models/xception_v1_06_0.925.h5')

## lets convert it the model to TF Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

with tf.io.gfile.GFile('clothing-model-v4.tflite', 'wb') as f:
    f.write(tflite_model)
    
  
## import libraries
import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor


## create a preprocessor
preprocessor = create_preprocessor('xception', target_size=(299, 299))

## load the model, and get the output and input
## create the tf lite interpreter
interpreter = tflite.Interpreter('clothing-model-v4.tflite')

## initializes the interpreter with the model
interpreter.allocate_tensors()

##
input_details = interpreter.get_input_details()
input_index = input_details[0]['index']

## 
output_details = interpreter.get_output_details()
output_index = output_details[0]['index']

## create a function for making predictions
def predict(X):
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    ##
    preds = interpreter.get_tensor(output_index)
    return preds[0]


## create a function for preparing results
labels = [
'dress',
'hat',
'longsleeve',
'outwear',
'pants',
'shirt',
'shoes',
'shorts',
'skirt',
't-shirt'
]

def decode_predictions(pred):
    results = {c: float(p) for c, p in zip(labels, pred)}
    return result

## lets put everythin together in one function
def lambda_handler(event, context):
    url = event['url']
    X = preprocessor.from_url(url)
    preds = predict(X)
    results = decode_predictions(preds)
    return results


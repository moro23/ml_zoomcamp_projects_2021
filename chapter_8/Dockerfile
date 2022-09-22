## lets use the official docker image
FROM public.ecr.aws/lambda/python:3.9

## install keras_image_helper
RUN pip3 install keras_image_helper --no-cache-dir
RUN pip3 install tflite-runtime --no-cache-dir
## copies the model
COPY clothing-model-v4.tflite clothing-model-v4.tflite

## copies the lambda function
COPY lambda_function.py lambda_function.py 

## defines the location of the lambda function
CMD  ["lamda_function.lambda_handler"]


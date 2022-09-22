from distutils.log import debug
from flask import Flask

## lets create a flask app
app = Flask('test')

## lets assign the function to an address/ route 

@app.route('/ping', methods=['GET'])
def ping():
    return 'PONG'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
import pickle
import numpy as np
from flask import Flask, request, jsonify 


## lets assign the /predict route to the predict function

def predict_single(customer, dv, model):
    """
    This function picks an instance of a customer data and transfroms
    it into a Vectorize dictionary. Applies the model prediction and 
    returns the prediction
    """
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:,1]

    return y_pred[0]
    
with open('churn-model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    ## converts the customer data into a JSON 
    customer = request.get_json()
     
    ## 

    prediction = predict_single(customer, dv, model)
    churn = prediction >= 0.5

    ## lets prepare the response 
    result = {
        'churn_probability': float(prediction),
        'churn': bool(churn)
    }

        ##
    return jsonify(result)

if __name__ ==  '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
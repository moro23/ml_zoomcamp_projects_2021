from unittest import result
import requests

data = {
    "url": "http://bit.ly/mlbookcamp-pants"
}

## specify the url 
url = "http://localhost:8080/2015-03-31/functions/function/invocations"

## sends a POST request to the service
results = requests.post(url, json=data).json()
print(results)
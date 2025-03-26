from flask import Flask, request
from flask_cors import CORS
import os
import model
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../model")))


app = Flask(__name__)
CORS(app)


@app.route('/api/getResult',methods = ['POST', 'GET'])
def getResult():
    if request.method == 'POST':

        req = request.get_json()
        result = model.getResult(list(req.values()))
        return result

    elif request.method == 'GET':

        result = model.getResultAmaGet()
        return result
    
    else:
        return ""


if __name__ == '__main__':
    app.run()

from flask import Flask, request, jsonify
from flask_cors import CORS 
from get_gotchis import get_gotchis_by_address, get_gotchi_by_id

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/users/<address>', methods=['GET'])
def api_gotchis_by_address(address):
    address = address.lower()
    results = get_gotchis_by_address(address)
    return jsonify(results)

@app.route('/api/gotchis/<gotchi_id>', methods=['GET'])
def api_get_gotchi(gotchi_id):
    results = get_gotchi_by_id(gotchi_id)
    return jsonify(results)


if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run() #run app
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/api/search')
def search_equipment():
    query = request.args.get('query')
    specs = {
        'model': query,
        'weight': '6,000 lbs',
        'engine': 'Kubota Diesel V2403',
        'operating_capacity': '2,000 lbs'
    }
    listings = [
        {'title': f'{query} for sale at Dealer A', 'price': '$28,000', 'link': 'https://dealera.com/listing1'},
        {'title': f'{query} on EquipmentTrader', 'price': '$29,500', 'link': 'https://equipmenttrader.com/listing2'}
    ]
    return jsonify({'specs': specs, 'listings': listings})

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


"""
    Inventory Service:
    Håndterer lagerbeholdningen for produkter.
    Sporer ændringer i lageret (f.eks. justeringer af mængden efter salg).
"""

from flask import Flask, jsonify, request
from services.products import fetch_product_details
from persistance.db import read, init_db, create, update

app = Flask(__name__)

init_db()

@app.route('/inventory/<int:product_id>', methods=['GET'])
def get_inventory(product_id):
    inventory = read(product_id)
    if not inventory:
        return jsonify({'message': 'Product not found in inventory'}), 404

    product_details = fetch_product_details(product_id)
    if not product_details:
        return jsonify({'message': 'Product details not found'}), 404

    response = {
        'product': product_details,
        'stock': inventory[1]
    }

    return jsonify(response)

@app.route('/inventory/<int:product_id>', methods=['PUT'])
def update_inventory(product_id):
    data = request.json
    change_in_stock = data.get('change_in_stock')
    
    if change_in_stock is None:
        return jsonify({'message': 'change_in_stock is required'}), 400

    if not read(product_id):
        create((product_id, change_in_stock))
        return jsonify({'message': 'New product created'}), 201
        #db[product_id] = {"product_id": product_id, "stock": 0}
    else:
        update((product_id, change_in_stock))
    #db[product_id]['stock'] += change_in_stock
        return jsonify({'message': 'Inventory updated successfully'}), 201

app.run(debug=True, port=5001, host='0.0.0.0') 
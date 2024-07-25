from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database
items = {}

# GET method to fetch items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# POST method to add an item
@app.route('/items', methods=['POST'])
def add_item():
    item_id = request.json.get('id')
    item_name = request.json.get('name')
    if not item_id or not item_name:
        return jsonify({"message": "Invalid data"}), 400
    items[item_id] = item_name
    return jsonify({"message": "Item added"}), 201

# PATCH method to update an item
@app.route('/items/<item_id>', methods=['PATCH'])
def update_item(item_id):
    if item_id not in items:
        return jsonify({"message": "Item not found"}), 404
    item_name = request.json.get('name')
    if not item_name:
        return jsonify({"message": "Invalid data"}), 400
    items[item_id] = item_name
    return jsonify({"message": "Item updated"}), 200

# DELETE method to delete an item
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({"message": "Item not found"}), 404
    del items[item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

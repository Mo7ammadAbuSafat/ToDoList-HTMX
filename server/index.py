from flask import Flask, render_template, jsonify, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

items = []

@app.route('/add_item', methods=['POST'])
def add_item():
    name = request.form.get('name')
    if name:
        items.append(name)
        return Response(status=204)
    return jsonify(success=False, message='Item name is required'), 400

@app.route('/delete_item/<int:item_index>', methods=['DELETE'])
def delete_item(item_index):
    if 0 <= item_index < len(items):
        del items[item_index]
        return Response(status=204)
    return jsonify(success=False, message='Item not found'), 404

@app.route('/get_items', methods=['GET'])
def refresh_items():
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
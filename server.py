from flask import Flask, jsonify, request
app = Flask(__name__)
orders = []
@app.route('/icecream/order', methods=['POST'])
def save_order():
    data = request.json
    flavor = data.get('flavor')
    quantity = data.get('quantity')
    if flavor and quantity:
        orders.append({'flavor': flavor, 'quantity': quantity})
        return jsonify({'message': f"Количество{quantity} порций {flavor} мороженного"}), 201
    return jsonify({'error': "Invalid order"}), 400

if __name__=="__main__":
    app.run(debug=True)
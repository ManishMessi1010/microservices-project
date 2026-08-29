from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/orders')
def orders():
    return jsonify({
        "orders": [
            "order-101",
            "order-102",
            "order-103"
        ]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def products():
    return jsonify({
        "products": [
            "Laptop",
            "Phone",
            "Keyboard"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

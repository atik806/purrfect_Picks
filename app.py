import os
from flask import Flask, render_template, send_from_directory, request as flask_request

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

# Vercel handler
def handler(req, context):
    with app.test_request_context(
        path=req.url_path,
        method=req.method,
        headers=dict(req.headers),
        query_string=req.url.query
    ):
        response = app.full_dispatch_request(flask_request)
        return {
            "statusCode": response.status_code,
            "headers": dict(response.headers),
            "body": response.get_data(as_text=True)
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

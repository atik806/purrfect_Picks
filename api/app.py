import os
from flask import Flask, render_template

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(basedir, "..", "templates"),
    static_folder=os.path.join(basedir, "..", "static")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/product")
def product():
    return render_template("product.html")

# Vercel serverless function handler
def handler(request):
    return app(request.environ, request.start_response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

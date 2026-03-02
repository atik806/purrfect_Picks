import os
from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from functools import wraps
from dotenv import load_dotenv
import re

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(basedir, "..", "templates"),
    static_folder=os.path.join(basedir, "..", "static")
)

# Security configurations
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(32))
app.config['SESSION_COOKIE_SECURE'] = True  # HTTPS only
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevent XSS
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # CSRF protection
app.config['PERMANENT_SESSION_LIFETIME'] = 3600  # 1 hour

# Security headers middleware
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.gstatic.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self' https://*.firebaseio.com https://*.googleapis.com"
    return response

# Admin authentication decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_authenticated' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Input validation helpers
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    # Bangladesh phone number format
    pattern = r'^(\+?880|0)?1[3-9]\d{8}$'
    return re.match(pattern, phone) is not None

def sanitize_input(text):
    if not text:
        return ""
    # Remove potential XSS patterns
    text = str(text).strip()
    dangerous_patterns = ['<script', 'javascript:', 'onerror=', 'onclick=']
    for pattern in dangerous_patterns:
        text = text.replace(pattern, '')
    return text

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
@admin_required
def admin():
    return render_template("admin.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route("/api/verify-admin", methods=['POST'])
def verify_admin():
    """Verify Firebase ID token and create session"""
    try:
        data = request.get_json()
        id_token = data.get('idToken')
        
        if not id_token:
            return jsonify({'error': 'No token provided'}), 401
        
        # In production, verify the token with Firebase Admin SDK
        # For now, we'll trust the client-side authentication
        # TODO: Implement Firebase Admin SDK verification
        
        session['admin_authenticated'] = True
        session.permanent = True
        
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/validate-order", methods=['POST'])
def validate_order():
    """Validate order data before submission"""
    try:
        data = request.get_json()
        
        # Validate customer info
        name = sanitize_input(data.get('customer', {}).get('name', ''))
        phone = data.get('customer', {}).get('phone', '')
        address = sanitize_input(data.get('customer', {}).get('address', ''))
        
        errors = []
        
        if not name or len(name) < 2:
            errors.append('Invalid name')
        
        if not validate_phone(phone):
            errors.append('Invalid phone number')
        
        if not address or len(address) < 10:
            errors.append('Invalid address')
        
        if errors:
            return jsonify({'valid': False, 'errors': errors}), 400
        
        return jsonify({'valid': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host="127.0.0.1", port=5000)

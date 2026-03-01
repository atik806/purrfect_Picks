# Purrfect Picks - Cat Accessories

Website Live on: https://purrfect-picks-sigma.vercel.app/

A complete e-commerce website for cat accessories with Firebase Realtime Database, shopping cart, checkout, and admin panel.

## Tech Stack

- **Frontend:** HTML5, CSS3 (Glassmorphism design)
- **Backend:** Python Flask
- **Database:** Firebase Realtime Database
- **Authentication:** Firebase Authentication

## Features

### Customer Features
- 🛒 **Shopping Cart** - Add products, modify quantities, remove items
- 📝 **Checkout** - Full order form with shipping & payment options
- 📱 **Responsive Design** - Works on mobile and desktop
- 🎨 **Glassmorphism UI** - Modern transparent glass style
- ⭐ **Product Details** - Click any product to see full details

### Admin Features
- 🔐 **Admin Login** - Secure authentication
- 📦 **Product Management** - Add, edit, delete products
- 📋 **Order Management** - View and update order status
- 📊 **Order Tracking** - Track orders: Pending → Confirmed → Shipped → Delivered

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Firebase:**
   - Go to [Firebase Console](https://console.firebase.google.com/)
   - Select project: `catproduct-f6852`
   - Enable **Authentication** > Email/Password
   - Enable **Realtime Database** > Start in test mode

3. **Create admin user:**
   - Go to Authentication > Add user
   - Enter your admin email and password

4. **Run the server:**
   ```bash
   python app.py
   ```

5. Open `http://localhost:5000`

## Routes

| Route | Description |
|-------|-------------|
| `/` | Main website with products |
| `/product` | Product detail page (add `?id=PRODUCT_ID`) |
| `/about` | About us page |
| `/cart` | Shopping cart |
| `/checkout` | Checkout page |
| `/login` | Admin login |
| `/admin` | Admin panel (protected) |

## Payment Methods

- 💵 Cash on Delivery
- 💳 Credit/Debit Card
- 📱 bKash

## Project Structure

```
cat web/
├── app.py                  # Flask backend
├── firebase-config.json    # Firebase config (not committed)
├── firebase-rule.md       # Firebase rules guide
├── requirements.txt        # Python dependencies
├── .gitignore            # Git ignore rules
├── static/
│   └── images/
│       └── image.jpg
└── templates/
    ├── index.html         # Main website
    ├── product.html       # Product details page
    ├── about.html        # About us page
    ├── cart.html         # Shopping cart
    ├── checkout.html     # Checkout page
    ├── admin.html       # Admin panel
    └── login.html       # Admin login
```

## Security

- Add `firebase-config.json` and any sensitive files to `.gitignore`
- For production, update Firebase rules to require authentication

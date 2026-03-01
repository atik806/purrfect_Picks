# Purrfect Picks - Cat Accessories Landing Page

A Flask-based landing page for cat accessories with Firebase database integration and admin panel.

## Tech Stack

- **Frontend:** HTML5, CSS3 (Glassmorphism design)
- **Backend:** Python Flask
- **Database:** Firebase Firestore

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Firebase:**
   - Go to [Firebase Console](https://console.firebase.google.com/)
   - Create a new project
   - Enable Firestore Database
   - Go to Project Settings > Service Accounts
   - Generate new private key
   - Replace `firebase-config.json` with your credentials

3. **Run the server:**
   ```bash
   cd "cat web"
   python app.py
   ```

4. Open `http://localhost:5000` in your browser

## Admin Panel

Access the admin panel at `http://localhost:5000/admin` to:
- Add new products
- Edit existing products
- Delete products

## Project Structure

```
cat web/
├── app.py                  # Flask backend with Firebase integration
├── firebase-config.json    # Firebase credentials (add your own)
├── requirements.txt       # Python dependencies
├── static/
│   └── images/
│       └── image.jpg
└── templates/
    ├── index.html         # Main website
    └── admin.html         # Admin panel
```

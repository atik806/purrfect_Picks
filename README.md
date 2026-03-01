# Purrfect Picks - Cat Accessories

A Flask-based landing page for cat accessories with Firebase Realtime Database and admin panel.

## Tech Stack

- **Frontend:** HTML5, CSS3 (Glassmorphism design)
- **Backend:** Python Flask
- **Database:** Firebase Realtime Database
- **Authentication:** Firebase Authentication

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
| `/` | Main website |
| `/login` | Admin login |
| `/admin` | Admin panel (protected) |

## Admin Panel Features

- Add new products
- Edit existing products
- Delete products
- Logout

## Project Structure

```
cat web/
├── app.py                  # Flask backend
├── firebase-config.json    # Firebase config (not committed)
├── firebase-rule.md        # Firebase rules guide
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── static/
│   └── images/
│       └── image.jpg
└── templates/
    ├── index.html         # Main website
    ├── admin.html         # Admin panel
    └── login.html         # Admin login
```

## Security

- Add `firebase-config.json` and any sensitive files to `.gitignore`
- For production, update Firebase rules to require authentication

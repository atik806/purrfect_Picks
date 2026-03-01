# Firebase Rules

## Authentication Setup

### Enable Authentication
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select project: `catproduct-f6852`
3. Click **Authentication** in the left menu
4. Click **Get Started**
5. Enable **Email/Password** sign-in method
6. Click **Save**

---

## Realtime Database Rules

Go to Firebase Console > Realtime Database > Rules

### Development/Testing (Not Secure)
```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

### Production (Secure - Requires Auth)
```json
{
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null",
    "admins": {
      "$uid": {
        ".read": "auth != null && data.child('email').val() === auth.token.email || root.child('admins').child(auth.uid).exists()",
        ".write": "auth != null && root.child('admins').child(auth.uid).exists()"
      }
    },
    "products": {
      ".read": true,
      ".write": "auth != null && root.child('admins').child(auth.uid).exists()"
    }
  }
}
```

---

## How to Create Admin Users

### Method 1: First User (Manual)
1. Go to Firebase Console > Authentication
2. Manually add user with email: `admin@purrfectpicks.com`
3. Go to Realtime Database
4. Add this structure:
```json
{
  "admins": {
    "USER_UID_HERE": {
      "email": "admin@purrfectpicks.com",
      "role": "admin"
    }
  }
}
```

### Method 2: Sign Up via Login Page
1. Go to `/login` page
2. Click "Sign up" link
3. Enter email and password (min 6 characters)
4. The user will be automatically added as admin

---

## Security Notes

- **Test mode**: Anyone can read/write (fine for development)
- **Locked mode**: Only authenticated users can access
- **Production**: Use authenticated rules with admin validation

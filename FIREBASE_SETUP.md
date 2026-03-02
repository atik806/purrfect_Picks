# Firebase Security Rules Setup

## Current Issue

Your Firebase security rules are blocking product reads and writes because they require:
1. `auth.token.admin === true` - This custom claim is NOT set in your app
2. Too restrictive authentication requirements

## ✅ Correct Security Rules

Copy and paste these rules into your Firebase Console:

### Option 1: Balanced Security (Recommended)

```json
{
  "rules": {
    "products": {
      ".read": true,
      ".write": "auth != null"
    },
    "orders": {
      ".read": "auth != null",
      ".write": true,
      "$orderId": {
        ".validate": "newData.hasChildren(['items', 'customer', 'total', 'paymentMethod', 'status', 'createdAt'])"
      }
    }
  }
}
```

**What this does:**
- ✅ Anyone can READ products (needed for public website)
- ✅ Only authenticated users can WRITE products (admin panel)
- ✅ Only authenticated users can READ orders (admin panel)
- ✅ Anyone can WRITE orders (customers placing orders)
- ✅ Validates order structure

### Option 2: Development/Testing (Less Secure)

```json
{
  "rules": {
    "products": {
      ".read": true,
      ".write": true
    },
    "orders": {
      ".read": true,
      ".write": true
    }
  }
}
```

**Use this ONLY for testing!** Switch to Option 1 before going live.

## How to Apply Rules

### Step 1: Go to Firebase Console
1. Visit: https://console.firebase.google.com/
2. Select your project: `catproduct-f6852`

### Step 2: Navigate to Realtime Database
1. Click "Realtime Database" in the left menu
2. Click the "Rules" tab at the top

### Step 3: Replace Rules
1. Delete all existing rules
2. Copy the rules from **Option 1** above
3. Click "Publish"

### Step 4: Test
1. Refresh your website
2. Products should now appear in "Trending Products"
3. Login to admin panel
4. Try adding a new product

## Troubleshooting

### Products Still Not Showing?

**Check Browser Console:**
1. Press F12 to open DevTools
2. Go to Console tab
3. Look for Firebase errors

**Common Errors:**

**Error: "Permission denied"**
- Solution: Make sure you published the new rules
- Wait 30 seconds after publishing for rules to propagate

**Error: "CORS policy"**
- Solution: This is the CSP header issue (already fixed in latest code)
- Restart your Flask server: `python api/app.py`

**Error: "Firebase not defined"**
- Solution: Check internet connection, Firebase CDN might be blocked

### Admin Cannot Add Products?

**Check if logged in:**
1. Open browser DevTools (F12)
2. Go to Application tab → Cookies
3. Look for session cookie
4. If not there, login again at `/login`

**Check Firebase Authentication:**
1. Go to Firebase Console → Authentication
2. Make sure you have a user created
3. Try logging in with that user

**Check browser console for errors:**
- Look for authentication errors
- Look for Firebase permission errors

## Understanding the Rules

### Products Rules Explained

```json
"products": {
  ".read": true,           // Anyone can view products (public website)
  ".write": "auth != null" // Only logged-in users can add/edit/delete
}
```

- `.read: true` - Allows public access to view products
- `.write: "auth != null"` - Requires Firebase Authentication to modify

### Orders Rules Explained

```json
"orders": {
  ".read": "auth != null",  // Only logged-in users can view orders
  ".write": true,           // Anyone can create orders (customers)
  "$orderId": {
    ".validate": "..."      // Ensures order has required fields
  }
}
```

- `.read: "auth != null"` - Only admin (logged in) can view orders
- `.write: true` - Customers can place orders without login
- `.validate` - Ensures data integrity

## Security Considerations

### Why allow public writes to orders?

Your app allows customers to checkout WITHOUT creating an account. This is common for e-commerce sites. The validation rules ensure orders have the correct structure.

### How to make it more secure?

**Option A: Require customer authentication**
```json
"orders": {
  ".read": "auth != null",
  ".write": "auth != null"  // Require login to place orders
}
```
Then update your checkout flow to require user login.

**Option B: Use custom claims for admin**

This requires backend setup with Firebase Admin SDK:

1. Install Firebase Admin SDK:
```bash
pip install firebase-admin
```

2. Set custom claims when admin logs in (backend code needed)

3. Update rules:
```json
"products": {
  ".read": true,
  ".write": "auth != null && auth.token.admin === true"
}
```

This is more secure but requires additional backend code.

## Quick Test Commands

### Test if rules are working:

**From browser console (F12):**

```javascript
// Test reading products
firebase.database().ref('products').once('value')
  .then(snapshot => console.log('Products:', snapshot.val()))
  .catch(error => console.error('Error:', error));

// Test writing (after login)
firebase.database().ref('products').push({
  name: 'Test Product',
  price: 100,
  icon: '🐱'
})
.then(() => console.log('Write successful!'))
.catch(error => console.error('Write error:', error));
```

## Current Rules vs Your Rules

### ❌ Your Current Rules (Not Working)
```json
{
  "products": {
    ".read": true,
    ".write": "auth != null && auth.token.admin === true"  // ❌ Requires custom claim
  }
}
```

**Problem:** `auth.token.admin === true` requires setting up custom claims with Firebase Admin SDK, which your app doesn't do.

### ✅ Recommended Rules (Working)
```json
{
  "products": {
    ".read": true,
    ".write": "auth != null"  // ✅ Just requires authentication
  }
}
```

**Solution:** Any authenticated user can write. Since only admins have accounts, this is secure enough.

## Next Steps

1. ✅ Apply the recommended rules (Option 1)
2. ✅ Test products loading on homepage
3. ✅ Test admin can add products
4. ✅ Test customers can place orders
5. 📝 Consider implementing custom claims for production (optional)

## Need Help?

If products still don't show after applying rules:
1. Check browser console for errors (F12)
2. Verify rules are published in Firebase Console
3. Clear browser cache and reload
4. Restart Flask server
5. Check if Firebase project ID matches in code

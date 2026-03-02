# Quick Start: Security Setup

## Immediate Actions Required (5 minutes)

### 1. Generate Secret Key
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
Copy the output and add it to your `.env` file:
```
SECRET_KEY=your-generated-key-here
```

### 2. Install New Dependencies
```bash
pip install -r requirements.txt
```

### 3. Update Firebase Security Rules

Go to [Firebase Console](https://console.firebase.google.com/) → Your Project → Realtime Database → Rules

Replace with:
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
        ".validate": "newData.hasChildren(['items', 'customer', 'total', 'status'])"
      }
    }
  }
}
```

### 4. Test Locally
```bash
python api/app.py
```

Visit: http://127.0.0.1:5000

### 5. Deploy to Production

**Vercel Environment Variables:**
1. Go to Vercel Dashboard → Your Project → Settings → Environment Variables
2. Add these variables:
   - `SECRET_KEY` = (your generated secret key)
   - `FLASK_ENV` = production
   - `FLASK_DEBUG` = False
   - All Firebase variables from `.env`

## What Changed?

### ✅ Security Improvements Applied

1. **Backend Protection**
   - Admin routes now require authentication
   - Secure session cookies (HttpOnly, Secure, SameSite)
   - Security headers added (CSP, HSTS, X-Frame-Options)
   - Debug mode disabled in production

2. **Configuration**
   - Environment variables for sensitive data
   - Strong secret key for session encryption
   - Proper .gitignore configuration

3. **Input Validation**
   - Server-side validation for forms
   - XSS protection through sanitization
   - Phone and email validation

4. **Session Security**
   - Server-side session management
   - Automatic session expiration (1 hour)
   - Secure logout functionality

## Testing the Security

### Test 1: Admin Access Protection
1. Open browser in incognito mode
2. Try to access: http://127.0.0.1:5000/admin
3. Should redirect to login page ✅

### Test 2: Session Security
1. Login to admin panel
2. Check browser cookies (DevTools → Application → Cookies)
3. Verify flags: HttpOnly ✅, Secure ✅, SameSite ✅

### Test 3: Security Headers
1. Open DevTools → Network tab
2. Refresh any page
3. Check Response Headers:
   - X-Frame-Options: DENY ✅
   - X-Content-Type-Options: nosniff ✅
   - Strict-Transport-Security ✅

## Common Issues

### Issue: "Session cookie requires HTTPS"
**Solution**: In development, this is expected. The app will work on localhost. In production, ensure HTTPS is enabled.

### Issue: "Admin page redirects to login"
**Solution**: This is correct behavior! Login first at `/login`

### Issue: "Firebase permission denied"
**Solution**: Update Firebase security rules as shown above

## Next Steps

After basic setup:
1. Review `SECURITY_CHECKLIST.md` for additional improvements
2. Read `SECURITY.md` for detailed explanations
3. Consider implementing rate limiting
4. Set up monitoring and logging

## Need Help?

- Check `SECURITY.md` for detailed documentation
- Review `SECURITY_CHECKLIST.md` for complete checklist
- Test each security feature individually

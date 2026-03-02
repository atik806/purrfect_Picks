#!/usr/bin/env python3
"""
Debug script to test Firebase connection and product loading
Run this to check if the issue is with Flask or Firebase
"""

import requests
import json

def test_firebase_direct():
    """Test Firebase REST API directly"""
    print("🔥 Testing Firebase REST API directly...")
    
    # Firebase REST API URL
    url = "https://catproduct-f6852-default-rtdb.firebaseio.com/products.json"
    
    try:
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data:
                print(f"✅ SUCCESS: Found {len(data)} products")
                print("Products:")
                for key, product in data.items():
                    print(f"  - {product.get('name', 'Unknown')} (${product.get('price', 0)})")
                return True
            else:
                print("⚠️  SUCCESS: Connected but no products found")
                return True
        else:
            print(f"❌ FAILED: HTTP {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ NETWORK ERROR: {e}")
        return False

def test_flask_server():
    """Test if Flask server is running"""
    print("\n🌐 Testing Flask server...")
    
    try:
        response = requests.get("http://127.0.0.1:5000", timeout=5)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Flask server is running")
            return True
        else:
            print(f"❌ Flask server error: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Flask server not accessible: {e}")
        print("Make sure to run: python api/app.py")
        return False

def test_firebase_rules():
    """Test Firebase security rules"""
    print("\n🔒 Testing Firebase security rules...")
    
    # Test read access (should work)
    url = "https://catproduct-f6852-default-rtdb.firebaseio.com/products.json"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Read access: ALLOWED")
        else:
            print(f"❌ Read access: DENIED ({response.status_code})")
            
    except Exception as e:
        print(f"❌ Rules test failed: {e}")

def main():
    print("🐱 Purrfect Picks - Firebase Debug Tool")
    print("=" * 50)
    
    # Test Firebase directly
    firebase_ok = test_firebase_direct()
    
    # Test Flask server
    flask_ok = test_flask_server()
    
    # Test Firebase rules
    test_firebase_rules()
    
    print("\n" + "=" * 50)
    print("📋 SUMMARY:")
    print(f"Firebase API: {'✅ OK' if firebase_ok else '❌ FAILED'}")
    print(f"Flask Server: {'✅ OK' if flask_ok else '❌ FAILED'}")
    
    if firebase_ok and flask_ok:
        print("\n🎉 Both Firebase and Flask are working!")
        print("The issue might be:")
        print("1. Content Security Policy blocking Firebase in browser")
        print("2. JavaScript errors in browser console")
        print("3. Firebase rules changed after testing")
        print("\nNext steps:")
        print("1. Open browser DevTools (F12) and check Console tab")
        print("2. Visit: http://127.0.0.1:5000/test")
        print("3. Look for any error messages")
    elif firebase_ok and not flask_ok:
        print("\n🔧 Firebase works but Flask doesn't!")
        print("Solution: Start Flask server with: python api/app.py")
    elif not firebase_ok and flask_ok:
        print("\n🔧 Flask works but Firebase doesn't!")
        print("Solution: Check Firebase rules and network connection")
    else:
        print("\n🚨 Both Firebase and Flask have issues!")
        print("Solution: Check network connection and Firebase configuration")

if __name__ == "__main__":
    main()
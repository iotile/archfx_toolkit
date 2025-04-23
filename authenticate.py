"""
Script: authenticate.py
Purpose: Authenticate to the ArchFX API and return an access token. This is the first step to using any APIs. This script is for local use only.

Instructions:
1. Edit `tenant_name`
2. Edit the credentials - username and password

System Requirements:
- Python v3 (may work for other versions, 3.9 works for sure)
- requests module

Arch Requirements:
- You must have a username password for Arch. SSO WILL NOT WORK FOR THIS.
"""

import requests

# ---- EDIT THIS SECTION ---
tenant_name = "your_tenant_name"
username = "your_email"
password = "your_password"

# --- BEGIN ---
auth_url = f"https://{tenant_name}.archfx.io/api/v1/auth/api-jwt-auth/"
credentials = {
    "username": username,
    "password": password 
}

auth_response = requests.post(auth_url, json=credentials)
auth_response.raise_for_status()

auth_data = auth_response.json()
access_token = auth_data.get("access") or auth_data.get("token")

headers = {
    "Authorization": f"JWT {access_token}",
    "Content-Type": "application/json"
}

# print(access_token)
print("✅ Auth successful. Access token stored in 'headers' variable.")

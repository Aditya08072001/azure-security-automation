import requests

TENANT_ID = "2d5cf188-464d-4592-a2f1-12fa21c36f4d"
CLIENT_ID = "df037682-89b4-40a3-a5f2-b2f7ba1f69ad"
CLIENT_SECRET = "CdG8Q~6J9BZg_Os7jkOtjBRe1h-VJTtMlg~7_aZ6"

# Get Access Token
token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

token_data = {
    "client_id": CLIENT_ID,
    "scope": "https://graph.microsoft.com/.default",
    "client_secret": CLIENT_SECRET,
    "grant_type": "client_credentials"
}

token_response = requests.post(token_url, data=token_data)

print("Token Status Code:", token_response.status_code)
print("Token Response:")
print(token_response.text)

# Stop if token request failed
if token_response.status_code != 200:
    exit()

access_token = token_response.json()["access_token"]

# Call Microsoft Graph
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(
    "https://graph.microsoft.com/v1.0/users?$top=10",
    headers=headers
)

print("\nGraph Status Code:", response.status_code)
print("Graph Response:")
print(response.text)
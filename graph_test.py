import requests

TENANT_ID = "TENANT_ID key"
CLIENT_ID = "CLIENT_ID key"
CLIENT_SECRET = "CLIENT_SECRET key"

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

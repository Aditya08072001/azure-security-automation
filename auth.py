import requests

TENANT_ID = "TENANT_ID key"
CLIENT_ID = "CLIENT_ID key"
CLIENT_SECRET = "CLIENT_SECRET key"

def get_access_token():

    token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

    token_data = {
        "client_id": CLIENT_ID,
        "scope": "https://graph.microsoft.com/.default",
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    response = requests.post(token_url, data=token_data)

    response.raise_for_status()

    return response.json()["access_token"]

token = get_access_token()

print("Token Generated Successfully")
print(token[:50])

import requests

TENANT_ID = "2d5cf188-464d-4592-a2f1-12fa21c36f4d"
CLIENT_ID = "df037682-89b4-40a3-a5f2-b2f7ba1f69ad"
CLIENT_SECRET = "CdG8Q~6J9BZg_Os7jkOtjBRe1h-VJTtMlg~7_aZ6"

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
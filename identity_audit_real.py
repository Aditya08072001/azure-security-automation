import requests
import csv

TENANT_ID = "2d5cf188-464d-4592-a2f1-12fa21c36f4d"
CLIENT_ID = "df037682-89b4-40a3-a5f2-b2f7ba1f69ad"
CLIENT_SECRET = "CdG8Q~6J9BZg_Os7jkOtjBRe1h-VJTtMlg~7_aZ6"

# Get Token
token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

token_data = {
    "client_id": CLIENT_ID,
    "scope": "https://graph.microsoft.com/.default",
    "client_secret": CLIENT_SECRET,
    "grant_type": "client_credentials"
}

token_response = requests.post(token_url, data=token_data)
access_token = token_response.json()["access_token"]

headers = {
    "Authorization": f"Bearer {access_token}"
}

# Get Users
response = requests.get(
    "https://graph.microsoft.com/v1.0/users?$select=displayName,userPrincipalName,accountEnabled",
    headers=headers
)

users = response.json()["value"]

# Generate Report
with open("identity_audit_report.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Display Name",
        "UPN",
        "Account Enabled",
        "Risk"
    ])

    for user in users:

        risk = "Low"

        if user.get("accountEnabled") is False:
            risk = "High"

        writer.writerow([
            user.get("displayName"),
            user.get("userPrincipalName"),
            user.get("accountEnabled"),
            risk
        ])

print(f"Users Audited: {len(users)}")
print("Identity Audit Report Generated")
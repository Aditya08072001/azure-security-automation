import requests
import csv

TENANT_ID = "TENANT_ID key"
CLIENT_ID = "CLIENT_ID key"
CLIENT_SECRET = "CLIENT_SECRET key"

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

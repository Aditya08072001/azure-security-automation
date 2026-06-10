import requests
from auth import get_access_token

token = get_access_token()

headers = {
    "Authorization": f"Bearer {token}"
}

url = "https://graph.microsoft.com/v1.0/users?$select=id,displayName,userPrincipalName,accountEnabled"

response = requests.get(url, headers=headers)

response.raise_for_status()

users = response.json()["value"]

disabled_users = []

for user in users:

    if user["accountEnabled"] == False:
        disabled_users.append(user)

print(f"\nDisabled Users Found: {len(disabled_users)}\n")

for user in disabled_users:

    print(f"Name : {user['displayName']}")
    print(f"UPN  : {user['userPrincipalName']}")
    print(f"ID   : {user['id']}")
    print("-" * 50)
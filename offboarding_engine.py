import requests
from auth import get_access_token

DRY_RUN = True

token = get_access_token()

headers = {
    "Authorization": f"Bearer {token}"
}

# Get all users
url = "https://graph.microsoft.com/v1.0/users?$select=id,displayName,userPrincipalName,accountEnabled"

response = requests.get(url, headers=headers)
users = response.json()["value"]

for user in users:

    if user["accountEnabled"] is False:

        print("\n" + "=" * 60)
        print("DISABLED USER FOUND")
        print("=" * 60)

        print(f"Name : {user['displayName']}")
        print(f"UPN  : {user['userPrincipalName']}")

        user_id = user["id"]

        groups_url = f"https://graph.microsoft.com/v1.0/users/{user_id}/memberOf"

        groups_response = requests.get(groups_url, headers=headers)

        groups = groups_response.json().get("value", [])

        print("\nGroups Found:")

        for group in groups:

            print(f"Would Remove Group : {group.get('displayName')}")

        print("\nDRY RUN COMPLETE")
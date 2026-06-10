import requests
from auth import get_access_token

USER_ID = "348cf04b-e3c3-4337-9787-ced5fa089502"

token = get_access_token()

headers = {
    "Authorization": f"Bearer {token}"
}

url = f"https://graph.microsoft.com/v1.0/users/{USER_ID}/memberOf"

response = requests.get(url, headers=headers)

response.raise_for_status()

groups = response.json().get("value", [])

print(f"\nGroups Found: {len(groups)}\n")

for group in groups:
    print("Name :", group.get("displayName"))
    print("ID   :", group.get("id"))
    print("-" * 50)
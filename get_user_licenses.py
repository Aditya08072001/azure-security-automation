import requests
from auth import get_access_token

USER_ID = "user id key"

token = get_access_token()

headers = {
    "Authorization": f"Bearer {token}"
}

url = f"https://graph.microsoft.com/v1.0/users/{USER_ID}/licenseDetails"

response = requests.get(url, headers=headers)

response.raise_for_status()

licenses = response.json()["value"]

print(f"\nLicenses Found: {len(licenses)}\n")

for license in licenses:
    print("SKU ID:", license["skuId"])
    print("-" * 50)

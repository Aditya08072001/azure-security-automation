import csv
import logging

from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient

# -------------------------
# CONFIGURATION
# -------------------------

SUBSCRIPTION_ID = "40a85ece-10ce-4d6e-b407-0ceeb73a56d1"

# -------------------------
# LOGGING
# -------------------------

logging.basicConfig(
    filename="azure_inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Script Started")

# -------------------------
# AUTHENTICATION
# -------------------------

credential = AzureCliCredential()

resource_client = ResourceManagementClient(
    credential,
    SUBSCRIPTION_ID
)

storage_client = StorageManagementClient(
    credential,
    SUBSCRIPTION_ID
)

# -------------------------
# CSV REPORT
# -------------------------

with open("azure_inventory_report.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Resource Type",
        "Name",
        "Location"
    ])

    # Resource Groups
    for rg in resource_client.resource_groups.list():

        writer.writerow([
            "Resource Group",
            rg.name,
            rg.location
        ])

        logging.info(f"Resource Group Found: {rg.name}")

    # Storage Accounts
    for storage in storage_client.storage_accounts.list():

        writer.writerow([
            "Storage Account",
            storage.name,
            storage.location
        ])

        logging.info(f"Storage Account Found: {storage.name}")

print("Inventory Report Generated")

logging.info("Script Completed")
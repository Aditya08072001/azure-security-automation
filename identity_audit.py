import csv

users = [
    {
        "displayName": "John Smith",
        "upn": "john@company.com",
        "enabled": False,
        "license": "E3"
    },
    {
        "displayName": "Alice Brown",
        "upn": "alice@company.com",
        "enabled": True,
        "license": "E3"
    },
    {
        "displayName": "Bob Wilson",
        "upn": "bob@company.com",
        "enabled": False,
        "license": "None"
    }
]

with open("identity_audit_report.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Display Name",
        "UPN",
        "Enabled",
        "License",
        "Risk"
    ])

    for user in users:

        risk = "Low"

        if not user["enabled"] and user["license"] != "None":
            risk = "Critical"

        writer.writerow([
            user["displayName"],
            user["upn"],
            user["enabled"],
            user["license"],
            risk
        ])

print("Identity Audit Report Generated")
import logging

logging.basicConfig(
    filename="identity_audit.log",
    level=logging.INFO
)

logging.info("Identity Audit Started")
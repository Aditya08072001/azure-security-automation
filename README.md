# 🔐 Azure Security Automation Project

## 📌 Overview
This project automates **license revocation and user access management** in Azure Entra ID based on inactivity rules.

---

## 🚀 Features
- Detect inactive users
- Automate license removal (E1/E3)
- Disable inactive accounts
- Generate audit logs
- Scalable DevOps automation approach

---

## 🏗 Architecture
Refer to `diagrams/architecture.mmd`

---

## 🧰 Tech Stack
- Python
- Azure Entra ID
- Active Directory (On-Prem optional)
- DevOps automation principles

---

## ⚙️ How to Run

```bash
pip install -r requirements.txt
python scripts/license_revoke.py

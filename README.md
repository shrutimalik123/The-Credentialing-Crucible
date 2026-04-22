# 📄 The Credentialing Crucible - Medical Staff Services Sim

A compliance-based simulation designed to teach the fundamentals of Physician Oversight and Provider Enrollment. You play as a Medical Staff Coordinator responsible for auditing the files of new and existing physicians. Your goal is to identify "Red Flags" in a provider's profile—such as expired licenses or missing board certifications—to ensure the hospital only grants privileges to fully qualified professionals.

This project focuses on teaching:
* **Primary Source Verification (PSV):** The administrative logic of cross-referencing multiple data points (License, DEA, Board Cert) before granting access.
* **Boolean Logic Gates:** Using `and` operators to ensure that 100% of requirements are met before a "Success" state is triggered.
* **Negligent Credentialing Risk:** Simulating the legal and financial consequences of administrative oversight in healthcare.
* **Database Auditing:** Iterating through a list of dictionaries to perform a standardized quality check on every entry.

---

## ✨ Features

* **Multi-Factor Verification:** Tracks three core pillars of medical practice: State Licenses, Federal DEA Registrations, and Specialty Board Certifications.
* **Negligent Credentialing Penalties:** Implements a heavy point-deduction system for granting privileges to non-compliant providers, mimicking real-world malpractice liability.
* **Revenue Impact Simulation:** Penalizes the "False Rejection" of qualified doctors, illustrating how administrative delays affect a hospital's bottom line.
* **Privileged Staff Directory:** Automatically generates a list of "Active Medical Staff" based on the player's successful audits.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `credentialing_sim.py`.
2.  **Open Terminal:** Navigate to the folder containing the file.
3.  **Run the Script:**
    ```bash
    python credentialing_sim.py
    ```

### 3. Gameplay Instructions
1.  **Review the File:** Examine the status of the three required documents for each doctor.
2.  **Verify Compliance:** * If all three documents are **[VALID]**, it is safe to grant privileges.
    * If any document is **[EXPIRED]**, you must deny privileges to protect the hospital.
3.  **Grant or Deny:** Enter **Y** to grant privileges or **N** to deny them.
4.  **Final Audit:** Achieve a score of 30 or higher to demonstrate total regulatory compliance.



---

## 🧠 Code Structure Highlights

### The "Three-Legged Stool" Logic
The core of the simulation is a Boolean verification. In medical staff services, there is no "partial" compliance; if one document is missing, the entire "True" state fails.

```python
# The three requirements for safe practice
is_actually_valid = p['license'] and p['dea'] and p['board_cert']


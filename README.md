# Cryptography & Network Security — Integrated Situation Assessment

**Module:** ETTCS801 Cryptography and Network Security  
**Lecturer:** Isaac TUMWINE  
**Institution:** ULK Polytechnic Institute  

---

## 1. Project Overview
This repository contains the complete technical deliverables for the ETTCS801 Integrated Situation assessment. It addresses critical security vulnerabilities found during a review of the polytechnic institute's infrastructure, including weak passwords, guest network access to sensitive assets, outdated software, and plain-text file transfers across campuses.

The project delivers:
- A structured risk assessment identifying assets, vulnerabilities, rankings, and controls.
- A robust Python security toolkit for AES-128/256-CBC (Fernet) file encryption, decryption, and SHA-256 integrity verification.
- Traffic filtering configuration (`iptables`) and test logs isolating the records server.
- A full LaTeX technical report summarizing the findings and implementation.

---

## 2. Repository Structure

```text
cryptography-network-security-exam/
│
├── README.md               # Overview, project structure, and execution guide
├── risk_assessment.md      # Assets, vulnerabilities, risk rankings, and controls
├── filter_tests.md         # Firewall configuration commands and netcat verification logs
├── security_toolkit.py     # Python script for encryption, decryption, and hash verification
├── report.tex              # Source code for the overall LaTeX technical report
└── report.pdf              # Compiled PDF report

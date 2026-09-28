# Risk Assessment Report

## 1. Assets, Vulnerabilities, and Consequences
1. **Asset:** Student Records Database / Records Server
   - **Vulnerability:** Unfiltered guest network access to the records server.
   - **Consequence:** Unauthorized internal access, data tampering, or full data breach of sensitive student records.
2. **Asset:** Student Files in Transit (Campus-to-Campus transfers)
   - **Vulnerability:** Unencrypted file transfer channels.
   - **Consequence:** Interception, eavesdropping (packet sniffing), and Man-in-the-Middle (MitM) attacks.
3. **Asset:** Administrative & Staff User Accounts
   - **Vulnerability:** Weak staff passwords and unpatched software.
   - **Consequence:** Brute-force credential compromise, system hijacking, and unauthorized operational access.

## 2. Risk Ranking (Likelihood and Impact)
1. **Unfiltered Guest Network Access (Risk 1)**
   - **Likelihood:** High | **Impact:** High
   - **Reasoning:** Guests share the local network infrastructure; direct access allows immediate targeting of internal server ports without external barriers.
2. **Unencrypted File Transfers & Weak Passwords (Risk 2)**
   - **Likelihood:** High | **Impact:** High
   - **Reasoning:** Automated dictionary attacks easily crack weak passwords, and plain text traffic on shared transit links exposes sensitive data continuously.
3. **External Server Probing Attempts (Risk 3)**
   - **Likelihood:** Medium | **Impact:** Medium-High
   - **Reasoning:** Unrestricted inbound exposure invites persistent external scanning and exploit attempts against outdated software.

## 3. Recommended Controls
1. **Control for Guest Access:** Implement strict firewall isolation (`iptables` / `ufw`) to drop all traffic originating from the guest subnet targeting the records server.
2. **Control for Data Transfers:** Mandate symmetric payload encryption (AES-256 via Python security toolkit) and transport-layer encryption (SFTP/TLS) for campus file transfers.
3. **Control for Unfiltered External Access:** Enforce strong authentication policies (12+ character complexity + MFA) and restrict external server access strictly to authorized management IP subnets.

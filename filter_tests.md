# Network Traffic Filtering Documentation

## Network Topology Assumptions
- **Records Server IP:** `192.168.10.100` (Service Port: SSH TCP 22 / Web TCP 80)
- **Staff Subnet:** `192.168.10.0/24`
- **Guest Subnet:** `192.168.20.0/24`
- **External Internet Range:** Any other IP source

## Firewall Rules Applied (`iptables`)
```bash
# Flush default rules
sudo iptables -F INPUT

# 3a. Block guest network access to the records server
sudo iptables -A INPUT -s 192.168.20.0/24 -d 192.168.10.100 -j DROP

# 3b. Permit authorized staff access to SSH (Port 22)
sudo iptables -A INPUT -p tcp -s 192.168.10.0/24 --dport 22 -d 192.168.10.100 -j ACCEPT

# 3c. Block all other inbound access to SSH (Port 22)
sudo iptables -A INPUT -p tcp --dport 22 -j DROP
```

## Traffic Filtering Test Logs

**Test 1: Permitted Connection (Staff Network)**

* **Source IP:** 192.168.10.15 (Staff Subnet)

* **Command:**
  ```bash
   nc -zv -w 3 192.168.10.100 22
  ```

* **Expected Outcome:** Connection Successful (OPEN)

* **Actual Result:** Connection to 192.168.10.100 22 port [tcp/ssh] succeeded!

**Test 2: Blocked Connection (Guest Network)**

* **Source IP:** 192.168.20.50 (Guest Subnet)

* **Command:**
  ```bash
   nc -zv -w 3 192.168.10.100 22
  ```

* **Expected Outcome:** Connection Timed Out / Dropped

* **Actual Result:** nc: connect to 192.168.10.100 port 22 (tcp) failed: Connection timed out

**Test 3: Blocked Connection (External Address)**

* **Source IP:** 198.51.100.44 (External Network)

* **Command:**
  ```bash
  nc -zv -w 3 192.168.10.100 22
  ```

* **Expected Outcome:** Connection Timed Out / Dropped

* **Actual Result:** nc: connect to 192.168.10.100 port 22 (tcp) failed: Connection timed out

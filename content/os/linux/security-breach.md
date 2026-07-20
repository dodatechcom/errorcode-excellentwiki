---
title: "[Solution] Linux: security-breach — security breach detected"
description: "Fix Linux security-breach errors. security breach detected with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["security"]
weight: 14
---
# Linux: Security Breach Indicators

Security breach indicators are signs that a Linux system may have been compromised. These require immediate investigation and response.

## Common Causes

- Unauthorized user access through stolen credentials or SSH keys
- Malware or rootkit installed through vulnerable services
- Brute force SSH attacks successfully compromising weak passwords
- Unpatched software exploited by remote attackers
- Misconfigured services exposed to the internet

## How to Fix

### 1. Check for Unauthorized Access

```bash
# Check recent logins
last -10
lastb -10

# Check currently logged in users
who -a
w

# Check auth logs for suspicious activity
sudo tail -100 /var/log/auth.log
sudo journalctl -u sshd -n 50
```

### 2. Check for Suspicious Processes

```bash
ps aux --sort=-%cpu | head -20
ps aux --sort=-%mem | head -20
# Look for unknown or suspicious commands
```

### 3. Check Network Connections

```bash
ss -tunap
lsof -i
netstat -tulpn
```

### 4. Check for Rootkits

```bash
sudo apt install rkhunter chkrootkit
sudo rkhunter --check
sudo chkrootkit
```

### 5. Check System File Integrity

```bash
# Verify package integrity
sudo debsums -c  # Debian/Ubuntu
sudo rpm -Va      # RHEL/CentOS
```

## Examples

```bash
$ last -10 | grep -v reboot | head -5
jdoe     pts/0        192.168.1.100    Mon Jul 20 14:30   still logged in
baduser  ssh          10.0.0.200       Sun Jul 19 03:15 - 03:20 (00:05)

$ sudo tail -20 /var/log/auth.log
Jul 20 03:15:01 server sshd[12345]: Failed password for root from 10.0.0.200 port 54321 ssh2
Jul 20 03:15:02 server sshd[12346]: Failed password for root from 10.0.0.200 port 54322 ssh2
Jul 20 03:15:03 server sshd[12347]: Failed password for root from 10.0.0.200 port 54323 ssh2
```

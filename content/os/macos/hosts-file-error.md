---
title: "[Solution] macOS Hosts File Error — DNS Override Not Working"
description: "Fix macOS hosts file error: hosts file changes not taking effect, DNS override not working, hosts file permissions issue."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 178
---

# Hosts File Error — DNS Override Not Working

Fix macOS hosts file error: hosts file changes not taking effect, DNS override not working, hosts file permissions issue.

## Common Causes

- DNS cache not flushed after hosts file change
- Hosts file permissions preventing modifications
- DNS resolver bypassing hosts file entries
- Hosts file syntax error in entry format

## How to Fix

### 1. Edit Hosts File

```bash
sudo nano /etc/hosts
# Add entries in format: 127.0.0.1 hostname
# Save with Ctrl+O, exit with Ctrl+X
```

### 2. Flush DNS Cache

```bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
```

### 3. Verify Hosts File Entries

```bash
cat /etc/hosts
# Check for syntax errors: entries must start with IP followed by space and hostname
```

### 4. Fix Hosts File Permissions

```bash
sudo chflags nouchg /etc/hosts
sudo chmod 644 /etc/hosts
```

## Common Scenarios

This error commonly occurs when:

- Custom hosts entries not redirecting to specified IP addresses
- hosts file changes disappear after macOS update
- DNS queries not respecting hosts file overrides
- Cannot save hosts file due to permissions error

## Prevent It

- Flush DNS cache after every hosts file modification
- Verify hosts file syntax is correct (IP space hostname)
- Keep backup of hosts file before making changes
- Use sudo when editing /etc/hosts to ensure write permissions

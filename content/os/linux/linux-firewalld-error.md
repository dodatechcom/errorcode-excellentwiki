---
title: "[Solution] Linux firewalld Configuration Error — Fix"
description: "Fix Linux firewalld configuration errors. Resolve zone, service, rule, and runtime issues with firewalld."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
tags: ["firewalld", "firewall", "configuration-error", "firewall-cmd", "network"]
weight: 5
---

# Linux: firewalld configuration error

firewalld configuration errors occur when firewall-cmd commands fail, zones are misconfigured, or runtime configurations cannot be applied. Common errors include `COMMAND_FAILED`, zone conflicts, and service definition issues.

## Common Causes

- Invalid zone name specified
- Service not defined in firewalld
- Conflicting rules between zones
- firewalld service not running
- XML configuration file syntax errors
- Interface assigned to multiple zones

## How to Fix

### 1. Check firewalld Status

```bash
# Check if firewalld is running
sudo systemctl status firewalld

# Start and enable
sudo systemctl start firewalld
sudo systemctl enable firewalld

# Check firewalld version
firewall-cmd --version
```

### 2. List Available Zones and Services

```bash
# List all zones
sudo firewall-cmd --get-zones

# List active zones
sudo firewall-cmd --get-active-zones

# List all services
sudo firewall-cmd --get-services

# List services in a zone
sudo firewall-cmd --zone=public --list-services
```

### 3. Fix COMMAND_FAILED Errors

```bash
# Typically means the service doesn't exist
sudo firewall-cmd --add-service=myapp
# Error: COMMAND_FAILED

# Check if the service definition exists
ls /usr/lib/firewalld/services/
ls /etc/firewalld/services/

# Create a custom service file if needed
sudo nano /etc/firewalld/services/myapp.xml
```

### 4. Create a Custom Service

```bash
# Create a service definition for a custom port
sudo nano /etc/firewalld/services/myapp.xml
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<service>
  <short>MyApp</short>
  <description>My Application</description>
  <port protocol="tcp" port="8080"/>
</service>
```

```bash
# Reload and add the service
sudo firewall-cmd --reload
sudo firewall-cmd --permanent --add-service=myapp
sudo firewall-cmd --reload
```

### 5. Fix Zone Assignment

```bash
# Check which zone an interface is in
sudo firewall-cmd --get-zone-of-interface=eth0

# Change interface zone
sudo firewall-cmd --zone=internal --change-interface=eth0

# Make permanent
sudo firewall-cmd --permanent --zone=internal --change-interface=eth0
```

### 6. Reload or Restart firewalld

```bash
# Reload without losing state
sudo firewall-cmd --reload

# Complete restart
sudo systemctl restart firewalld

# Reload with complete flush
sudo firewall-cmd --complete-reload
```

### 7. Check XML Configuration

```bash
# Validate zone configuration
sudo firewall-cmd --check-config

# View zone XML
sudo cat /etc/firewalld/zones/public.xml

# Fix any syntax errors in the XML
# Common issues: unclosed tags, invalid attributes
```

### 8. Reset firewalld to Defaults

```bash
# Remove all custom configuration
sudo firewall-cmd --reset-default-zone

# Remove all runtime rules
sudo firewall-cmd --panic-off

# Restore default configuration
sudo cp /usr/lib/firewalld/zones/public.xml /etc/firewalld/zones/
sudo firewall-cmd --reload
```

## Examples

```bash
$ sudo firewall-cmd --add-service=postgresql
Error: COMMAND_FAILED

$ ls /usr/lib/firewalld/services/ | grep postgres
# No output — service not defined

$ sudo firewall-cmd --add-port=5432/tcp
success

$ sudo firewall-cmd --permanent --add-port=5432/tcp
success
```

```bash
$ sudo firewall-cmd --zone=public --add-interface=eth0
Error: ZONE_CONFLICT

$ sudo firewall-cmd --get-active-zones
  internal
    interfaces: eth0

# Interface already assigned to 'internal' zone
$ sudo firewall-cmd --zone=internal --list-all
```

## Related Errors

- [iptables errors]({{< relref "/os/linux/iptables-error" >}}) — Underlying netfilter issues
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Service blocked by firewall
- [NetworkManager error]({{< relref "/os/linux/linux-network-manager" >}}) — Network connectivity issues

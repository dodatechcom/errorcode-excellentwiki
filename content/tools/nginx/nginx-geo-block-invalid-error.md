---
title: "[Solution] Nginx Geo Block Invalid Error"
description: "The geo block contains invalid IP addresses, overlapping CIDR ranges, or malformed syntax."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The geo block contains invalid IP addresses, overlapping CIDR ranges, or malformed syntax.

## Common Causes

- **Prefix length > 32** (IPv4) or > 128 (IPv6)
- **Invalid IP format**
- **Overlapping CIDR ranges**
- **Missing default**

## How to Fix

1. Use valid CIDR: `192.168.0.0/16`
2. Validate: `python3 -c "import ipaddress; print(ipaddress.ip_network('192.168.0.0/16'))"`
3. Ensure default set
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
geo $region { default 0; 192.168.1.1/33 1; }  # prefix > 32
```
**Valid:**
```nginx
geo $region { default 0; 192.168.0.0/16 1; 10.0.0.0/8 1; 172.16.0.0/12 1; }
```
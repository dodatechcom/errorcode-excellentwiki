---
title: "Netplan WiFi Country Code Error"
description: "WiFi connection fails due to incorrect or missing country code setting"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Netplan WiFi Country Code Error

WiFi connection fails due to incorrect or missing country code setting

## Common Causes

- Country code not set in Netplan config
- Country code not matching regulatory domain
- WiFi adapter does not support requested frequencies
- CRDA (Central Regulatory Domain Agent) not installed

## How to Fix

1. Set country code: `country-code: US` in wifi config
2. Check current: `iw reg get`
3. Set regulatory domain: `sudo iw reg set US`
4. Install CRDA: `sudo apt-get install crda`

## Examples

```yaml
# Netplan WiFi config with country code
network:
  version: 2
  wifis:
    wlan0:
      dhcp4: true
      access-points:
        "my-wifi":
          password: "mypass"
      country-code: US
```

---
title: "[Solution] macOS NSURLErrorCannotFindHost — Fix Host Resolution"
description: "Fix macOS NSURLErrorCannotFindHost (-1003) with these step-by-step solutions. Includes terminal commands and system settings."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime"]
weight: 308
---

# macOS NSURLErrorCannotFindHost — Fix Host Resolution

NSURLErrorCannotFindHost (-1003) means the system could not find the specified host, either through DNS or local resolution.

## Common Causes

1. Hostname does not exist in DNS records
2. Typo in the hostname
3. DNS server is not responding
4. Hosts file does not contain the required entry
5. Network prevents DNS queries

## How to Fix

### Fix 1: Verify Hostname Exists

```bash
# Check DNS records for the host
dig example.com A
dig example.com AAAA

# Check multiple record types
dig example.com ANY

# Verify the hostname resolves
host example.com
```

### Fix 2: Check DNS Configuration

```bash
# View current DNS servers
scutil --dns | grep "nameserver\["

# Test DNS resolution with specific server
dig @8.8.8.8 example.com

# Check for DNS configuration issues
networksetup -getdnsservers Wi-Fi
```

### Fix 3: Verify Network Connection

```bash
# Confirm network is active
ifconfig en0 | grep "inet "

# Test basic internet connectivity
ping -c 3 8.8.8.8

# Check if the host is reachable via IP
curl -I http://93.184.216.34 -H "Host: example.com"
```

## Related Errors

- [NSURLErrorDNSLookupFailed](/os/macos/nsurlerror-dns-failed/)
- [NSURLErrorNotConnectedToInternet](/os/macos/nsurlerror-not-connected/)
- [NSURLErrorCannotConnectToHost](/os/macos/nsurlerror-cannot-connect/)

---
title: "[Solution] macOS NSURLErrorDNSLookupFailed — Fix DNS Resolution"
description: "Fix macOS NSURLErrorDNSLookupFailed (-1006) with these step-by-step solutions. Includes terminal commands and system settings."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime"]
weight: 304
---

# macOS NSURLErrorDNSLookupFailed — Fix DNS Resolution

NSURLErrorDNSLookupFailed (-1006) occurs when the system cannot resolve a hostname to an IP address via DNS.

## Common Causes

1. DNS server is unreachable or not responding
2. Hostname does not exist or is misspelled
3. DNS cache contains stale or corrupted entries
4. DNS resolver configuration is incorrect
5. Network prevents DNS queries on port 53

## How to Fix

### Fix 1: Flush DNS Cache

```bash
# Flush DNS cache (macOS Ventura and later)
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

# Verify DNS cache is flushed
dscacheutil -q host -a name example.com
```

### Fix 2: Check and Configure DNS Resolvers

```bash
# View current DNS configuration
scutil --dns | grep nameserver

# Check network service DNS settings
networksetup -getdnsservers Wi-Fi

# Set custom DNS servers
sudo networksetup -setdnsservers Wi-Fi 8.8.8.8 8.8.4.4
```

### Fix 3: Verify Hostname Resolution

```bash
# Test DNS resolution
nslookup example.com

# Use dig for detailed DNS info
dig example.com ANY

# Check hosts file for overrides
cat /etc/hosts | grep example.com
```

## Related Errors

- [NSURLErrorCannotFindHost](/os/macos/nsurlerror-cannot-find-host/)
- [NSURLErrorNotConnectedToInternet](/os/macos/nsurlerror-not-connected/)
- [NSURLErrorCannotConnectToHost](/os/macos/nsurlerror-cannot-connect/)

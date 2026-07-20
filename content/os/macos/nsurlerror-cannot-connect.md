---
title: "[Solution] macOS NSURLErrorCannotConnectToHost — Fix Connection Failures"
description: "Fix macOS NSURLErrorCannotConnectToHost (-1004) with these step-by-step solutions. Includes terminal commands and system settings."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime"]
weight: 302
---

# macOS NSURLErrorCannotConnectToHost — Fix Connection Failures

NSURLErrorCannotConnectToHost (-1004) indicates that the app was unable to establish a connection to the specified host server.

## Common Causes

1. Hostname is incorrect or does not exist
2. Target port is closed or blocked
3. Firewall is blocking the outgoing connection
4. Server is down or not accepting connections
5. SSL/TLS handshake failure preventing connection

## How to Fix

### Fix 1: Verify Hostname and Port

```bash
# Resolve the hostname
nslookup example.com

# Check if the port is open
nc -zv example.com 443

# Verify the full URL is correct
curl -I https://example.com
```

### Fix 2: Check Firewall Settings

```bash
# Check macOS firewall status
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate

# List blocked applications
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --listapps

# Temporarily disable firewall for testing
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate off
```

### Fix 3: Verify Server Availability

```bash
# Test server reachability
traceroute example.com

# Check server headers
curl -I --connect-timeout 10 https://example.com

# Verify the server is responding
wget --spider https://example.com
```

## Related Errors

- [NSURLErrorTimedOut](/os/macos/nsurlerror-timedout/)
- [NSURLErrorDNSLookupFailed](/os/macos/nsurlerror-dns-failed/)
- [NSURLErrorServerCertificateUntrusted](/os/macos/nsurlerror-tls-error/)

---
title: "[Solution] macOS DNS Cache Error -- DNS Cache Corrupted or Stale"
description: "Fix macOS DNS cache error when DNS cache is corrupted or stale. Resolve DNS caching issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS DNS Cache Error -- DNS Cache Corrupted or Stale

DNS caching stores recently resolved domain names for faster access. When the cache is corrupted or stale, you may be directed to old IP addresses or experience DNS resolution failures.

## Common Causes
- DNS cache has stale entries pointing to old IP addresses
- DNS cache is corrupted from a network change
- mDNSResponder process has stale cache data
- Router DNS cache is also stale
- VPN or proxy left stale DNS entries

## How to Fix
1. Flush the local DNS cache
2. Restart the mDNSResponder daemon
3. Restart the router to clear its DNS cache
4. Change DNS servers to bypass cache
5. Wait for TTL expiry if flushing does not work

```bash
# Flush DNS cache
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

# Check DNS resolution
dig google.com
```

## Examples

```bash
# Test DNS resolution speed
time dig google.com

# Check current DNS servers
scutil --dns
```

This error is common after changing DNS servers, when a VPN disconnects leaving stale entries, or when the router's DNS cache is also stale.

---
title: "[Solution] macOS NTP Error -- Mac Time Is Incorrect or Not Syncing"
description: "Fix macOS NTP error when the Mac clock is incorrect or not syncing with time servers. Resolve time synchronization issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS NTP Error -- Mac Time Is Incorrect or Not Syncing

NTP (Network Time Protocol) keeps your Mac's clock accurate by syncing with Apple's time servers. When NTP fails, the system time may drift, causing certificate errors and authentication failures.

## Common Causes
- Network time sync is disabled
- Apple time server is unreachable
- Firewall is blocking NTP traffic (UDP port 123)
- System clock hardware is drifting
- VPN is interfering with time sync

## How to Fix
1. Enable automatic time synchronization
2. Sync the clock manually from terminal
3. Check network connectivity to Apple time servers
4. Ensure UDP port 123 is not blocked
5. Disable VPN temporarily to test time sync

```bash
# Sync time manually
sudo sntp -sS time.apple.com

# Check time sync status
systemsetup -getusingnetworktime

# Enable network time
systemsetup -setusingnetworktime on
```

## Examples

```bash
# Check current time
date

# Test NTP server connectivity
sntp -sS time.apple.com
```

This error is common when network time sync is disabled, when the Apple time server is unreachable, or when a VPN interferes with NTP traffic.

---
title: "[Solution] macOS NSURLErrorNetworkConnectionLost — Handle Network Drops"
description: "Fix macOS NSURLErrorNetworkConnectionLost (-1005) with these step-by-step solutions. Includes terminal commands and system settings."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime"]
weight: 303
---

# macOS NSURLErrorNetworkConnectionLost — Handle Network Drops

NSURLErrorNetworkConnectionLost (-1005) means the network connection was lost during data transfer, interrupting an active request.

## Common Causes

1. Unstable WiFi or cellular connection
2. Network switch or router issue
3. VPN connection dropping mid-transfer
4. Server closing the connection prematurely
5. Sleep/wake cycle interrupting network state

## How to Fix

### Fix 1: Check Network Stability

```bash
# Monitor connection stability
ping -i 0.5 -c 100 example.com

# Check WiFi signal strength
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I

# View network interface errors
netstat -I en0
```

### Fix 2: Implement Retry Logic

```swift
func fetchDataWithRetry(url: URL, retries: Int = 3) {
    let task = URLSession.shared.dataTask(with: url) { data, response, error in
        if let error = error as? URLError, error.code == .networkConnectionLost {
            if retries > 0 {
                fetchDataWithRetry(url: url, retries: retries - 1)
            }
        }
    }
    task.resume()
}
```

### Fix 3: Handle Reconnection

```bash
# Monitor network changes
sudo ifconfig en0 down && sudo ifconfig en0 up

# Reset network interface
sudo dscacheutil -flushcache && sudo killall -HUP mDNSResponder

# Check for network handoff issues
log show --predicate 'eventMessage contains "network"' --last 5m
```

## Related Errors

- [NSURLErrorTimedOut](/os/macos/nsurlerror-timedout/)
- [NSURLErrorNotConnectedToInternet](/os/macos/nsurlerror-not-connected/)
- [NSURLErrorCancelled](/os/macos/nsurlerror-cancelled/)

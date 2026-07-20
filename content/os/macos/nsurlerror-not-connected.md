---
title: "[Solution] macOS NSURLErrorNotConnectedToInternet — Fix Offline Errors"
description: "Fix macOS NSURLErrorNotConnectedToInternet (-1009) with these step-by-step solutions. Includes terminal commands and system settings."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime"]
weight: 305
---

# macOS NSURLErrorNotConnectedToInternet — Fix Offline Errors

NSURLErrorNotConnectedToInternet (-1009) indicates the device has no active network connection and cannot reach the internet.

## Common Causes

1. WiFi is turned off or not connected to a network
2. Ethernet cable is disconnected
3. Airplane mode is enabled
4. Network adapter is disabled
5. ISP or upstream network is down

## How to Fix

### Fix 1: Check Network Status

```bash
# Check network connectivity
ping -c 4 8.8.8.8

# Verify network interfaces
ifconfig -l

# Check WiFi status
networksetup -getairportnetwork en0
```

### Fix 2: Detect Connectivity Programmatically

```swift
import Network

let monitor = NWPathMonitor()
monitor.pathUpdateHandler = { path in
    if path.status == .satisfied {
        print("Connected to network")
    } else {
        print("No network connection")
    }
}
monitor.start(queue: DispatchQueue.global(qos: .background))
```

### Fix 3: Queue Requests for Offline

```swift
class RequestQueue {
    var pendingRequests: [(URLRequest, (Data?, URLResponse?, Error?) -> Void)] = []

    func enqueue(_ request: URLRequest, completion: @escaping (Data?, URLResponse?, Error?) -> Void) {
        pendingRequests.append((request, completion))
    }

    func processPendingRequests() {
        for (request, completion) in pendingRequests {
            URLSession.shared.dataTask(with: request, completionHandler: completion).resume()
        }
        pendingRequests.removeAll()
    }
}
```

## Related Errors

- [NSURLErrorNetworkConnectionLost](/os/macos/nsurlerror-network-lost/)
- [NSURLErrorTimedOut](/os/macos/nsurlerror-timedout/)
- [NSURLErrorDNSLookupFailed](/os/macos/nsurlerror-dns-failed/)

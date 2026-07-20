---
title: "[Solution] macOS NSURLErrorCancelled — Fix Cancelled Request Errors"
description: "Fix macOS NSURLErrorCancelled (-999) with these step-by-step solutions. Includes terminal commands and system settings."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime"]
weight: 310
---

# macOS NSURLErrorCancelled — Fix Cancelled Request Errors

NSURLErrorCancelled (-999) indicates the request was explicitly cancelled by the app or user before it could complete.

## Common Causes

1. Task was cancelled using `cancel()` before completion
2. View controller was deallocated while request was in progress
3. User navigated away triggering automatic cancellation
4. Duplicate request cancelled the previous one
5. App entered background cancelling active requests

## How to Fix

### Fix 1: Check Cancellation Logic

```swift
// Verify task is not cancelled before processing response
let task = session.dataTask(with: url) { data, response, error in
    if let error = error as? URLError, error.code == .cancelled {
        print("Request was cancelled")
        return
    }
    // Process data
}
task.resume()

// Only cancel intentionally
task.cancel()
```

### Fix 2: Handle Task States Properly

```swift
class NetworkManager {
    var activeTask: URLSessionDataTask?

    func fetchData(from url: URL) {
        activeTask?.cancel()
        activeTask = URLSession.shared.dataTask(with: url) { [weak self] data, response, error in
            guard let self = self else { return }
            if let error = error as? URLError, error.code == .cancelled {
                return
            }
            // Handle response
        }
        activeTask?.resume()
    }
}
```

### Fix 3: Debug Cancellation Sources

```bash
# Monitor network requests in Console.app
log show --predicate 'eventMessage contains "NSURLSession"' --last 5m

# Check for memory pressure causing cancellations
memory_pressure

# View system logs for request lifecycle
log show --predicate 'subsystem == "com.apple.network"' --last 10m
```

## Related Errors

- [NSURLErrorTimedOut](/os/macos/nsurlerror-timedout/)
- [NSURLErrorNetworkConnectionLost](/os/macos/nsurlerror-network-lost/)
- [NSURLErrorNotConnectedToInternet](/os/macos/nsurlerror-not-connected/)

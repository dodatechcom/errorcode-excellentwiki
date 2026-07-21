---
title: "[Solution] Network.framework NWBrowser Discovery Error"
description: "Fix Network framework NWBrowser service discovery failures."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Network.framework NWBrowser Discovery Error

NWBrowser fails to discover services when Bonjour services are not properly configured or when the browser parameters do not match the service type.

## Common Causes
- Service type string does not match published service
- Browser parameters incompatible with service protocol
- Network permissions not granted
- Service not published yet when browser starts

## How to Fix
1. Verify service type matches exactly (e.g., _myservice._tcp)
2. Use correct NWParameters for the protocol
3. Add Bonjour services entitlement
4. Start browser after service is published

```swift
// Discover Bonjour services:
let params = NWParameters()
params.includePeerToPeer = true

let browser = NWBrowser(for: .bonjour(type: "_myservice._tcp", domain: nil), using: params)
browser.stateUpdateHandler = { state in
    switch state {
    case .ready: print("Browsing")
case .failed(let error): print("Failed: \(error)")
default: break
    }
}
browser.browseResultsChangedHandler = { results, changes in
    for result in results {
        print("Found: \(result.endpoint)")
    }
}
browser.start(queue: .main)
```

## Examples
```swift
// Publish and browse:
let listener = try NWListener(using: NWParameters.tcp)
listener.service = NWListener.Service(type: "_myservice._tcp")
listener.stateUpdateHandler = { state in
    if case .ready = state {
        print("Published: \(String(describing: listener.service))")
    }
}
listener.start(queue: .main)
```

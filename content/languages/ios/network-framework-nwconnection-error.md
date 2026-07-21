---
title: "[Solution] Network Framework NWConnection Error"
description: "Fix Network framework NWConnection errors for modern networking in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Network Framework NWConnection Error

NWConnection errors occur when the connection fails to establish, times out, or encounters protocol-specific issues during data transfer.

## Common Causes
- Connection parameters configured incorrectly
- Network path unavailable
- Connection timeout too short
- Protocol not supported by the endpoint

## How to Fix
1. Verify connection parameters and endpoint
2. Handle connection state changes
3. Set appropriate timeout values
4. Implement retry logic for transient failures

```swift
let connection = NWConnection(host: "example.com", port: 443, using: .tls)
connection.stateUpdateHandler = { state in
    switch state {
    case .ready: print("Connected")
    case .failed(let error): print("Failed: \(error)")
    case .waiting(let error): print("Waiting: \(error)")
    default: break
    }
}
connection.start(queue: .global())
```

## Examples
```swift
// NWConnection with error handling:
func connect(host: String, port: UInt16) {
    let parameters = NWParameters.tls
    let endpoint = NWEndpoint.Host(host)
    let conn = NWConnection(host: endpoint, port: NWEndpoint.Port(rawValue: port)!, using: parameters)

    conn.stateUpdateHandler = { [weak conn] state in
        switch state {
        case .ready:
            self.receive(on: conn!)
        case .failed(let error):
            print("Connection failed: \(error)")
            conn?.cancel()
        case .waiting(let error):
            print("Waiting: \(error)")
        default: break
        }
    }
    conn.start(queue: .main)
}
```

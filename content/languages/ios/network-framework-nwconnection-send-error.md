---
title: "[Solution] Network.framework NWConnection Send Error"
description: "Fix Network framework NWConnection send and receive data transfer errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Network.framework NWConnection Send Error

Send errors occur when the connection is not in ready state, when content is too large, or when the connection has been invalidated.

## Common Causes
- Connection not in .ready state when sending
- Data too large for single send operation
- Connection cancelled or failed
- Send completion not handled

## How to Fix
1. Verify connection state is .ready before sending
2. Split large data into smaller chunks
3. Check for connection errors before send
4. Handle send completion in content completion

```swift
// Safe send operation:
func send(data: Data, on connection: NWConnection) {
    guard connection.state == .ready else { return }
    connection.send(content: data, completion: .contentProcessed { error in
        if let error = error {
            print("Send failed: \(error)")
        }
    })
}
```

## Examples
```swift
// Complete send/receive cycle:
func sendAndReceive(data: Data, on connection: NWConnection) {
    connection.send(content: data, completion: .contentProcessed { error in
        if error != nil { return }
        connection.receive(minimumIncompleteLength: 1, maximumLength: 65536) { content, _, _, error in
            if let data = content {
                print("Received: \(data.count) bytes")
            }
        }
    })
}
```

---
title: "[Solution] Swift URLSession WebSocket Error — Send/Receive/Close"
description: "Fix Swift URLSessionWebSocket errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 130
---

URLSessionWebSocket errors occur when send/receive operations fail, close codes are invalid, or ping/pong handling is missing.

## Common Causes

```swift
// Not handling receive in loop
let task = URLSessionWebSocketTask(request: request)
task.resume()

// Missing: receive loop

// Invalid close code
task.cancel(with: .goingAway, reason: nil)
```

## How to Fix

**1. Create and manage WebSocket task**

```swift
let url = URL(string: "wss://example.com/socket")!
let task = URLSession.shared.webSocketTask(with: url)
task.resume()

func send(_ message: String) {
    let wsMessage = URLSessionWebSocketTask.Message.string(message)
    task.send(wsMessage) { error in
        if let error = error {
            print("Send failed: \(error)")
        }
    }
}
```

**2. Receive loop**

```swift
func receiveMessages() {
    task.receive { result in
        switch result {
        case .success(let message):
            switch message {
            case .string(let text):
                print("Received: \(text)")
            case .data(let data):
                print("Received data: \(data.count) bytes")
            @unknown default:
                break
            }
            self.receiveMessages() // Loop
        case .failure(let error):
            print("Receive error: \(error)")
        }
    }
}
```

**3. Handle close properly**

```swift
func disconnect() {
    let reason = "Closing connection".data(using: .utf8)
    task.cancel(with: .goingAway, reason: reason)
}
```

**4. Ping/pong handling**

```swift
func sendPing() {
    task.sendPing { error in
        if let error = error {
            print("Ping failed: \(error)")
        } else {
            print("Pong received")
        }
    }
}

// Periodic ping
Timer.scheduledTimer(withTimeInterval: 30, repeats: true) { _ in
    self.sendPing()
}
```

**5. URLSession delegate for WebSocket**

```swift
class WebSocketDelegate: NSObject, URLSessionWebSocketDelegate {
    func urlSession(_ session: URLSession, webSocketTask: URLSessionWebSocketTask,
                    didOpenWithProtocol protocol: String?) {
        print("WebSocket connected")
    }
    
    func urlSession(_ session: URLSession, webSocketTask: URLSessionWebSocketTask,
                    didCloseWith closeCode: URLSessionWebSocketTask.CloseCode, reason: Data?) {
        print("WebSocket closed: \(closeCode.rawValue)")
    }
}
```

## Examples

Complete WebSocket client:
```swift
class WebSocketClient {
    private var task: URLSessionWebSocketTask?
    private var delegate: WebSocketDelegate?
    
    func connect(to url: URL) {
        delegate = WebSocketDelegate()
        let session = URLSession(
            configuration: .default,
            delegate: delegate,
            delegateQueue: nil
        )
        task = session.webSocketTask(with: url)
        task?.resume()
        receiveMessages()
    }
    
    func send(_ text: String) async throws {
        try await task?.send(.string(text))
    }
    
    func receive() async throws -> String? {
        let message = try await task?.receive()
        if case .string(let text) = message {
            return text
        }
        return nil
    }
    
    func disconnect() {
        task?.cancel(with: .goingAway, reason: nil)
    }
}
```

## Related Errors

- [URLSession Background Error](/languages/swift/swift-urlsession-background)
- [URLSession Upload Error](/languages/swift/swift-urlsession-upload)
- [Alamofire Error](/languages/swift/swift-alamofire-error)

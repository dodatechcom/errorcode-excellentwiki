---
title: "[Solution] SwiftUI .onDisappear Cleanup Error"
description: "Fix SwiftUI .onDisappear view cleanup and resource release errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .onDisappear Cleanup Error

onDisappear errors occur when resources are not properly cleaned up, when the cleanup conflicts with the view lifecycle, or when the cleanup does not release all resources.

## Common Causes
- Resources not cleaned up
- Cleanup conflicts with lifecycle
- Cleanup does not release resources
- Cleanup not called

## How to Fix
1. Clean up resources properly
2. Ensure cleanup is compatible with lifecycle
3. Release all resources
4. Ensure cleanup is called

```swift
struct ContentView: View {
    @State private var timer: Timer?

    var body: some View {
        Text("Hello")
            .onAppear {
                timer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { _ in
                    // Update
                }
            }
            .onDisappear {
                timer?.invalidate()
            }
    }
}
```

## Examples
```swift
// Cancel async tasks:
.onDisappear {
    task?.cancel()
}

// Remove notifications:
.onDisappear {
    NotificationCenter.default.removeObserver(self)
}

// Close connections:
.onDisappear {
    webSocket.close()
}
```

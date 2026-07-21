---
title: "[Solution] Swift Compiler Error: Enum Case Not Handled in Switch"
description: "Fix exhaustive switch statement errors for enums in Swift."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Enum Case Not Handled in Switch

Swift switch statements on enums must handle all cases unless a default case is provided. Missing cases cause a compiler error.

## Common Causes
- New enum case added without updating switch statements
- Default case missing for non-exhaustive enums
- Case added in an extension not visible to the switch
- Indirect cases not properly handled

## How to Fix
1. Add cases for all enum values in the switch
2. Add a default case for future-proofing
3. Use @unknown default for C enums that may gain cases
4. Handle each case explicitly for clarity

```swift
// WRONG: Not all cases handled
enum Direction {
    case north, south, east, west
}

let dir: Direction = .north
switch dir {
case .north: print("North")
case .south: print("South")
// Missing east and west
}

// RIGHT: Handle all cases
switch dir {
case .north: print("North")
case .south: print("South")
case .east: print("East")
case .west: print("West")
}
```

## Examples
```swift
// Example: Proper switch handling
enum ConnectionState {
    case connected, disconnected, connecting, error(Error)
}

func handleState(_ state: ConnectionState) {
    switch state {
    case .connected:
        print("Connected")
    case .disconnected:
        print("Disconnected")
    case .connecting:
        print("Connecting...")
    case .error(let error):
        print("Error: \(error.localizedDescription)")
    }
}

// For future-proofing with @unknown default:
switch state {
case .connected: print("Connected")
case .disconnected: print("Disconnected")
case .connecting: print("Connecting")
case .error: print("Error")
@unknown default: print("Unknown state")
}
```

---
title: "[Solution] Swift Error — ProcessInfo Error"
description: "Fix Swift ProcessInfo errors. Learn about ProcessInfo property access, environment variable issues, and operating system version checks."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ProcessInfo Error

`ProcessInfo` errors occur when accessing system information, environment variables, command-line arguments, or operating system version details that are unavailable or restricted.

## Description

`ProcessInfo` provides access to the current process's environment, arguments, and system information. While most properties are safe to access, some operations can fail or return unexpected values, especially in sandboxed apps, test environments, or when system restrictions apply.

Common patterns:

- **Missing environment variables** — accessing unset environment keys.
- **OS version checks** — incorrect version comparisons.
- **Argument parsing** — accessing arguments that don't exist.
- **Thermal state** — monitoring device thermal state changes.

## Common Causes

```swift
// Cause 1: Force-unwrapping environment variable
let apiKey = ProcessInfo.processInfo.environment["API_KEY"]!
// Crashes if API_KEY is not set

// Cause 2: Wrong OS version check
if ProcessInfo.processInfo.isOperatingSystemAtLeast(OperatingSystemVersion(majorVersion: 17, minorVersion: 0, patchVersion: 0)) {
    // May not work as expected if version format is wrong
}

// Cause 3: Argument parsing without bounds checking
let args = ProcessInfo.processInfo.arguments
let configFile = args[1] // Index out of range if no arguments

// Cause 4: Thermal state not checked
func heavyComputation() {
    // Not checking thermalState before CPU-intensive work
    // May cause thermal throttling
}
```

## How to Fix

### Fix 1: Safely access environment variables

```swift
let env = ProcessInfo.processInfo.environment

// Wrong
let apiKey = env["API_KEY"]!

// Correct
if let apiKey = env["API_KEY"] {
    print("API Key: \(apiKey)")
} else {
    print("API_KEY not set in environment")
}
```

### Fix 2: Check OS version properly

```swift
// Correct — check major version
if ProcessInfo.processInfo.isOperatingSystemAtLeast(OperatingSystemVersion(majorVersion: 16, minorVersion: 0, patchVersion: 0)) {
    // iOS 16+ features
}

// For Swift version checks
if #available(iOS 16.0, macOS 13.0, *) {
    // Use newer API
}
```

### Fix 3: Safe argument parsing

```swift
let args = ProcessInfo.processInfo.arguments

// Wrong
let configPath = args[1]

// Correct
guard args.count > 1 else {
    print("Usage: app <config_path>")
    exit(1)
}
let configPath = args[1]
```

### Fix 4: Monitor thermal state

```swift
import Foundation

class ThermalMonitor {
    func startMonitoring() {
        NotificationCenter.default.addObserver(
            self,
            selector: #selector(thermalStateChanged),
            name: ProcessInfo.thermalStateDidChangeNotification,
            object: nil
        )
    }

    @objc func thermalStateChanged() {
        switch ProcessInfo.processInfo.thermalState {
        case .nominal:
            print("Thermal state: nominal")
        case .fair:
            print("Thermal state: fair - reduce CPU usage")
        case .serious:
            print("Thermal state: serious - minimize processing")
        case .critical:
            print("Thermal state: critical - stop heavy computation")
        @unknown default:
            break
        }
    }
}
```

## Examples

```swift
// Example 1: Environment variable not set in Xcode
// If you forget to add API_KEY to scheme environment variables
let key = ProcessInfo.processInfo.environment["API_KEY"] // nil

// Example 2: Wrong argument index
let args = ProcessInfo.processInfo.arguments
// args = ["MyApp"] — no additional arguments
let flag = args[1] // Fatal error: index out of range
```

## Related Errors

- [Index Out of Range]({{< relref "/languages/swift/index-out-of-range" >}}) — array index errors.
- [File Not Found]({{< relref "/languages/swift/file-not-found" >}}) — missing configuration files.
- [Arithmetic Overflow]({{< relref "/languages/swift/overflow" >}}) — version comparison issues.

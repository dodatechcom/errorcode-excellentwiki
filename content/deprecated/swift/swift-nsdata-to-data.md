---
title: "[Solution] Deprecated Function Migration: NSData to Data"
description: "Migrate from deprecated NSData to Data in Swift."
deprecated_function: "NSData(contentsOf: url)"
replacement_function: "Data(contentsOf: url)"
languages: ["swift"]
deprecated_since: "Swift 3.0+"
---

# [Solution] Deprecated Function Migration: NSData to Data

The `NSData(contentsOf: url)` has been deprecated in favor of `Data(contentsOf: url)`.

## Migration Guide

Data is the Swift value type

NSData is the Objective-C class. Data is the Swift value type.

## Before (Deprecated)

```swift
let data = NSData(contentsOf: url)
let bytes = data?.bytes.bindMemory(to: UInt8.self, count: data!.length)
```

## After (Modern)

```swift
let data = try Data(contentsOf: url)
let bytes = [UInt8](data)
```

## Key Differences

- Data is a Swift struct
- NSData is Objective-C class
- Direct conversion to [UInt8]
- Better memory management

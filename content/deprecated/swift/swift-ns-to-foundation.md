---
title: "[Solution] Deprecated Function Migration: NSString to Swift String"
description: "Migrate from deprecated NSString/NSArray/NSDictionary to Swift native types."
deprecated_function: "NSString / NSArray / NSDictionary"
replacement_function: "String / Array / Dictionary"
languages: ["swift"]
deprecated_since: "Swift 1.0+"
---

# [Solution] Deprecated Function Migration: NSString to Swift String

The `NSString / NSArray / NSDictionary` has been deprecated in favor of `String / Array / Dictionary`.

## Migration Guide

Swift native types are value types with better API. Foundation types are reference types bridged from Objective-C.

## Before (Deprecated)

```swift
let nsString: NSString = "Hello, World!"
let length = nsString.length

let nsArray: NSArray = ["a", "b", "c"]
let count = nsArray.count
```

## After (Modern)

```swift
let string: String = "Hello, World!"
let length = string.count

let array: [String] = ["a", "b", "c"]
let count = array.count
let first = array[0]
```

## Key Differences

- Swift types are value types (structs)
- Foundation types are reference types
- Better language integration
- Automatic bridging between types

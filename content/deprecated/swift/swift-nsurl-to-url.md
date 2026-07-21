---
title: "[Solution] Deprecated Function Migration: NSURL to URL"
description: "Migrate from deprecated NSURL to URL in Swift."
deprecated_function: "NSURL(string: url)"
replacement_function: "URL(string: url)"
languages: ["swift"]
deprecated_since: "Swift 3.0+"
---

# [Solution] Deprecated Function Migration: NSURL to URL

The `NSURL(string: url)` has been deprecated in favor of `URL(string: url)`.

## Migration Guide

URL is the Swift struct

NSURL is the Objective-C class. URL is the Swift value type.

## Before (Deprecated)

```swift
let url = NSURL(string: "https://example.com")
let request = URLRequest(url: url! as URL)
```

## After (Modern)

```swift
let url = URL(string: "https://example.com")
let request = URLRequest(url: url!)

// Safer with optional binding
if let url = URL(string: "https://example.com") {
    let request = URLRequest(url: url)
}
```

## Key Differences

- URL is a Swift struct (value type)
- NSURL is an Objective-C class
- Use optional binding for safety
- Better Swift integration

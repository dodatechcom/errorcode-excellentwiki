---
title: "[Solution] Deprecated Function Migration: NSURLRequest to URLRequest"
description: "Migrate from deprecated NSURLRequest to URLRequest."
deprecated_function: "NSURLRequest(url: url)"
replacement_function: "URLRequest(url: url)"
languages: ["swift"]
deprecated_since: "Swift 3.0+"
---

# [Solution] Deprecated Function Migration: NSURLRequest to URLRequest

The `NSURLRequest(url: url)` has been deprecated in favor of `URLRequest(url: url)`.

## Migration Guide

URLRequest is the Swift value type

NSURLRequest is Objective-C.

## Before (Deprecated)

```swift
let request = NSURLRequest(url: url!)
```

## After (Modern)

```swift
var request = URLRequest(url: url)
request.httpMethod = "POST"
```

## Key Differences

- URLRequest is a Swift struct
- Follows Swift naming conventions

---
title: "[Solution] Deprecated Function Migration: NSURLSession to URLSession"
description: "Migrate from deprecated NSURLSession to URLSession in Swift."
deprecated_function: "NSURLSession.shared"
replacement_function: "URLSession.shared"
languages: ["swift"]
deprecated_since: "Swift 3.0+"
---

# [Solution] Deprecated Function Migration: NSURLSession to URLSession

The `NSURLSession.shared` has been deprecated in favor of `URLSession.shared`.

## Migration Guide

URLSession follows Swift naming conventions

NSURLSession is the Objective-C name. URLSession is the Swift name.

## Before (Deprecated)

```swift
let session = URLSession.shared
let task = session.dataTask(with: url) { data, response, error in
    // handle
}
```

## After (Modern)

```swift
let session = URLSession.shared
let task = session.dataTask(with: url) { data, response, error in
    // handle
}
task.resume()
```

## Key Differences

- URLSession is the Swift name
- Same functionality
- Follows Swift naming conventions
- Automatic bridging from Objective-C

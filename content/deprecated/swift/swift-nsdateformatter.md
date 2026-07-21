---
title: "[Solution] Deprecated Function Migration: NSDateFormatter to DateFormatter"
description: "Migrate from deprecated NSDateFormatter to DateFormatter."
deprecated_function: "NSDateFormatter()"
replacement_function: "DateFormatter()"
languages: ["swift"]
deprecated_since: "Swift 3.0+"
---

# [Solution] Deprecated Function Migration: NSDateFormatter to DateFormatter

The `NSDateFormatter()` has been deprecated in favor of `DateFormatter()`.

## Migration Guide

DateFormatter follows Swift naming conventions

NSDateFormatter is the Objective-C class. DateFormatter is the Swift name.

## Before (Deprecated)

```swift
let formatter = NSDateFormatter()
formatter.dateFormat = "yyyy-MM-dd"
let string = formatter.stringFromDate(date)
```

## After (Modern)

```swift
let formatter = DateFormatter()
formatter.dateFormat = "yyyy-MM-dd"
let string = formatter.string(from: date)

// Or use ISO8601DateFormatter (iOS 10+)
let isoFormatter = ISO8601DateFormatter()
let isoString = isoFormatter.string(from: date)
```

## Key Differences

- DateFormatter is the Swift name
- ISO8601DateFormatter for ISO 8601
- Same functionality
- Follows Swift naming conventions

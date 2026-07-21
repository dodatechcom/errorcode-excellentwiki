---
title: "[Solution] Deprecated Function Migration: URLSessionDownloadDelegate to async/await"
description: "Migrate from deprecated URLSessionDownloadDelegate to async/await."
deprecated_function: "URLSessionDownloadDelegate"
replacement_function: "(url, response) = try await session.download(from:)"
languages: ["swift"]
deprecated_since: "iOS 15+"
---

# [Solution] Deprecated Function Migration: URLSessionDownloadDelegate to async/await

The `URLSessionDownloadDelegate` has been deprecated in favor of `(url, response) = try await session.download(from:)`.

## Migration Guide

async/await is cleaner.

## Before (Deprecated)

```swift
func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didFinishDownloadingTo location: URL) { }
```

## After (Modern)

```swift
let (url, _) = try await session.download(from: myURL)
```

## Key Differences

- async/await is cleaner

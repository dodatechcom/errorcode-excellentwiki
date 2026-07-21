---
title: "[Solution] Background URL Session Completion Handler Error"
description: "Fix background URLSession completion handler not being called in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Background URL Session Completion Handler Error

The completion handler for background URL sessions must be called exactly once. Failing to call it causes the app to be suspended and the download to fail.

## Common Causes
- Completion handler not called in handleEventsForBackgroundURLSession
- Multiple calls to the same completion handler
- App terminated before completion handler called
- Session configuration not set to background

## How to Fix
1. Store the completion handler and call it when downloads finish
2. Call the completion handler only once
3. Handle all delegate methods for background sessions
4. Verify the session configuration uses a background identifier

```swift
// In AppDelegate or SceneDelegate:
func application(_ application: UIApplication, handleEventsForBackgroundURLSession completionHandler: @escaping () -> Void) {
    // Store the handler
    backgroundCompletionHandler = completionHandler
}

// In URLSession delegate:
func urlSessionDidFinishEvents(for session: URLSession) {
    backgroundCompletionHandler?()
    backgroundCompletionHandler = nil
}
```

## Examples
```swift
// Background download manager:
class BackgroundDownloadManager: NSObject, URLSessionDownloadDelegate {
    var backgroundCompletionHandler: (() -> Void)?
    private lazy var session: URLSession = {
        let config = URLSessionConfiguration.background(withIdentifier: "com.app.download")
        return URLSession(configuration: config, delegate: self, delegateQueue: nil)
    }()

    func urlSessionDidFinishEvents(for session: URLSession) {
        backgroundCompletionHandler?()
        backgroundCompletionHandler = nil
    }
}
```

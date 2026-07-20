---
title: "[Solution] Swift URLSession Background Configuration Error"
description: "Fix Swift URLSession background configuration errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 132
---

URLSession background configuration errors occur when background sessions aren't properly configured, completion handlers are missing, or task identifiers are mismanaged.

## Common Causes

```swift
// Using foreground session for background work
let session = URLSession.shared // Not background-capable

// Missing background session identifier
let config = URLSessionConfiguration.background(withIdentifier: nil) // Crash
```

## How to Fix

**1. Create background session**

```swift
let config = URLSessionConfiguration.background(withIdentifier: "com.app.download")
config.isDiscretionary = true
config.sessionSendsLaunchEvents = true

let session = URLSession(configuration: config, delegate: self, delegateQueue: nil)
```

**2. Handle background events in AppDelegate**

```swift
func application(_ application: UIApplication,
                 handleEventsForBackgroundURLSession identifier: String,
                 completionHandler: @escaping () -> Void) {
    self.backgroundCompletionHandler = completionHandler
}
```

**3. URLSession delegate callbacks**

```swift
extension AppDelegate: URLSessionDelegate, URLSessionDownloadDelegate {
    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask,
                    didFinishDownloadingTo location: URL) {
        // Move file from temporary location
        let destURL = documentsURL.appendingPathComponent(downloadTask.originalRequest?.url?.lastPathComponent ?? "")
        try? FileManager.default.moveItem(at: location, to: destURL)
    }
    
    func urlSessionDidFinishEvents(forBackground session: URLSession) {
        backgroundCompletionHandler?()
        backgroundCompletionHandler = nil
    }
}
```

**4. Background download task**

```swift
func startDownload(url: URL) {
    let task = session.downloadTask(with: url)
    task.resume()
}
```

**5. Resume background transfer**

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Handle background download completion
    if let identifier = launchOptions?[.backgroundFetchIdentifier] as? String {
        let config = URLSessionConfiguration.background(withIdentifier: identifier)
        let _ = URLSession(configuration: config, delegate: self, delegateQueue: nil)
    }
    return true
}
```

## Examples

Complete background download manager:
```swift
class BackgroundDownloadManager: NSObject {
    static let shared = BackgroundDownloadManager()
    private var session: URLSession!
    private var completion: ((URL) -> Void)?
    
    func startDownload(url: URL, completion: @escaping (URL) -> Void) {
        self.completion = completion
        let config = URLSessionConfiguration.background(withIdentifier: "download.\(UUID().uuidString)")
        config.isDiscretionary = true
        session = URLSession(configuration: config, delegate: self, delegateQueue: nil)
        
        let task = session.downloadTask(with: url)
        task.resume()
    }
}

extension BackgroundDownloadManager: URLSessionDownloadDelegate {
    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask,
                    didFinishDownloadingTo location: URL) {
        let destURL = FileManager.default.temporaryDirectory
            .appendingPathComponent(downloadTask.originalRequest?.url?.lastPathComponent ?? "")
        try? FileManager.default.moveItem(at: location, to: destURL)
        completion?(destURL)
    }
    
    func urlSessionDidFinishEvents(forBackground session: URLSession) {}
}
```

## Related Errors

- [URLSession Upload Error](/languages/swift/swift-urlsession-upload)
- [WebSocket Error](/languages/swift/swift-websocket-error)
- [Alamofire Error](/languages/swift/swift-alamofire-error)

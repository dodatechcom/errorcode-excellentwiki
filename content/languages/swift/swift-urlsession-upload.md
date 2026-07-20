---
title: "[Solution] Swift URLSession Upload Task Error"
description: "Fix Swift URLSession upload task errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 133
---

URLSession upload task errors occur when streamed bodies are misconfigured, HTTP body streams fail, or upload completion isn't handled.

## Common Causes

```swift
// Wrong upload method for large data
let task = session.uploadTask(with: request, from: largeData) // Memory issue

// Missing stream for large uploads
let task = session.uploadTask(withStreamedRequest: request)
// No delegate to provide body stream
```

## How to Fix

**1. Simple upload**

```swift
let url = URL(string: "https://api.example.com/upload")!
var request = URLRequest(url: url)
request.httpMethod = "POST"

let task = session.uploadTask(with: request, from: fileData) { data, response, error in
    if let error = error {
        print("Upload failed: \(error)")
        return
    }
    print("Upload complete")
}
task.resume()
```

**2. Streamed upload for large files**

```swift
let task = session.uploadTask(withStreamedRequest: request)
task.resume()

func urlSession(_ session: URLSession, task: URLSessionTask,
                needNewBodyStream completionHandler: @escaping (InputStream?) -> Void) {
    let stream = InputStream(url: largeFileURL)
    completionHandler(stream)
}
```

**3. Upload with progress**

```swift
let task = session.uploadTask(with: request, from: fileData) { data, response, error in
    // Handle completion
}

// Observe progress
let observation = task.progress.observe(\.fractionCompleted) { progress, _ in
    print("Upload progress: \(progress.fractionCompleted)")
}
```

**4. Multipart form data upload**

```swift
func uploadImage(_ image: UIImage, to url: URL) {
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    
    let boundary = UUID().uuidString
    request.setValue("multipart/form-data; boundary=\(boundary)", forHTTPHeaderField: "Content-Type")
    
    var body = Data()
    body.append("--\(boundary)\r\n".data(using: .utf8)!)
    body.append("Content-Disposition: form-data; name=\"file\"; filename=\"image.jpg\"\r\n".data(using: .utf8)!)
    body.append("Content-Type: image/jpeg\r\n\r\n".data(using: .utf8)!)
    body.append(image.jpegData(compressionQuality: 0.8)!)
    body.append("\r\n--\(boundary)--\r\n".data(using: .utf8)!)
    
    let task = session.uploadTask(with: request, from: body) { data, response, error in
        // Handle response
    }
    task.resume()
}
```

**5. Background upload**

```swift
let task = session.uploadTask(with: request, fromFile: fileURL)
task.resume()
```

## Examples

Complete upload manager:
```swift
class UploadManager {
    func upload(file: URL, to endpoint: URL) async throws -> Data {
        var request = URLRequest(url: endpoint)
        request.httpMethod = "POST"
        
        let data = try Data(contentsOf: file)
        let (responseData, response) = try await URLSession.shared.upload(for: request, from: data)
        
        guard let httpResponse = response as? HTTPURLResponse,
              200..<300 ~= httpResponse.statusCode else {
            throw UploadError.serverError
        }
        
        return responseData
    }
}

enum UploadError: Error {
    case serverError
    case invalidData
}
```

## Related Errors

- [URLSession Background Error](/languages/swift/swift-urlsession-background)
- [WebSocket Error](/languages/swift/swift-websocket-error)
- [Alamofire Error](/languages/swift/swift-alamofire-error)

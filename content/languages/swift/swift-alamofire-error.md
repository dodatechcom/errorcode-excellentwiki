---
title: "[Solution] Swift Alamofire Error — Request Validation & AFError"
description: "Fix Swift Alamofire errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 131
---

Alamofire errors occur when request validation fails, response decoding encounters issues, or AFError isn't handled properly.

## Common Causes

```swift
// Missing error handling
AF.request("https://api.example.com/data").responseJSON { response in
    // Not checking response.result
}

// Decoding failure
AF.request(url).responseDecodable(of: Model.self) { response in
    // Not handling .failure
}
```

## How to Fix

**1. Handle response result**

```swift
AF.request("https://api.example.com/data").responseJSON { response in
    switch response.result {
    case .success(let value):
        print("Success: \(value)")
    case .failure(let error):
        print("Error: \(error)")
    }
}
```

**2. Decode response**

```swift
AF.request(url).responseDecodable(of: Model.self) { response in
    switch response.result {
    case .success(let model):
        self.updateUI(with: model)
    case .failure(let error):
        self.handleError(error)
    }
}
```

**3. Handle AFError**

```swift
func handleError(_ error: AFError) {
    switch error {
    case .invalidURL(let url):
        print("Invalid URL: \(url)")
    case .responseValidationFailed(let reason):
        print("Validation failed: \(reason)")
    case .responseSerializationFailed(let reason):
        print("Serialization failed: \(reason)")
    default:
        print("Other error: \(error)")
    }
}
```

**4. Request validation**

```swift
AF.request(url)
    .validate(statusCode: 200..<300)
    .validate(contentType: ["application/json"])
    .responseDecodable(of: Model.self) { response in
        // Handle response
    }
```

**5. Custom headers and parameters**

```swift
let headers: HTTPHeaders = [
    "Authorization": "Bearer \(token)",
    "Content-Type": "application/json"
]

AF.request(url,
           method: .post,
           parameters: params,
           encoder: JSONParameterEncoder.default,
           headers: headers)
    .responseDecodable(of: Response.self) { response in
        // Handle response
    }
```

## Examples

Complete Alamofire setup:
```swift
class APIClient {
    static let shared = APIClient()
    
    private let session: Session
    
    private init() {
        let config = URLSessionConfiguration.default
        config.timeoutIntervalForRequest = 30
        session = Session(configuration: config)
    }
    
    func fetch<T: Decodable>(_ endpoint: String) async throws -> T {
        try await withCheckedThrowingContinuation { continuation in
            session.request(endpoint)
                .validate()
                .responseDecodable(of: T.self) { response in
                    switch response.result {
                    case .success(let value):
                        continuation.resume(returning: value)
                    case .failure(let error):
                        continuation.resume(throwing: error)
                    }
                }
        }
    }
}
```

## Related Errors

- [URLSession Background Error](/languages/swift/swift-urlsession-background)
- [URLSession Upload Error](/languages/swift/swift-urlsession-upload)
- [WebSocket Error](/languages/swift/swift-websocket-error)

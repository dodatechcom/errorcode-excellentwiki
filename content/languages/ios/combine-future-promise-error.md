---
title: "[Solution] Combine Future Promise Error"
description: "Fix Combine Future and promise callback errors in asynchronous Combine pipelines."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Combine Future Promise Error

Future promise callbacks fail when the promise is not called, when it is called more than once, or when errors are not properly passed through the promise.

## Common Causes
- Promise not called in async completion
- Promise called multiple times
- Error not passed to promise
- Promise called after Future is deallocated

## How to Fix
1. Ensure promise is called exactly once
2. Pass .finished in completion on success
3. Pass .failure(error) on error
4. Handle both success and failure paths

```swift
let future = Future<String, Error> { promise in
    asyncOperation { result in
        switch result {
        case .success(let value):
            promise(.success(value))
        case .failure(let error):
            promise(.failure(error))
        }
    }
}

future
    .sink { completion in
        if case .failure(let error) = completion {
            print("Error: \(error)")
        }
    } receiveValue: { value in
        print("Value: \(value)")
    }
```

## Examples
```swift
// Future with network request:
func fetchUser(id: Int) -> Future<User, Error> {
    return Future { promise in
        let url = URL(string: "https://api.example.com/users/\(id)")!
        URLSession.shared.dataTask(with: url) { data, response, error in
            if let error = error {
                promise(.failure(error))
                return
            }
            guard let data = data,
                  let user = try? JSONDecoder().decode(User.self, from: data) else {
                promise(.failure(NSError(domain: "", code: -1)))
                return
            }
            promise(.success(user))
        }.resume()
    }
}
```

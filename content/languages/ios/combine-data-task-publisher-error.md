---
title: "[Solution] Combine Data Task Publisher Error"
description: "Fix URLSession.dataTaskPublisher errors and response handling in Combine."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Combine Data Task Publisher Error

DataTaskPublisher errors occur when the response is not an HTTPURLResponse, when status codes are not in the 200 range, or when data is nil.

## Common Causes
- Response cast to HTTPURLResponse fails
- Status code outside 200-299 range
- Network connectivity lost during request
- Publisher cancelled before completion

## How to Fix
1. Cast response to HTTPURLResponse
2. Check status code in the pipeline
3. Use tryMap for error handling
4. Handle cancellation in sink/receive

```swift
// DataTaskPublisher with error handling:
URLSession.shared.dataTaskPublisher(for: url)
    .tryMap { data, response in
        guard let httpResponse = response as? HTTPURLResponse,
              (200...299).contains(httpResponse.statusCode) else {
            throw URLError(.badServerResponse)
        }
        return data
    }
    .decode(type: MyModel.self, decoder: JSONDecoder())
    .receive(on: DispatchQueue.main)
    .sink { completion in
        if case .failure(let error) = completion {
            print("Error: \(error)")
        }
    } receiveValue: { model in
        print("Received: \(model)")
    }
    .store(in: &cancellables)
```

## Examples
```swift
// Full network pipeline:
func fetchUser(id: Int) -> AnyPublisher<User, Error> {
    let url = URL(string: "https://api.example.com/users/\(id)")!
    return URLSession.shared.dataTaskPublisher(for: url)
        .tryMap { data, response in
            guard let http = response as? HTTPURLResponse, http.statusCode == 200 else {
                throw APIError.invalidResponse
            }
            return data
        }
        .decode(type: User.self, decoder: JSONDecoder())
        .eraseToAnyPublisher()
}
```

---
title: "[Solution] Combine.Publisher error: Subscribe from non-main thread"
description: "Fix Combine publisher subscription threading errors. Learn why subscribing to Combine publishers off the main thread causes crashes and how to fix it."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "swift"
tags: ["swift", "combine", "publisher", "threading", "main-thread"]
severity: "error"
---

# Combine.Publisher error: Subscribe from non-main thread

## Error Message

```
Combine: subscribing to publisher from non-main thread while updating UI. Publishing changes from background threads is not allowed, make sure to subscribe on the main thread.
```

## Common Causes

- Subscribing to a Combine publisher inside a background DispatchQueue
- Using .receive(on:) before .sink when the downstream updates UI
- Calling assign(to:on:) from a non-main context without switching threads first
- Chaining operators that perform work on background threads before receiving on main

## Solutions

### Solution 1: Subscribe on the main thread with DispatchQueue.main

Ensure that the subscription happens on the main thread so UI updates are safe.

```swift
import Combine

class DataViewModel: ObservableObject {
    @Published var items: [String] = []
    private var cancellables = Set<AnyCancellable>()

    func loadItems() {
        URLSession.shared.dataTaskPublisher(for: url)
            .map { $0.data }
            .decode(type: [String].self, decoder: JSONDecoder())
            .receive(on: DispatchQueue.main)
            .sink(receiveCompletion: { _ in },
                  receiveValue: { [weak self] items in
                self?.items = items
            })
            .store(in: &cancellables)
    }
}
```

### Solution 2: Use receive(on: RunLoop.main) for UI updates

Use receive(on:) with RunLoop.main to ensure downstream subscribers run on the main thread.

```swift
class SearchViewModel: ObservableObject {
    @Published var results: [SearchResult] = []
    private var cancellables = Set<AnyCancellable>()

    func search(query: String) {
        Just(query)
            .debounce(for: .milliseconds(300), scheduler: RunLoop.main)
            .removeDuplicates()
            .flatMap { query in
                self.apiClient.search(query: query)
            }
            .receive(on: DispatchQueue.main)
            .sink(receiveCompletion: { _ in },
                  receiveValue: { [weak self] results in
                self?.results = results
            })
            .store(in: &cancellables)
    }
}
```

### Solution 3: Use assign(to:on:) with the main thread

For simple value binding, use assign(to:on:) to safely update a property on a specific object.

```swift
class TimerViewModel: ObservableObject {
    @Published var elapsed: TimeInterval = 0
    private var cancellables = Set<AnyCancellable>()

    func startTimer() {
        Timer.publish(every: 1.0, on: .main, in: .common)
            .autoconnect()
            .receive(on: DispatchQueue.main)
            .assign(to: \.elapsed, on: self)
            .store(in: &cancellables)
    }
}
```

## Prevention Tips

- Always use .receive(on: DispatchQueue.main) before updating UI in .sink
- Avoid subscribing to publishers inside DispatchQueue.global().async blocks
- Use Combine's built-in schedulers instead of manual GCD dispatching
- Test Combine pipelines with ImmediateScheduler for unit tests

## Related Errors

- [Swift concurrency error]({{< relref "/languages/swift/swift-concurrency-error" >}})
- [Swift async sequence error]({{< relref "/languages/swift/swift-async-error" >}})
- [Swift actor isolation error]({{< relref "/languages/swift/swift-actor-error" >}})

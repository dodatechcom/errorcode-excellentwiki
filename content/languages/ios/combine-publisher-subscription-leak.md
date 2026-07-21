---
title: "[Solution] Combine Publisher Subscription Leak"
description: "Fix Combine publisher subscription memory leaks in iOS applications."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Combine Publisher Subscription Leak

Subscriptions that are not stored in a cancellable set will be deallocated immediately, causing the publisher to never receive values.

## Common Causes
- Subscription not stored in AnyCancellable set
- Cancellable set deallocated before publisher completes
- Using .sink without storing the cancellable
- Forgetting to store cancellables in the class

## How to Fix
1. Store all subscriptions in a Set<AnyCancellable>
2. Use cancellable store in the owning class
3. Use .store(in: &cancellables) at the end of the chain
4. Ensure the cancellable set has the same lifetime as the subscriber

```swift
class ViewModel {
    var cancellables = Set<AnyCancellable>()

    func loadData() {
        service.fetch()
            .receive(on: DispatchQueue.main)
            .sink { completion in
                // Handle completion
            } receiveValue: { [weak self] value in
                self?.updateUI(with: value)
            }
            .store(in: &cancellables)
    }
}
```

## Examples
```swift
// Proper Combine subscription management:
class DataModel: ObservableObject {
    @Published var items: [Item] = []
    private var cancellables = Set<AnyCancellable>()

    init() {
        NotificationCenter.default.publisher(for: .dataUpdated)
            .sink { [weak self] _ in
                self?.refresh()
            }
            .store(in: &cancellables)
    }
}
```

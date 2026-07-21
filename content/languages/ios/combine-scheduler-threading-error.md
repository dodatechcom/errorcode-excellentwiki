---
title: "[Solution] Combine Scheduler Threading Error"
description: "Fix Combine scheduler threading issues causing UI updates on background threads."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Combine Scheduler Threading Error

Combine publishers deliver values on the scheduler they are created on. Failing to switch to the main scheduler before UI updates causes threading violations.

## Common Causes
- Publisher created on background scheduler
- receive(on:) not called before UI updates
- DispatchQueue.main used instead of RunLoop.main
- Multiple scheduler switches causing race conditions

## How to Fix
1. Use receive(on: DispatchQueue.main) for UI updates
2. Use receive(on: RunLoop.main) for time-sensitive UI
3. Avoid unnecessary scheduler switches
4. Test with Thread.isMainThread assertions

```swift
// Correct threading:
service.fetch()
    .receive(on: DispatchQueue.main) // UI updates on main thread
    .sink { value in
        self.label.text = value // Safe
    }
    .store(in: &cancellables)
```

## Examples
```swift
// Thread-safe Combine pipeline:
publisher
    .subscribe(on: DispatchQueue.global()) // Background processing
    .map { transform($0) } // Still on background
    .receive(on: DispatchQueue.main) // Switch to main for UI
    .sink { [weak self] result in
        self?.updateUI(result) // Safe to update UI
    }
    .store(in: &cancellables)
```

---
title: "[Solution] Swift Actor Isolation Error Fix"
description: "Fix Swift actor isolation errors. Learn why actor isolation fails and how to handle concurrency access properly."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["actor", "isolation", "concurrency", "swift"]
weight: 5
---

## What This Error Means

An actor isolation error occurs when you try to access actor-isolated state from outside the actor. Swift actors protect shared mutable state, and accessing their properties or methods from non-isolated code causes compilation errors.

## Common Causes

- Accessing actor properties from outside
- Mixing async and sync contexts
- Missing await when calling actor methods
- Sendable conformance issues

## How to Fix

```swift
// WRONG: Accessing actor property from outside
actor Counter {
    var count = 0
}

let counter = Counter()
print(counter.count)  // Error: actor-isolated property

// CORRECT: Use await
let counter = Counter()
let count = await counter.count
```

```swift
// WRONG: Not using await for actor method
actor DataStore {
    func save(_ data: Data) { }
}

let store = DataStore()
store.save(data)  // Error: actor-isolated method

// CORRECT: Use await
let store = DataStore()
await store.save(data)
```

```swift
// WRONG: Mixing actor and non-actor contexts
actor MyActor {
    var value = 0
    func update() {
        value += 1
        nonIsolatedFunction()  // Error: may access actor state
    }
}

// CORRECT: Mark function as nonisolated
func nonIsolatedFunction() { }
```

## Examples

```swift
// Example 1: Basic actor
actor BankAccount {
    var balance: Double = 0

    func deposit(_ amount: Double) {
        balance += amount
    }

    func withdraw(_ amount: Double) -> Bool {
        guard balance >= amount else { return false }
        balance -= amount
        return true
    }
}

// Example 2: Actor with async access
Task {
    let account = BankAccount()
    await account.deposit(100)
    let balance = await account.balance
    print("Balance: \(balance)")
}

// Example 3: Actor with Sendable
actor Config {
    var settings: [String: Any] = [:]

    func update(_ key: String, value: Any) {
        settings[key] = value
    }
}
```

## Related Errors

- [Sendable protocol error](sendable-error) — Sendable conformance
- [Swift concurrency error](swift-concurrency-error) — async/await error
- [Memory access error](memory-access-error) — EXC_BAD_ACCESS

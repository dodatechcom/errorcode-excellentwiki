---
title: "[Solution] C++ std::future_error - promise already satisfied"
description: "Fix C++ std::future_error when promise is already satisfied or future already retrieved."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# std::future_error - promise already satisfied

`std::future_error` is thrown when you try to satisfy a `std::promise` that has already been set, or retrieve a `std::future` that has already been retrieved.

## Common Causes

```cpp
// Cause 1: Setting value twice
std::promise<int> p;
p.set_value(1);
p.set_value(2); // throws future_error (promise_already_satisfied)

// Cause 2: Getting future twice
std::promise<int> p;
auto f1 = p.get_future();
auto f2 = p.get_future(); // throws (future_already_retrieved)
```

## How to Fix

### Fix 1: Check if already satisfied

```cpp
std::promise<int> p;
auto f = p.get_future();

// Check before setting
if (f.valid()) {
    p.set_value(42);
}
```

### Fix 2: Use try_set_value

```cpp
std::promise<int> p;
bool success1 = p.set_value(1); // true
bool success2 = p.set_value(2); // false (no throw)
```

### Fix 3: Use shared_future

```cpp
std::promise<int> p;
std::shared_future<int> f = p.get_future().share();
auto f2 = f; // OK — shared_future can be copied
```

## Related Errors

- [std::promise already satisfied]({{< relref "/languages/cpp/promise-already-satisfied" >}}) — detailed analysis.
- [std::future_error (retrieved)]({{< relref "/languages/cpp/future-error-2" >}}) — future already retrieved.
- [std::bad_function_call]({{< relref "/languages/cpp/bad-function-call" >}}) — empty function.

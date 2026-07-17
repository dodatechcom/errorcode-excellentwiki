---
title: "[Solution] C++ std::future Already Retrieved — Double Get Fix"
description: "Fix C++ std::future already retrieved error when calling get() twice. Learn proper future usage and shared state management."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::future Already Retrieved — Double Get Fix

A `std::future_error` with `std::errc::future_already_retrieved` is thrown when you call `get()` on a `std::future` that has already had `get()` called on it. A `std::future` can only have its value retrieved once — after that, the shared state is invalidated.

## Why Future Already Retrieved Occurs

Common causes include calling `get()` twice on the same future, attempting to retrieve the result in multiple code paths, and misunderstanding that `std::future` is a one-shot value retrieval mechanism.

## Wrong: Calling get() Twice

```cpp
// WRONG — throws future_error: future_already_retrieved
#include <future>
#include <iostream>

int main() {
    std::promise<int> prom;
    auto fut = prom.get_future();

    prom.set_value(42);

    std::cout << fut.get() << std::endl;  // first get — OK
    std::cout << fut.get() << std::endl;  // second get — throws
    return 0;
}
```

## Correct: Call get() Only Once

```cpp
// CORRECT — retrieve value exactly once
#include <future>
#include <iostream>

int main() {
    std::promise<int> prom;
    auto fut = prom.get_future();

    prom.set_value(42);

    int value = fut.get();  // retrieve once
    std::cout << "Value: " << value << std::endl;
    return 0;
}
```

## Use std::shared_future for Multiple Access

```cpp
// CORRECT — shared_future can be retrieved multiple times
#include <future>
#include <iostream>

int main() {
    std::promise<int> prom;
    auto fut = prom.get_future().share();  // convert to shared_future

    prom.set_value(42);

    std::cout << "First: " << fut.get() << std::endl;   // OK
    std::cout << "Second: " << fut.get() << std::endl;  // OK
    return 0;
}
```

## Store Result Before Sharing

```cpp
// CORRECT — store result for repeated access
#include <future>
#include <iostream>
#include <string>

class ResultCache {
    std::promise<std::string> prom_;
    std::shared_future<std::string> fut_;
    std::string cached_;
    bool retrieved_ = false;

public:
    ResultCache() : fut_(prom_.get_future().share()) {}

    void set_result(std::string value) {
        prom_.set_value(std::move(value));
    }

    const std::string& get() {
        if (!retrieved_) {
            cached_ = fut_.get();
            retrieved_ = true;
        }
        return cached_;
    }
};

int main() {
    ResultCache cache;
    cache.set_result("computed value");

    std::cout << cache.get() << std::endl;
    std::cout << cache.get() << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Call `get()` only once on `std::future` | Always — future is single-use |
| Use `std::shared_future` | When multiple threads need the result |
| Store the result in a local variable | When you need the value later |
| Convert to `shared_future` immediately | When you know multiple retrievals are needed |

## Related Errors

- [std::promise already satisfied]({{< relref "/languages/cpp/promise-already-satisfied" >}}) — setting value twice on promise.
- [std::future_error]({{< relref "/languages/cpp/future-error" >}}) — general future errors.
- [std::packaged_task error]({{< relref "/languages/cpp/packaged-task" >}}) — packaged_task issues.

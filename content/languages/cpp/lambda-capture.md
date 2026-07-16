---
title: "[Solution] C++ Lambda Capture — Lambda Capture Error Fix"
description: "Fix C++ lambda capture errors including dangling references, missing captures, and capture-by-move issues. Learn correct lambda capture patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["lambda", "capture", "closure", "dangling"]
weight: 5
---

# [Solution] C++ Lambda Capture — Lambda Capture Error Fix

Lambda capture errors occur when a lambda captures a variable by reference and the variable goes out of scope before the lambda is invoked, when a needed variable is not captured, or when moving captured values incorrectly. These lead to undefined behavior or compilation errors.

## Why Lambda Capture Errors Occur

Common causes include capturing local variables by reference that go out of scope, forgetting to capture `this` in member lambdas, accidentally capturing by value when mutation is needed, and using `[=]` or `[&]` over-capturing unintended variables.

## Wrong: Capturing Local by Reference

```cpp
// WRONG — dangling reference in lambda
#include <functional>
#include <iostream>

std::function<int()> make_counter() {
    int count = 0;
    return [&count]() { return ++count; };  // dangling reference
}

int main() {
    auto counter = make_counter();
    std::cout << counter() << std::endl;  // UB
    return 0;
}
```

## Correct: Capture by Value When Out of Scope

```cpp
// CORRECT — capture by value for lifetime safety
#include <functional>
#include <iostream>

std::function<int()> make_counter() {
    int count = 0;
    return [count]() mutable { return ++count; };
}

int main() {
    auto counter = make_counter();
    std::cout << counter() << std::endl;  // 1
    std::cout << counter() << std::endl;  // 2
    return 0;
}
```

## Use Init Capture for Move Semantics

```cpp
// CORRECT — move capture for expensive objects
#include <memory>
#include <iostream>
#include <string>

auto make_processor() {
    auto data = std::make_unique<std::string>("hello");
    return [d = std::move(data)]() mutable {
        std::cout << *d << std::endl;
        *d = "modified";
        std::cout << *d << std::endl;
    };
}

int main() {
    auto process = make_processor();
    process();
    return 0;
}
```

## Explicit Capture Lists

```cpp
// CORRECT — capture only what you need
#include <iostream>
#include <string>

int main() {
    int x = 10;
    std::string name = "Alice";

    auto fn = [x, &name]() {  // x by value, name by reference
        std::cout << name << ": " << x << std::endl;
    };

    fn();
    name = "Bob";
    fn();
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Capture by value `[=]` | When the lambda outlives the variable |
| Capture by reference `[&]` | When the lambda is called within the scope |
| Use init capture `[x = std::move(p)]` | For move-only types |
| Use explicit capture list | To avoid over-capturing |

## Related Errors

- [std::bind exceptions]({{< relref "/languages/cpp/bind-exceptions" >}}) — std::bind issues.
- [std::function exceptions]({{< relref "/languages/cpp/function-exceptions" >}}) — std::function issues.
- [std::bad_function_call]({{< relref "/languages/cpp/bad-function-call" >}}) — invoking empty callable.

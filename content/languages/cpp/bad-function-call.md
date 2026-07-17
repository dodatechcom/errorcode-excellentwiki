---
title: "[Solution] C++ std::bad_function_call - empty function"
description: "Fix C++ std::bad_function_call when invoking empty std::function. Check validity before calling."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-function-call", "function", "empty", "callable", "invoke"]
weight: 5
---

# std::bad_function_call - empty function

`std::bad_function_call` is thrown when you invoke an empty `std::function` (one that holds no callable target).

## Common Causes

```cpp
// Cause 1: Empty function
std::function<void()> f;
f(); // throws

// Cause 2: After move
std::function<int()> g = []{ return 42; };
std::function<int()> h = std::move(g);
int val = g(); // throws — g is now empty

// Cause 3: Null function pointer
std::function<int()> f = nullptr;
f(); // throws
```

## How to Fix

### Fix 1: Check if callable

```cpp
std::function<void()> f = get_callback();
if (f) {
    f(); // safe
}
```

### Fix 2: Provide default function

```cpp
std::function<void()> f = []{ /* default */ };
```

### Fix 3: Use target to check

```cpp
if (f.target<void(*)()>() != nullptr) {
    f();
}
```

## Examples

```cpp
#include <functional>
#include <iostream>

void safe_call(std::function<void()> f) {
    if (f) {
        f();
    } else {
        std::cerr << "Function is empty" << std::endl;
    }
}

int main() {
    std::function<void()> empty;
    safe_call(empty); // prints "Function is empty"
    safe_call([]{ std::cout << "Called!" << std::endl; });
    return 0;
}
```

## Related Errors

- [std::bad_weak_ptr]({{< relref "/languages/cpp/bad-weak-ptr" >}}) — expired weak_ptr.
- [std::bad_optional_access]({{< relref "/languages/cpp/bad-optional-access" >}}) — empty optional.
- [std::bad_any_cast]({{< relref "/languages/cpp/any-cast-error" >}}) — any_cast failure.

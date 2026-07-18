---
title: "[Solution] C++ noexcept Error — How to Fix"
description: "Fix C++ noexcept errors including violated noexcept specifiers, unexpected exceptions in move constructors, and noexcept operator misuse."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime", "compile-time"]
weight: 5
comments: true
---

# [Solution] C++ noexcept Error — How to Fix

`noexcept` specifiers guarantee a function won't throw exceptions, but violating this guarantee by allowing an exception to escape calls `std::terminate`. Incorrect use in move constructors, swap functions, and destructors can break exception safety.

## Why It Happens

Noexcept errors occur when a `noexcept`-marked function throws an exception (causing `std::terminate`), when move constructors lack `noexcept` preventing container optimizations, when the `noexcept` operator is used incorrectly in conditional contexts, or when noexcept specifications conflict with virtual function overrides.

## Common Error Messages

1. `terminate called after throwing an exception in a noexcept function`
2. `warning: exception specification of overriding function is more restrictive`
3. `error: cannot throw expression — function is noexcept`
4. `error: noexcept operator applied to non-call expression`

## How to Fix It

### Fix 1: Make Move Constructors noexcept

```cpp
#include <vector>
#include <string>
#include <iostream>

class Buffer {
    int* data_;
    std::size_t size_;
public:
    Buffer(std::size_t n) : data_(new int[n]), size_(n) {}

    // WRONG — missing noexcept, vector won't use move
    // Buffer(Buffer&& other) : data_(other.data_), size_(other.size_) {
    //     other.data_ = nullptr;
    // }

    // CORRECT — noexcept enables move optimization
    Buffer(Buffer&& other) noexcept : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
    }

    ~Buffer() { delete[] data_; }
};

int main() {
    std::vector<Buffer> vec;
    vec.push_back(Buffer(100));  // uses move if noexcept
    return 0;
}
```

### Fix 2: Use noexcept Conditionally

```cpp
#include <type_traits>
#include <iostream>

template <typename T>
void safe_swap(T& a, T& b) noexcept(noexcept(T(std::move(a)))) {
    T temp = std::move(a);
    a = std::move(b);
    b = std::move(temp);
}

int main() {
    int x = 1, y = 2;
    safe_swap(x, y);  // noexcept because int move is noexcept
    std::cout << x << " " << y << "\n";  // 2 1
    return 0;
}
```

### Fix 3: Don't Throw from noexcept Functions

```cpp
#include <stdexcept>
#include <iostream>

// WRONG — will call std::terminate if allocation fails
// void process() noexcept {
//     throw std::runtime_error("error");
// }

// CORRECT — let non-noexcept functions throw freely
void process() {
    throw std::runtime_error("error");
}

// CORRECT — noexcept for operations that truly won't throw
void cleanup() noexcept {
    // cleanup code that should never throw
}

int main() {
    try {
        process();
    } catch (const std::exception& e) {
        std::cout << e.what() << "\n";
    }
    return 0;
}
```

### Fix 4: noexcept with Destructors

```cpp
#include <iostream>
#include <vector>

class Resource {
    int* data_;
public:
    Resource() : data_(new int[10]{}) {}
    ~Resource() { delete[] data_; }

    // Destructors are implicitly noexcept — don't throw from them
    // ~Resource() { throw std::runtime_error("bad"); }  // WRONG
};

int main() {
    std::vector<Resource> vec(3);
    vec.clear();  // calls destructors — must not throw
    return 0;
}
```

## Common Scenarios

- **Move semantics**: Without `noexcept`, `std::vector` copies instead of moves during reallocation.
- **Virtual overrides**: Overriding a `noexcept` virtual function with a throwing one is undefined behavior.
- **Swap functions**: `std::swap` relies on move constructors being `noexcept` for strong exception guarantee.

## Prevent It

1. Always mark move constructors and move assignment operators as `noexcept`.
2. Use `noexcept(expression)` conditionally when the exception safety depends on the contained type.
3. Never throw exceptions from destructors, swap functions, or any function marked `noexcept`.

## Related Errors

- [System error]({{< relref "/languages/cpp/system-error-system" >}}) — system call failures.
- [Logic error]({{< relref "/languages/cpp/logic-error" >}}) — program logic issues.
- [Bad alloc]({{< relref "/languages/cpp/bad-allocation" >}}) — memory allocation failures.

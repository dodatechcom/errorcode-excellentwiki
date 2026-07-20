---
title: "[Solution] C++ noexcept Violation — std::terminate Fix"
description: "Fix noexcept violation and std::terminate by removing noexcept, handling exceptions, and using noexcept(false) when needed."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 921
---

# C++ noexcept Violation — std::terminate Fix

When an exception escapes a function marked `noexcept`, the runtime calls `std::terminate` immediately — no stack unwinding, no catch blocks. This is a hard crash. The fix is either to remove `noexcept`, handle all exceptions inside the function, or ensure the function truly cannot throw.

## Common Causes

```cpp
// Cause 1: noexcept function that throws
#include <stdexcept>

void safe_operation() noexcept {
    throw std::runtime_error("oops");  // std::terminate called
}

int main() {
    try {
        safe_operation();
    } catch (...) {
        // Never reached — terminate already called
    }
    return 0;
}
```

```cpp
// Cause 2: Move constructor marked noexcept but throws
#include <string>

class Buffer {
    std::string data_;
public:
    Buffer(Buffer&& other) noexcept  // WRONG: string move can throw
        : data_(std::move(other.data_)) {}
};
// If std::string's move constructor throws, std::terminate
```

```cpp
// Cause 3: Destructor that throws through noexcept
class Resource {
public:
    ~Resource() noexcept {  // destructors are implicitly noexcept in C++11+
        throw std::runtime_error("cleanup failed");  // std::terminate
    }
};
```

```cpp
// Cause 4: Container operations with noexcept-violating move
#include <vector>

class MayThrowMove {
    std::string data_;
public:
    MayThrowMove(MayThrowMove&&) noexcept(false) = default;
};

int main() {
    std::vector<MayThrowMove> v;
    v.emplace_back("hello");  // may trigger std::terminate during reallocation
    return 0;
}
```

```cpp
// Cause 5: std::function with noexcept mismatch
#include <functional>

void callback() noexcept {
    throw std::runtime_error("error");
}

int main() {
    std::function<void()> f = callback;
    f();  // std::terminate — exception from noexcept function
    return 0;
}
```

## How to Fix

### Fix 1: Remove noexcept or Make It Conditional

```cpp
#include <stdexcept>
#include <iostream>

// Option A: remove noexcept entirely
void operation() {
    throw std::runtime_error("oops");
}

// Option B: use noexcept(false) explicitly
void operation2() noexcept(false) {
    throw std::runtime_error("oops");
}

int main() {
    try {
        operation();
    } catch (const std::exception& e) {
        std::cout << "Caught: " << e.what() << std::endl;  // works
    }
    return 0;
}
```

### Fix 2: Handle All Exceptions Inside noexcept

```cpp
#include <stdexcept>
#include <iostream>

void safe_operation() noexcept {
    try {
        throw std::runtime_error("oops");
    } catch (const std::exception& e) {
        std::cerr << "Handled: " << e.what() << std::endl;
    } catch (...) {
        std::cerr << "Unknown error" << std::endl;
    }
    // No exception escapes — noexcept is valid
}

int main() {
    safe_operation();
    return 0;
}
```

### Fix 3: Use noexcept Conditionally

```cpp
#include <type_traits>
#include <string>

class Buffer {
    std::string data_;
public:
    // noexcept only if string move is noexcept
    Buffer(Buffer&& other) noexcept(std::is_nothrow_move_constructible_v<std::string>)
        : data_(std::move(other.data_)) {}
};

// Or use the noexcept operator:
template <typename T>
void swap_vals(T& a, T& b) noexcept(noexcept(T(std::move(a)))) {
    T tmp = std::move(a);
    a = std::move(b);
    b = std::move(tmp);
}
```

### Fix 4: Use noexcept(false) for Potentially-Throwing Moves

```cpp
#include <string>
#include <vector>

class ComplexResource {
    std::string name_;
    std::vector<int> data_;
public:
    // noexcept(false) — honest about potential to throw
    ComplexResource(ComplexResource&& other) noexcept(false)
        : name_(std::move(other.name_))
        , data_(std::move(other.data_)) {}

    // Swap is often a better noexcept candidate
    friend void swap(ComplexResource& a, ComplexResource& b) noexcept {
        using std::swap;
        swap(a.name_, b.name_);
        swap(a.data_, b.data_);
    }
};
```

### Fix 5: Use std::terminate_handler for Debugging

```cpp
#include <exception>
#include <iostream>
#include <stdexcept>

void my_terminate() {
    std::cerr << "terminate called — printing backtrace" << std::endl;
    // In production, log the call stack
    std::abort();
}

int main() {
    std::set_terminate(my_terminate);

    void bad_func() noexcept {
        throw std::runtime_error("crash");
    }

    bad_func();  // calls my_terminate instead of default terminate
    return 0;
}
```

## Examples

```cpp
// Real-world: noexcept policy for a performance-critical container
#include <string>
#include <utility>

template <typename T>
class FastStack {
    T* data_;
    size_t size_;
    size_t capacity_;

public:
    FastStack() : data_(nullptr), size_(0), capacity_(0) {}
    ~FastStack() { delete[] data_; }

    // Move: noexcept only if T's move is noexcept
    FastStack(FastStack&& other) noexcept(std::is_nothrow_move_constructible_v<T>)
        : data_(other.data_), size_(other.size_), capacity_(other.capacity_) {
        other.data_ = nullptr;
        other.size_ = 0;
        other.capacity_ = 0;
    }

    // If T's move can throw, use non-noexcept move and copy-and-swap
    FastStack(FastStack&& other) requires (!std::is_nothrow_move_constructible_v<T>)
        : FastStack() {
        // Copy then move — provides strong exception guarantee
        FastStack temp(other);
        swap(*this, temp);
    }

    friend void swap(FastStack& a, FastStack& b) noexcept {
        using std::swap;
        swap(a.data_, b.data_);
        swap(a.size_, b.size_);
        swap(a.capacity_, b.capacity_);
    }
};
```

## Related Errors

- [Exception in destructor]({{< relref "/languages/cpp/exception-destructor" >}}) — exceptions during cleanup.
- [Stack unwinding error]({{< relref "/languages/cpp/stack-unwinding-error" >}}) — cleanup during exception propagation.
- [Exception safety guarantees]({{< relref "/languages/cpp/exception-safety-guarantees" >}}) — guarantee violations.

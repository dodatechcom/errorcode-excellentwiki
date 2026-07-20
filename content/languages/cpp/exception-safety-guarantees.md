---
title: "[Solution] C++ Exception Safety Guarantee Violation — Fix"
description: "Fix exception safety guarantee violations using basic, strong, and no-throw guarantees, plus the copy-swap idiom."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 924
---

# C++ Exception Safety Guarantee Violation — Fix

Exception safety guarantees define what happens to program invariants when an exception occurs. The three levels are: **basic guarantee** (no leaks, invariants preserved), **strong guarantee** (commit-or-rollback, state unchanged on exception), and **no-throw guarantee** (operation never fails). Violating these leads to resource leaks, corrupted state, or crashes.

## Common Causes

```cpp
// Cause 1: Resource leak in non-RAII code
#include <stdexcept>

void process() {
    int* a = new int[100];
    int* b = new int[200];
    // If this throws, a and b are leaked
    throw std::runtime_error("error");
    delete[] a;
    delete[] b;
}
```

```cpp
// Cause 2: Partial update without strong guarantee
#include <vector>
#include <string>

class Record {
    std::vector<std::string> fields_;
public:
    void update(const std::vector<std::string>& new_fields) {
        // Save old state
        auto old = fields_;
        fields_.clear();
        for (const auto& f : new_fields) {
            fields_.push_back(f);  // if this throws, fields_ is already cleared
        }
        // Should use copy-and-swap instead
    }
};
```

```cpp
// Cause 3: Container insertion without basic guarantee
#include <vector>

void add_items(std::vector<int>& v) {
    v.push_back(1);  // may throw, but vector handles this — basic guarantee OK
    v.push_back(2);
    // But if push_back(2) throws, we have one extra element — violates strong guarantee
}
```

```cpp
// Cause 4: Exception during move leaves object in bad state
#include <string>

class BadMove {
    std::string data_;
    int* raw_ptr_;
public:
    BadMove(BadMove&& other)
        : data_(std::move(other.data_))  // if this throws, raw_ptr_ not moved
        , raw_ptr_(other.raw_ptr_) {
        other.raw_ptr_ = nullptr;
    }
};
```

```cpp
// Cause 5: No-throw assumption violated
#include <vector>

void no_throw_func() noexcept {
    std::vector<int> v;
    v.push_back(1);  // may allocate — CAN throw std::bad_alloc
    // Assumption of no-throw is wrong
}
```

## How to Fix

### Fix 1: Use RAII for Basic Guarantee

```cpp
#include <memory>
#include <stdexcept>

void safe_process() {
    auto a = std::make_unique<int[]>(100);
    auto b = std::make_unique<int[]>(200);

    throw std::runtime_error("error");
    // a and b automatically cleaned up — basic guarantee met
}
```

### Fix 2: Use Copy-and-Swap for Strong Guarantee

```cpp
#include <vector>
#include <string>
#include <utility>

class Record {
    std::vector<std::string> fields_;

    friend void swap(Record& a, Record& b) noexcept {
        using std::swap;
        swap(a.fields_, b.fields_);
    }

public:
    Record() = default;

    // Strong guarantee: if anything throws, original state unchanged
    void update(const std::vector<std::string>& new_fields) {
        Record temp;
        temp.fields_.assign(new_fields.begin(), new_fields.end());
        swap(*this, temp);
        // If assign throws, *this is unchanged
        // If swap succeeds, update is committed
    }
};
```

### Fix 3: Pre-Allocate to Avoid Mid-Operation Throws

```cpp
#include <vector>
#include <string>

class DataProcessor {
    std::vector<int> buffer_;
public:
    void process(const std::vector<int>& input) {
        // Pre-allocate — no reallocation during processing
        buffer_.reserve(input.size());

        for (int val : input) {
            buffer_.push_back(val);  // won't throw (capacity reserved)
        }
    }

    void safe_update(const std::vector<int>& new_data) {
        // Create new buffer, then swap — strong guarantee
        std::vector<int> temp;
        temp.reserve(new_data.size());
        for (int val : new_data) {
            temp.push_back(val);
        }
        buffer_.swap(temp);  // no-throw operation
    }
};
```

### Fix 4: Use no-throw Guarantee for Critical Operations

```cpp
#include <utility>
#include <vector>

class NoThrowStack {
    std::vector<int> data_;

public:
    // no-throw: swap and move for vectors are noexcept
    friend void swap(NoThrowStack& a, NoThrowStack& b) noexcept {
        a.data_.swap(b.data_);  // vector::swap is noexcept
    }

    // Basic guarantee: push_back may throw but leaves valid state
    void push(int val) {
        data_.push_back(val);
    }

    // no-throw guarantee
    void pop() noexcept {
        data_.pop_back();
    }

    bool empty() const noexcept {
        return data_.empty();
    }
};
```

### Fix 5: Commit-or-Rollback with Exception-Safe Patterns

```cpp
#include <string>
#include <vector>
#include <memory>

class TransactionalBuffer {
    std::vector<int> data_;

public:
    // Strong guarantee via copy-modify-swap
    void replace_all(const std::vector<int>& new_data) {
        std::vector<int> backup = data_;  // may throw, but *this unchanged

        try {
            backup = new_data;  // may throw, but *this unchanged
        } catch (...) {
            throw;  // *this still has original data
        }

        data_.swap(backup);  // noexcept — commit
    }

    // Strong guarantee via function extraction
    void transform_all(int (*func)(int)) {
        std::vector<int> result;
        result.reserve(data_.size());

        for (int val : data_) {
            result.push_back(func(val));  // may throw
        }

        data_.swap(result);  // commit — noexcept
    }
};
```

## Examples

```cpp
// Real-world: exception-safe shared_ptr-like class
#include <algorithm>
#include <cstddef>
#include <stdexcept>

template <typename T>
class SharedPtr {
    T* ptr_;
    size_t* count_;

    void release() noexcept {
        if (count_ && --(*count_) == 0) {
            delete ptr_;
            delete count_;
        }
    }

public:
    SharedPtr() noexcept : ptr_(nullptr), count_(nullptr) {}
    explicit SharedPtr(T* p) : ptr_(p), count_(new size_t(1)) {}

    ~SharedPtr() noexcept { release(); }

    // Copy: basic guarantee (allocation may throw)
    SharedPtr(const SharedPtr& other)
        : ptr_(other.ptr_), count_(other.count_) {
        if (count_) ++(*count_);
    }

    // Move: no-throw guarantee
    SharedPtr(SharedPtr&& other) noexcept
        : ptr_(other.ptr_), count_(other.count_) {
        other.ptr_ = nullptr;
        other.count_ = nullptr;
    }

    SharedPtr& operator=(SharedPtr other) noexcept {
        swap(*this, other);
        return *this;
    }

    friend void swap(SharedPtr& a, SharedPtr& b) noexcept {
        std::swap(a.ptr_, b.ptr_);
        std::swap(a.count_, b.count_);
    }

    T& operator*() const { return *ptr_; }
    T* operator->() const { return ptr_; }
};
```

## Related Errors

- [noexcept violation]({{< relref "/languages/cpp/noexcept-violation" >}}) — exception from noexcept function.
- [Exception in destructor]({{< relref "/languages/cpp/exception-destructor" >}}) — exceptions during cleanup.
- [Stack unwinding error]({{< relref "/languages/cpp/stack-unwinding-error" >}}) — cleanup during propagation.

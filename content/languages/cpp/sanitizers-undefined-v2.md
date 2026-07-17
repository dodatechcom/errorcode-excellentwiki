---
title: "[Solution] UBSan Undefined Behavior Detected Fix"
description: "Fix UndefinedBehaviorSanitizer detected errors. Handle signed integer overflow, null pointer dereference, and alignment issues."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# UBSan Undefined Behavior Detected

Fix UndefinedBehaviorSanitizer detected errors. Handle signed integer overflow, null pointer dereference, and alignment issues.

## What This Error Means

UBSan detects undefined behavior at runtime:

```
runtime error: signed integer overflow: 2147483647 + 1 cannot be represented in type 'int'
runtime error: null pointer passed as argument 2, which is declared to never be null
runtime error: load of misaligned address 0x... for type 'int', which requires 4 byte alignment
```

## Common Causes

```cpp
// Cause 1: Signed integer overflow
int x = INT_MAX + 1; // UB!

// Cause 2: Null pointer dereference
int* p = nullptr;
*p = 42; // UB!

// Cause 3: Shift overflow
int y = 1 << 32; // UB - shift amount >= width of type

// Cause 4: Misaligned access
char buf[8];
int* ip = reinterpret_cast<int*>(buf + 1);
*ip = 42; // UB - misaligned
```

## How to Fix

### Fix 1: Use unsigned types for bit operations

```cpp
#include <cstdint>

uint32_t shift_value(uint32_t val, int shift) {
    if (shift >= 32) return 0;
    return val << shift;
}
```

### Fix 2: Check for null before dereferencing

```cpp
void process(int* ptr) {
    if (ptr == nullptr) {
        return;
    }
    *ptr = 42;
}
```

### Fix 3: Use safe arithmetic

```cpp
#include <limits>
#include <stdexcept>

int safe_add(int a, int b) {
    if (b > 0 && a > std::numeric_limits<int>::max() - b) {
        throw std::overflow_error("Integer overflow");
    }
    if (b < 0 && a < std::numeric_limits<int>::min() - b) {
        throw std::underflow_error("Integer underflow");
    }
    return a + b;
}
```

## Examples

```cpp
#include <cstdint>
#include <limits>
#include <stdexcept>

class SafeInt {
    int value_;

public:
    explicit SafeInt(int v) : value_(v) {}

    SafeInt operator+(const SafeInt& other) const {
        int64_t result = static_cast<int64_t>(value_) + other.value_;
        if (result > std::numeric_limits<int>::max() ||
            result < std::numeric_limits<int>::min()) {
            throw std::overflow_error("Integer overflow in addition");
        }
        return SafeInt(static_cast<int>(result));
    }

    int value() const { return value_; }
};

int main() {
    try {
        SafeInt a(std::numeric_limits<int>::max());
        SafeInt b(1);
        SafeInt c = a + b; // Throws
    } catch (const std::overflow_error& e) {
        // Handled safely
    }
    return 0;
}
```

## Related Errors

- [Sanitizers Undefined]({{< relref "/languages/cpp/sanitizers-undefined" >}}) — UBSan error
- [Sanitizers Address]({{< relref "/languages/cpp/sanitizers-address-v2" >}}) — ASan error
- [Overflow Error]({{< relref "/languages/cpp/overflow-error-example" >}}) — overflow error

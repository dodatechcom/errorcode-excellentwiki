---
title: "[Solution] C++ UBSan Error — How to Fix"
description: "Fix C++ UndefinedBehaviorSanitizer errors including signed integer overflow, misaligned pointer access, and shift-exponent violations in C++ code."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ UBSan Error — How to Fix

UndefinedBehaviorSanitizer (UBSan) detects undefined behavior including signed integer overflow, null pointer dereference, misaligned memory access, and invalid shift operations that the C++ standard defines as undefined.

## Why It Happens

UBSan errors indicate actual undefined behavior in the code: signed integer overflow from unchecked arithmetic, shift operations with exponents >= type width, null pointer member access, out-of-bounds array indexing, or misaligned pointer dereferences on strict-alignment platforms.

## Common Error Messages

1. `runtime error: signed integer overflow: 2147483647 + 1 cannot be represented`
2. `runtime error: shift exponent 32 is too large for 32-bit type`
3. `runtime error: null pointer passed as argument`
4. `runtime error: load of misaligned address`

## How to Fix It

### Fix 1: Fix Signed Integer Overflow

```cpp
#include <iostream>
#include <limits>

// WRONG — signed overflow is UB
int bad_add(int a, int b) {
    return a + b;  // UB if result overflows
}

// CORRECT — check before arithmetic
int safe_add(int a, int b) {
    if ((b > 0 && a > std::numeric_limits<int>::max() - b) ||
        (b < 0 && a < std::numeric_limits<int>::min() - b)) {
        throw std::overflow_error("integer overflow");
    }
    return a + b;
}

int main() {
    try {
        std::cout << safe_add(2000000000, 2000000000) << "\n";
    } catch (const std::overflow_error& e) {
        std::cout << e.what() << "\n";
    }
    return 0;
}
```

### Fix 2: Prevent Shift Exponent Errors

```cpp
#include <iostream>
#include <cstdint>

int main() {
    uint32_t value = 1;
    int shift = 33;

    // WRONG — shift by >= type width is UB
    // uint32_t result = value << shift;

    // CORRECT — validate shift
    if (shift >= 0 && shift < 32) {
        uint32_t result = value << shift;
        std::cout << "Result: " << result << "\n";
    } else {
        std::cout << "Invalid shift amount\n";
    }

    return 0;
}
```

### Fix 3: Avoid Null Pointer Dereference

```cpp
#include <iostream>
#include <memory>

void process(int* ptr) {
    // CORRECT — check for null
    if (!ptr) {
        std::cout << "Null pointer passed\n";
        return;
    }
    std::cout << "Value: " << *ptr << "\n";
}

int main() {
    process(nullptr);
    int val = 42;
    process(&val);
    return 0;
}
```

### Fix 4: Use Alignment-Safe Memory Access

```cpp
#include <iostream>
#include <cstdint>
#include <cstring>

int main() {
    char buffer[16];
    // CORRECT — use memcpy for potentially unaligned access
    int value = 42;
    std::memcpy(buffer, &value, sizeof(int));

    int result;
    std::memcpy(&result, buffer, sizeof(int));
    std::cout << result << "\n";

    // Or ensure proper alignment
    alignas(int) int aligned_val;
    std::memcpy(&aligned_val, buffer, sizeof(int));
    std::cout << aligned_val << "\n";

    return 0;
}
```

## Common Scenarios

- **Signed overflow**: `INT_MAX + 1` is undefined — use unsigned or checked arithmetic.
- **Null dereference**: Accessing members through null pointers is always UB.
- **Strict aliasing**: Accessing an object through an incompatible pointer type.

## Prevent It

1. Compile with `-fsanitize=undefined` in debug and CI builds.
2. Use unsigned integers for arithmetic that may overflow.
3. Always check pointers for null before dereferencing.

## Related Errors

- [Sanitizer error]({{< relref "/languages/cpp/cpp-sanitizer-error.md" >}}) — memory safety issues.
- [TSan error]({{< relref "/languages/cpp/cpp-tsan-error.md" >}}) — thread safety issues.
- [Overflow error]({{< relref "/languages/cpp/overflowerror" >}}) — arithmetic overflow.

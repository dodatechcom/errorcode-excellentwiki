---
title: "[Solution] C++ MSan Error — How to Fix"
description: "Fix C++ MemorySanitizer errors including use-of-uninitialized-value bugs, conditional jumps on uninitialized data, and uninitialized memory reads."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ MSan Error — How to Fix

MemorySanitizer (MSan) detects reads of uninitialized memory values that can cause unpredictable program behavior, including conditional branches based on uninitialized data and uninitialized values flowing into system calls.

## Why It Happens

MSan errors occur when variables are used before initialization, when structs contain uninitialized padding bytes, when memory obtained via `malloc` is used without `memset`, when `std::vector::resize` is used without initializing new elements, or when reading from partially initialized objects.

## Common Error Messages

1. `WARNING: MemorySanitizer: use-of-uninitialized-value`
2. `WARNING: MemorySanitizer: conditional jump depends on uninitialized value`
3. `WARNING: MemorySanitizer: stack-use-after-scope`
4. `Uninitialized value used in property access`

## How to Fix It

### Fix 1: Initialize All Variables

```cpp
#include <iostream>

int main() {
    // WRONG — uninitialized variable
    // int x;
    // if (x > 0) { ... }  // MSan error

    // CORRECT — always initialize
    int x = 0;
    if (x > 0) {
        std::cout << "Positive\n";
    } else {
        std::cout << "Non-positive\n";
    }

    return 0;
}
```

### Fix 2: Initialize Struct Members

```cpp
#include <iostream>

struct Config {
    int width = 0;
    int height = 0;
    bool enabled = false;
};

// WRONG — uninitialized padding bytes
// struct BadConfig { char a; int b; };

int main() {
    // CORRECT — all members initialized
    Config cfg;
    std::cout << cfg.width << "x" << cfg.height << "\n";

    // CORRECT — zero-initialize with {}
    int arr[10] = {};  // all zeros
    std::cout << arr[5] << "\n";

    return 0;
}
```

### Fix 3: Use memset for Raw Memory

```cpp
#include <iostream>
#include <cstdlib>
#include <cstring>

int main() {
    // WRONG — malloc doesn't initialize memory
    // int* p = (int*)malloc(sizeof(int) * 10);

    // CORRECT — zero-initialize allocated memory
    int* p = static_cast<int*>(malloc(sizeof(int) * 10));
    std::memset(p, 0, sizeof(int) * 10);

    std::cout << p[5] << "\n";  // 0, no MSan error

    std::free(p);
    return 0;
}
```

### Fix 4: Use value-initialization with vector

```cpp
#include <vector>
#include <iostream>

int main() {
    // WRONG — resize doesn't initialize POD types
    // std::vector<int> v(10);
    // v.resize(20);  // elements 10-19 are uninitialized

    // CORRECT — use value-initialization
    std::vector<int> v(10, 0);
    v.resize(20, 0);  // new elements initialized to 0

    // CORRECT — assign immediately
    std::vector<int> v2(20);
    for (auto& x : v2) x = 0;

    std::cout << v[15] << "\n";

    return 0;
}
```

## Common Scenarios

- **Stack variables**: Local variables used before initialization on the stack.
- **Struct padding**: Unused bytes in structs between members.
- **malloc buffers**: Raw memory from `malloc`/`realloc` not zeroed before use.

## Prevent It

1. Compile with `-fsanitize=memory` and run test suites to detect uninitialized reads.
2. Always initialize variables at declaration: `int x = 0;` not `int x;`.
3. Prefer `std::vector<int>(n, 0)` over `std::vector<int>(n)` for POD types.

## Related Errors

- [Sanitizer error]({{< relref "/languages/cpp/cpp-sanitizer-error.md" >}}) — memory safety issues.
- [UBSan error]({{< relref "/languages/cpp/cpp-ubsan-error.md" >}}) — undefined behavior issues.
- [TSan error]({{< relref "/languages/cpp/cpp-tsan-error.md" >}}) — thread safety issues.

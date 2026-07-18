---
title: "[Solution] C++ Sanitizer Error — How to Fix"
description: "Fix C++ sanitizer errors including AddressSanitizer, UBSan, and ThreadSanitizer violations that detect memory and thread safety issues."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ Sanitizer Error — How to Fix

C++ sanitizers detect undefined behavior, memory errors, and thread safety violations at runtime. Sanitizer errors indicate real bugs that need fixing in the source code, not configuration issues.

## Why It Happens

Sanitizer errors occur when the code has buffer overflows, use-after-free bugs, data races between threads, integer overflow in signed arithmetic, or null pointer dereferences that would otherwise cause unpredictable behavior.

## Common Error Messages

1. `AddressSanitizer: heap-buffer-overflow on address`
2. `AddressSanitizer: stack-buffer-underflow`
3. `ThreadSanitizer: data race`
4. `UndefinedBehaviorSanitizer: signed integer overflow`

## How to Fix It

### Fix 1: Compile with AddressSanitizer

```bash
# Enable AddressSanitizer
g++ -fsanitize=address -fno-omit-frame-pointer -g -O1 src/*.cpp -o app

# Run the program
./app
```

### Fix 2: Fix the Detected Memory Bug

```cpp
#include <iostream>
#include <vector>

// WRONG — buffer overflow
void bad_function() {
    int arr[5] = {1, 2, 3, 4, 5};
    // ASan would flag: arr[10] = 42;  // out of bounds

    // CORRECT — bounds checking
    std::vector<int> safe_arr = {1, 2, 3, 4, 5};
    if (safe_arr.size() > 10) {
        safe_arr[10] = 42;
    }
}

int main() {
    bad_function();
    return 0;
}
```

### Fix 3: Use Multiple Sanitizers Together

```bash
# Combine AddressSanitizer with UndefinedBehaviorSanitizer
g++ -fsanitize=address,undefined \
    -fno-omit-frame-pointer -g -O1 \
    src/*.cpp -o app

# With LeakSanitizer (enabled by default with ASan on Linux)
ASAN_OPTIONS=detect_leaks=1 ./app
```

### Fix 4: Fix Use-After-Free

```cpp
#include <iostream>
#include <memory>

int main() {
    // WRONG — use after free
    // int* p = new int(42);
    // delete p;
    // std::cout << *p;  // use-after-free

    // CORRECT — use smart pointers
    auto p = std::make_unique<int>(42);
    std::cout << *p << "\n";
    // automatically freed when p goes out of scope

    return 0;
}
```

## Common Scenarios

- **Heap overflow**: Writing beyond allocated heap buffer boundaries.
- **Stack overflow**: Accessing stack arrays beyond their declared size.
- **Data race**: Two threads accessing the same memory without synchronization.

## Prevent It

1. Run sanitizers in CI/CD pipelines on every pull request.
2. Fix all sanitizer warnings immediately — they represent real bugs.
3. Use `-fno-omit-frame-pointer` for better stack traces in sanitizer output.

## Related Errors

- [UBSan error]({{< relref "/languages/cpp/cpp-ubsan-error.md" >}}) — undefined behavior detection.
- [TSan error]({{< relref "/languages/cpp/cpp-tsan-error.md" >}}) — thread safety issues.
- [MSan error]({{< relref "/languages/cpp/cpp-msan-error.md" >}}) — uninitialized memory issues.

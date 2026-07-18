---
title: "[Solution] C++ Valgrind Error — How to Fix"
description: "Fix C++ Valgrind memory errors including memory leaks, invalid reads/writes, and use of uninitialized values detected by memcheck."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ Valgrind Error — How to Fix

Valgrind memcheck detects memory leaks, invalid memory access, and use of uninitialized values in C++ programs. Each error type requires specific fixes in source code to properly manage memory.

## Why It Happens

Valgrind errors occur when dynamically allocated memory isn't freed (leak), when pointers are dereferenced after being freed (invalid read/write), when memory is read before being written (uninitialized value), when double-free occurs, or when buffer overflows occur.

## Common Error Messages

1. `Invalid read of size 4 — use after free`
2. `1,024 bytes in 1 blocks are definitely lost — memory leak`
3. `Conditional jump depends on uninitialized value`
4. `Invalid free() / delete — double free`

## How to Fix It

### Fix 1: Fix Memory Leaks

```cpp
#include <iostream>
#include <memory>

// WRONG — memory leak
void leak() {
    int* p = new int(42);
    std::cout << *p << "\n";
    // forgot: delete p;
}

// CORRECT — use smart pointers
void no_leak() {
    auto p = std::make_unique<int>(42);
    std::cout << *p << "\n";
    // automatically freed
}

int main() {
    no_leak();
    return 0;
}
```

### Fix 2: Fix Invalid Reads and Writes

```cpp
#include <iostream>
#include <vector>

int main() {
    // WRONG — invalid read
    // std::vector<int> v;
    // std::cout << v[0];  // empty vector

    // CORRECT — check size before access
    std::vector<int> v = {1, 2, 3};
    if (!v.empty()) {
        std::cout << v[0] << "\n";
    }

    // WRONG — buffer overflow
    // int arr[5];
    // arr[10] = 42;

    // CORRECT — bounds checking
    std::vector<int> arr(5);
    if (arr.size() > 10) {
        arr[10] = 42;
    }

    return 0;
}
```

### Fix 3: Initialize Memory Before Use

```cpp
#include <iostream>
#include <cstring>
#include <cstdlib>

int main() {
    // WRONG — uninitialized memory
    // int* arr = (int*)malloc(5 * sizeof(int));
    // int sum = arr[0] + arr[1];  // valgrind: uninitialized value

    // CORRECT — initialize after allocation
    int* arr = static_cast<int*>(malloc(5 * sizeof(int)));
    std::memset(arr, 0, 5 * sizeof(int));

    int sum = arr[0] + arr[1];
    std::cout << "Sum: " << sum << "\n";

    std::free(arr);
    return 0;
}
```

### Fix 4: Avoid Double Free

```cpp
#include <iostream>
#include <memory>

int main() {
    // WRONG — double free
    // int* p = new int(42);
    // delete p;
    // delete p;  // double free

    // CORRECT — set to nullptr after delete
    int* p = new int(42);
    delete p;
    p = nullptr;  // safe to delete again (no-op)

    // BETTER — use smart pointers
    auto sp = std::make_unique<int>(42);
    // sp is automatically managed

    return 0;
}
```

## Common Scenarios

- **Leaked allocations**: `new` without corresponding `delete` or smart pointer.
- **Use after free**: Accessing memory after `delete` has been called.
- **Uninitialized reads**: Using `malloc` memory without `memset` or reading before writing.

## Prevent It

1. Run `valgrind --leak-check=full ./app` on every test suite run.
2. Use `std::unique_ptr` and `std::shared_ptr` for all dynamic allocations.
3. Compile with `-fsanitize=address` for faster detection during development.

## Related Errors

- [Sanitizer error]({{< relref "/languages/cpp/cpp-sanitizer-error.md" >}}) — memory safety issues.
- [MSan error]({{< relref "/languages/cpp/cpp-msan-error.md" >}}) — uninitialized memory issues.
- [Bad alloc]({{< relref "/languages/cpp/bad-allocation" >}}) — memory allocation failures.

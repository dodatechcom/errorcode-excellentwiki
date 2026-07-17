---
title: "[Solution] C++ std::unique_ptr — Unique Pointer Error Fix"
description: "Fix C++ std::unique_ptr errors including use-after-move, double deletion, and incorrect array deletion. Learn RAII ownership patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::unique_ptr — Unique Pointer Error Fix

`std::unique_ptr` errors typically involve using a moved-from pointer, mismatched array deleters, or attempting to copy a unique_ptr. These errors lead to undefined behavior, null pointer dereferences, or compile-time failures.

## Why unique_ptr Errors Occur

Common causes include using a unique_ptr after it has been moved, creating unique_ptr with `delete` instead of `delete[]` for arrays, attempting to copy unique_ptr (compile error), and creating raw pointer ownership conflicts.

## Wrong: Using unique_ptr After Move

```cpp
// WRONG — use-after-move leads to null dereference
#include <memory>
#include <iostream>

int main() {
    auto ptr = std::make_unique<int>(42);
    auto moved = std::move(ptr);  // ptr is now null

    std::cout << *ptr << std::endl;  // UB — dereferencing null
    return 0;
}
```

## Correct: Check for Null After Move

```cpp
// CORRECT — check before using after potential move
#include <memory>
#include <iostream>

void process(std::unique_ptr<int> p) {
    if (p) {
        std::cout << "Value: " << *p << std::endl;
    } else {
        std::cout << "Null pointer" << std::endl;
    }
}

int main() {
    auto ptr = std::make_unique<int>(42);
    process(std::move(ptr));

    // ptr is now null
    if (!ptr) {
        std::cout << "ptr is null after move" << std::endl;
    }
    return 0;
}
```

## Use Correct Deleter for Arrays

```cpp
// CORRECT — use unique_ptr with array deleter
#include <memory>
#include <iostream>

int main() {
    // For arrays, use unique_ptr<T[]> or custom deleter
    auto arr = std::make_unique<int[]>(10);
    arr[0] = 42;
    arr[9] = 99;

    std::cout << arr[0] << " " << arr[9] << std::endl;
    return 0;
}
```

## Transfer Ownership With std::move

```cpp
// CORRECT — explicit ownership transfer
#include <memory>
#include <iostream>
#include <string>

class Resource {
    std::string name_;
public:
    explicit Resource(std::string name) : name_(std::move(name)) {
        std::cout << "Created: " << name_ << std::endl;
    }
    ~Resource() { std::cout << "Destroyed: " << name_ << std::endl; }
};

int main() {
    auto r1 = std::make_unique<Resource>("file.txt");
    auto r2 = std::move(r1);  // ownership transferred

    if (!r1) {
        std::cout << "r1 is null — ownership transferred to r2" << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check for null before dereferencing | After `std::move` |
| Use `std::make_unique<T[]>` | For dynamic arrays |
| Use `std::move` for ownership transfer | When transferring between owners |
| Never copy `unique_ptr` | Use `std::move` instead |

## Related Errors

- [std::shared_ptr errors]({{< relref "/languages/cpp/shared-ptr" >}}) — shared ownership issues.
- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — memory allocation failure.
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type on variant.

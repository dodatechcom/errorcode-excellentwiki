---
title: "[Solution] C++ std::shared_ptr — Shared Pointer Error Fix"
description: "Fix C++ std::shared_ptr errors including circular references, dangling pointers, and thread safety issues. Learn smart pointer best practices."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::shared_ptr — Shared Pointer Error Fix

`std::shared_ptr` errors include memory leaks from circular references (cycles), dangling pointers from misuse, undefined behavior from creating multiple `shared_ptr` from raw pointers, and data races on the reference count when shared across threads without proper synchronization.

## Why shared_ptr Errors Occur

Common causes include circular references between objects (both hold shared_ptr to each other), creating multiple independent shared_ptr groups from the same raw pointer, accessing the managed object after it has been destroyed, and thread safety issues when modifying shared_ptr concurrently.

## Wrong: Creating Circular References

```cpp
// WRONG — memory leak from circular reference
#include <memory>
#include <iostream>

struct Node {
    std::shared_ptr<Node> next;  // strong reference
    ~Node() { std::cout << "Destroyed" << std::endl; }
};

int main() {
    auto a = std::make_shared<Node>();
    auto b = std::make_shared<Node>();
    a->next = b;
    b->next = a;  // circular reference — neither is freed

    a.reset();
    b.reset();
    // "Destroyed" never printed — memory leak
    return 0;
}
```

## Correct: Use weak_ptr to Break Cycles

```cpp
// CORRECT — use weak_ptr for back-references
#include <memory>
#include <iostream>

struct Node {
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;  // weak reference breaks cycle
    ~Node() { std::cout << "Destroyed" << std::endl; }
};

int main() {
    auto a = std::make_shared<Node>();
    auto b = std::make_shared<Node>();
    a->next = b;
    b->prev = a;

    a.reset();
    b.reset();
    // Both destroyed correctly
    return 0;
}
```

## Don't Create Multiple shared_ptr From Same Raw Pointer

```cpp
// WRONG — double-free from multiple control blocks
#include <memory>

int main() {
    int* raw = new int(42);
    std::shared_ptr<int> p1(raw);
    std::shared_ptr<int> p2(raw);  // UB — double delete
    return 0;
}
```

## Use make_shared or allocate_shared

```cpp
// CORRECT — single allocation for object and control block
#include <memory>
#include <iostream>

int main() {
    auto p1 = std::make_shared<int>(42);
    auto p2 = std::make_shared<std::string>("hello");

    std::cout << *p1 << " " << *p2 << std::endl;

    // Shared ownership
    auto p3 = p1;
    std::cout << "Use count: " << p1.use_count() << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `std::weak_ptr` for back-references | To break circular references |
| Use `std::make_shared` | When creating new shared objects |
| Never create two `shared_ptr` from same raw | Always |
| Check `use_count()` | When debugging ownership issues |

## Related Errors

- [std::weak_ptr expired]({{< relref "/languages/cpp/weak-ptr-expired" >}}) — expired weak_ptr access.
- [std::bad_weak_ptr]({{< relref "/languages/cpp/bad-weak-ptr" >}}) — constructing from expired weak_ptr.
- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — memory allocation failure.

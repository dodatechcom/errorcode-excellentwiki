---
title: "[Solution] C++ std::bad_weak_ptr — Expired Weak Pointer Fix"
description: "Fix C++ std::bad_weak_ptr when constructing shared_ptr from an expired weak_ptr. Handle weak pointer lifecycle safely."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["bad-weak-ptr", "weak-ptr", "shared-ptr", "smart-pointer"]
weight: 5
---

# [Solution] C++ std::bad_weak_ptr — Expired Weak Pointer Fix

A `std::bad_weak_ptr` is thrown when you try to construct a `std::shared_ptr` from a `std::weak_ptr` using the `weak_ptr::lock()` or `shared_ptr(weak_ptr)` constructor, and the referenced object has already been destroyed. This exception was introduced in C++11.

## Why std::bad_weak_ptr Occurs

Common causes include creating a `shared_ptr` from a `weak_ptr` after the last `shared_ptr` to the object has been destroyed, holding a `weak_ptr` beyond the lifetime of the managed object, and race conditions in multithreaded code where one thread destroys the last `shared_ptr` while another tries to lock a `weak_ptr`.

## Wrong: Constructing shared_ptr from Expired weak_ptr

```cpp
// WRONG — throws std::bad_weak_ptr
#include <memory>
#include <iostream>

int main() {
    std::weak_ptr<int> weak;

    {
        auto shared = std::make_shared<int>(42);
        weak = shared;
    }  // shared destroyed here

    auto locked = weak.lock();
    if (!locked) {
        std::cout << "Weak pointer expired" << std::endl;
    }

    // This throws std::bad_weak_ptr
    std::shared_ptr<int> ptr(weak);
    std::cout << *ptr << std::endl;
    return 0;
}
```

## Correct: Check expired() or Use lock() Before Constructing

```cpp
// CORRECT — check before constructing shared_ptr
#include <memory>
#include <iostream>

int main() {
    std::weak_ptr<int> weak;

    {
        auto shared = std::make_shared<int>(42);
        weak = shared;
    }

    if (auto locked = weak.lock()) {
        std::cout << "Value: " << *locked << std::endl;
    } else {
        std::cout << "Object has been destroyed" << std::endl;
    }
    return 0;
}
```

## Use weak_ptr to Break Circular References

```cpp
// CORRECT — use weak_ptr to avoid prevent reference cycles
#include <memory>
#include <iostream>
#include <string>

struct Node {
    std::string name;
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> parent;  // weak to avoid cycle

    Node(const std::string& n) : name(n) {
        std::cout << "Created: " << name << std::endl;
    }

    ~Node() {
        std::cout << "Destroyed: " << name << std::endl;
    }
};

int main() {
    auto root = std::make_shared<Node>("root");
    auto child = std::make_shared<Node>("child");

    child->next = root;
    root->parent = child;

    if (auto p = root->parent.lock()) {
        std::cout << "Parent: " << p->name << std::endl;
    }
    return 0;
}
```

## Safe weak_ptr Usage Pattern

```cpp
// CORRECT — always check before using weak_ptr
#include <memory>
#include <iostream>

class Widget {
    std::weak_ptr<Widget> sibling_;

public:
    void set_sibling(std::weak_ptr<Widget> s) { sibling_ = s; }

    void do_work() {
        if (auto s = sibling_.lock()) {
            std::cout << "Sibling is alive" << std::endl;
        } else {
            std::cout << "Sibling is gone" << std::endl;
        }
    }
};

int main() {
    auto w1 = std::make_shared<Widget>();
    auto w2 = std::make_shared<Widget>();

    w1->set_sibling(w2);
    w2->set_sibling(w1);

    w1->do_work();
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Always use `lock()` before constructing `shared_ptr` | When the object might be destroyed |
| Use `weak_ptr` for back-references | To avoid circular reference cycles |
| Check `expired()` or use `if(auto p = wp.lock())` | Before accessing the managed object |
| Store `shared_ptr` for ownership, `weak_ptr` for observation | As a design pattern |

## Related Errors

- [std::shared_ptr errors]({{< relref "/languages/cpp/shared-ptr" >}}) — shared pointer issues.
- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — memory allocation failure.
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type on variant.

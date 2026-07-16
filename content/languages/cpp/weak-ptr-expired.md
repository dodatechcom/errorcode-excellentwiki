---
title: "[Solution] C++ std::weak_ptr Expired — Expired Weak Pointer Fix"
description: "Fix C++ std::weak_ptr expired access when the managed object has been destroyed. Learn safe weak_ptr usage patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["weak-ptr", "expired", "smart-pointer", "shared-ptr"]
weight: 5
---

# [Solution] C++ std::weak_ptr Expired — Expired Weak Pointer Fix

A `std::weak_ptr` becomes expired when all `std::shared_ptr` instances managing the object have been destroyed. Calling `lock()` returns nullptr, and attempting to access the object through an expired `weak_ptr` without checking leads to null pointer dereferences.

## Why weak_ptr Expired Occurs

Common causes include the last `shared_ptr` to the object being destroyed, holding a `weak_ptr` beyond the managed object's lifetime, race conditions where one thread destroys the last `shared_ptr` while another accesses via `weak_ptr`, and forgetting to check `lock()` result.

## Wrong: Using Expired weak_ptr Without Checking

```cpp
// WRONG — null dereference on expired weak_ptr
#include <memory>
#include <iostream>

int main() {
    std::weak_ptr<int> weak;

    {
        auto shared = std::make_shared<int>(42);
        weak = shared;
    }  // shared destroyed — weak is expired

    auto ptr = weak.lock();
    std::cout << *ptr << std::endl;  // UB — ptr is null
    return 0;
}
```

## Correct: Check lock() Result Before Use

```cpp
// CORRECT — always check lock() result
#include <memory>
#include <iostream>

int main() {
    std::weak_ptr<int> weak;

    {
        auto shared = std::make_shared<int>(42);
        weak = shared;
    }

    if (auto ptr = weak.lock()) {
        std::cout << "Value: " << *ptr << std::endl;
    } else {
        std::cout << "Object has been destroyed" << std::endl;
    }
    return 0;
}
```

## Use expired() to Check State

```cpp
// CORRECT — check expired() before lock()
#include <memory>
#include <iostream>

void observe(std::weak_ptr<int> weak) {
    if (weak.expired()) {
        std::cout << "Expired — cannot access" << std::endl;
        return;
    }

    auto ptr = weak.lock();
    if (ptr) {
        std::cout << "Value: " << *ptr << std::endl;
    }
}

int main() {
    auto shared = std::make_shared<int>(100);
    std::weak_ptr<int> weak = shared;

    observe(weak);
    shared.reset();
    observe(weak);
    return 0;
}
```

## Safe Observer Pattern

```cpp
// CORRECT — weak_ptr for observer pattern
#include <memory>
#include <iostream>

class Subject {
    int value_ = 0;
    std::weak_ptr<class Observer> observer_;

public:
    void set_observer(std::shared_ptr<Observer> obs) { observer_ = obs; }
    void set_value(int v) { value_ = v; notify(); }
    void notify();
    int value() const { return value_; }
};

class Observer : public std::enable_shared_from_this<Observer> {
public:
    void on_change(int val) { std::cout << "Notified: " << val << std::endl; }
};

void Subject::notify() {
    if (auto obs = observer_.lock()) {
        obs->on_change(value_);
    }
}

int main() {
    auto obs = std::make_shared<Observer>();
    Subject subj;
    subj.set_observer(obs);
    subj.set_value(42);
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Always check `lock()` result | Before dereferencing weak_ptr |
| Use `expired()` for quick checks | When you only need existence check |
| Store `shared_ptr` for ownership | Use `weak_ptr` only for observation |
| Use `enable_shared_from_this` | When objects need weak_ptr to themselves |

## Related Errors

- [std::bad_weak_ptr]({{< relref "/languages/cpp/bad-weak-ptr" >}}) — constructing shared_ptr from expired weak_ptr.
- [std::shared_ptr errors]({{< relref "/languages/cpp/shared-ptr" >}}) — shared ownership issues.
- [std::unique_ptr errors]({{< relref "/languages/cpp/unique-ptr" >}}) — unique ownership issues.

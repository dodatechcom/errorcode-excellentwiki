---
title: "[Solution] C++ std::bad_weak_ptr — Expired Weak Pointer Fix"
description: "Fix C++ std::bad_weak_ptr when locking an expired weak_ptr. Handle shared_ptr lifecycle and validate weak pointers before use."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-weak-ptr", "weak-ptr", "shared-ptr", "exception"]
weight: 50
---

# [Solution] C++ std::bad_weak_ptr — Expired Weak Pointer Fix

A `std::bad_weak_ptr` is thrown by `std::shared_ptr` constructor when you pass an expired `std::weak_ptr` directly to a `shared_ptr` constructor. This occurs when the original `shared_ptr` has been destroyed and the weak reference is no longer valid. Note that calling `weak_ptr::lock()` does not throw this exception — it returns an empty `shared_ptr` instead.

## Common Causes

- Constructing a `shared_ptr` from an expired `weak_ptr`
- Using `weak_ptr` after the observed object has been destroyed
- Race conditions in multithreaded code where the object is destroyed between checking and using the `weak_ptr`
- Circular references that prevent proper cleanup

## Example: Throwing std::bad_weak_ptr

```cpp
#include <memory>
#include <iostream>

int main() {
    std::weak_ptr<int> wp;
    {
        auto sp = std::make_shared<int>(42);
        wp = sp;
    }  // sp destroyed, wp is now expired

    // This throws std::bad_weak_ptr
    auto sp2 = std::shared_ptr<int>(wp);
    return 0;
}
```

## How to Fix: Use weak_ptr::lock() to Check Expiration

```cpp
#include <memory>
#include <iostream>

int main() {
    std::weak_ptr<int> wp;
    {
        auto sp = std::make_shared<int>(42);
        wp = sp;
    }

    auto sp2 = wp.lock();
    if (sp2) {
        std::cout << "Value: " << *sp2 << std::endl;
    } else {
        std::cerr << "weak_ptr has expired" << std::endl;
    }
    return 0;
}
```

## Checking Expiration Before Use

```cpp
#include <memory>
#include <iostream>

class Resource {
    std::string name_;
public:
    explicit Resource(std::string name) : name_(std::move(name)) {}
    ~Resource() { std::cout << "Resource " << name_ << " destroyed" << std::endl; }
    const std::string& name() const { return name_; }
};

int main() {
    std::weak_ptr<Resource> wp;
    {
        auto sp = std::make_shared<Resource>("database");
        wp = sp;
    }

    if (wp.expired()) {
        std::cerr << "Resource is gone" << std::endl;
    } else {
        auto sp = wp.lock();
        if (sp) {
            std::cout << "Using resource: " << sp->name() << std::endl;
        }
    }
    return 0;
}
```

## Safe Observer Pattern with weak_ptr

```cpp
#include <memory>
#include <iostream>
#include <vector>

class Observer : public std::enable_shared_from_this<Observer> {
public:
    void on_event() {
        std::cout << "Observer received event" << std::endl;
    }
};

class EventDispatcher {
    std::vector<std::weak_ptr<Observer>> observers_;
public:
    void add_observer(std::shared_ptr<Observer> obs) {
        observers_.push_back(obs);
    }

    void notify() {
        for (auto it = observers_.begin(); it != observers_.end();) {
            auto sp = it->lock();
            if (sp) {
                sp->on_event();
                ++it;
            } else {
                it = observers_.erase(it);
            }
        }
    }
};

int main() {
    EventDispatcher dispatcher;
    {
        auto obs = std::make_shared<Observer>();
        dispatcher.add_observer(obs);
        dispatcher.notify();
    }
    dispatcher.notify();
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `weak_ptr::lock()` | Always when converting `weak_ptr` to `shared_ptr` |
| Check `expired()` before `lock()` | When you want explicit expiration check |
| Clean up expired weak pointers | When storing weak pointers in containers |
| Use `enable_shared_from_this` | When objects need to produce shared_ptr from `this` |

## Related Errors

- [std::bad_alloc]({{< relref "/languages/cpp/std-bad-alloc" >}}) — memory allocation failure.
- [std::bad_function_call]({{< relref "/languages/cpp/bad-function-call" >}}) — invoking an empty callable.
- [std::bad_any_cast]({{< relref "/languages/cpp/bad-any-cast" >}}) — invalid `std::any` cast.

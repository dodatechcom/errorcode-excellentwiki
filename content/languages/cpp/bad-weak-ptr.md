---
title: "[Solution] C++ std::bad_weak_ptr - expired weak_ptr"
description: "Fix C++ std::bad_weak_ptr when converting expired weak_ptr to shared_ptr. Check expiry before lock."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-weak-ptr", "weak-ptr", "shared-ptr", "expired", "lock"]
weight: 5
---

# std::bad_weak_ptr - expired weak_ptr

`std::bad_weak_ptr` is thrown when a `std::weak_ptr` that has expired is used in contexts that require a valid `shared_ptr`.

## Common Causes

```cpp
// Cause 1: Expired weak_ptr
std::weak_ptr<int> wp;
{
    auto sp = std::make_shared<int>(42);
    wp = sp;
} // sp destroyed, wp expired
auto sp = wp.lock(); // sp is nullptr

// Cause 2: Using expired pointer
std::weak_ptr<int> wp;
// ... wp expires ...
std::shared_ptr<int> sp = wp.lock(); // returns nullptr
int val = *sp; // undefined behavior (dereferencing null)

// Cause 3: make_shared_from_this after destruction
class Obj : public std::enable_shared_from_this<Obj> {
    std::shared_ptr<Obj> get_self() {
        return shared_from_this(); // throws if not managed
    }
};
```

## How to Fix

### Fix 1: Check lock() result

```cpp
std::shared_ptr<int> sp = wp.lock();
if (sp) {
    int val = *sp;
}
```

### Fix 2: Check expired()

```cpp
if (!wp.expired()) {
    auto sp = wp.lock();
}
```

### Fix 3: Use shared_from_this safely

```cpp
class Obj : public std::enable_shared_from_this<Obj> {
    std::shared_ptr<Obj> get_self() {
        try {
            return shared_from_this();
        } catch (const std::bad_weak_ptr&) {
            return nullptr;
        }
    }
};
```

## Related Errors

- [std::bad_function_call]({{< relref "/languages/cpp/bad-function-call" >}}) — empty function.
- [std::bad_optional_access]({{< relref "/languages/cpp/bad-optional-access" >}}) — empty optional.
- [std::bad_exception]({{< relref "/languages/cpp/bad-exception" >}}) — unexpected exception.

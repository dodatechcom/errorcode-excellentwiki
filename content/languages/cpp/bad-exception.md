---
title: "[Solution] C++ std::bad_exception - unexpected exception"
description: "Fix C++ std::bad_exception from unexpected exception types. Use proper exception specifications."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-exception", "unexpected", "exception", "dynamic-exception", "throw"]
weight: 5
---

# std::bad_exception - unexpected exception

`std::bad_exception` is thrown when a function throws an exception not listed in its dynamic exception specification. This is mostly obsolete in C++17 and later.

## Common Causes

```cpp
// Cause 1: Dynamic exception specification (pre-C++17)
void func() throw(int) {
    throw "string"; // throws bad_exception
}

// Cause 2: noexcept violation
void func() noexcept {
    throw 42; // std::terminate called (not bad_exception)
}

// Cause 3: Virtual function exception mismatch
class Base {
    virtual void f() throw(int);
};
class Derived : public Base {
    void f() throw(double); // different exception spec
};
```

## How to Fix

### Fix 1: Don't use dynamic exception specifications

```cpp
void func() { // no throw specification
    throw 42; // OK
}
```

### Fix 2: Use noexcept correctly

```cpp
void func() noexcept {
    // if this throws, std::terminate is called
}
```

### Fix 3: Use exception filters in catch

```cpp
try {
    func();
} catch (const std::exception& e) {
    // handle C++ exceptions
} catch (...) {
    // handle everything else
}
```

## Related Errors

- [std::bad_alloc]({{< relref "/languages/cpp/bad-alloc-nostd" >}}) — allocation failure.
- [std::bad_cast]({{< relref "/languages/cpp/bad-cast-dynamic" >}}) — dynamic_cast failure.
- [std::bad_typeid]({{< relref "/languages/cpp/bad-typeid" >}}) — typeid on null.

---
title: "[Solution] C++ std::bad_typeid — Typeid Null Pointer Fix"
description: "Fix C++ std::bad_typeid when using typeid on a null pointer dereference. Learn proper RTTI usage and virtual type checking."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["bad-typeid", "typeid", "rtti", "type-info"]
weight: 5
---

# [Solution] C++ std::bad_typeid — Typeid Null Pointer Fix

A `std::bad_typeid` is thrown when `typeid` is applied to a dereferenced null pointer in a polymorphic context. This can happen when you have a base class pointer that is null and you call `typeid(*ptr)` on it. The exception is defined in `<typeinfo>`.

## Why std::bad_typeid Occurs

Common causes include calling `typeid` on a dereferenced null polymorphic pointer, using `typeid` on a reference that actually binds to a null pointer through dereferencing, and incorrect RTTI usage with uninitialized pointers.

## Wrong: Using typeid on a Null Polymorphic Pointer

```cpp
// WRONG — throws std::bad_typeid
#include <iostream>
#include <typeinfo>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {};

int main() {
    Base* ptr = nullptr;

    // ptr is null — typeid(*ptr) throws std::bad_typeid
    std::cout << typeid(*ptr).name() << std::endl;
    return 0;
}
```

## Correct: Check for Null Before Using typeid

```cpp
// CORRECT — check pointer before typeid
#include <iostream>
#include <typeinfo>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {};

int main() {
    Base* ptr = nullptr;

    if (ptr != nullptr) {
        std::cout << typeid(*ptr).name() << std::endl;
    } else {
        std::cerr << "Null pointer — cannot determine type" << std::endl;
    }
    return 0;
}
```

## Use typeid on Non-Polymorphic Types Safely

```cpp
// CORRECT — typeid on non-pointer types is always safe
#include <iostream>
#include <typeinfo>

class NonVirtual {
public:
    int data;
};

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {};

int main() {
    NonVirtual nv;
    std::cout << typeid(nv).name() << std::endl;  // always safe

    Derived d;
    Base& ref = d;
    std::cout << typeid(ref).name() << std::endl;  // safe — ref is valid
    return 0;
}
```

## Safe Type Checking Pattern

```cpp
// CORRECT — helper for safe polymorphic type checking
#include <iostream>
#include <typeinfo>
#include <string>

class Base {
public:
    virtual ~Base() = default;
    virtual std::string type_name() const { return "Base"; }
};

class Derived : public Base {
public:
    std::string type_name() const override { return "Derived"; }
};

int main() {
    Base* ptr = new Derived();

    if (ptr) {
        std::cout << "Type: " << typeid(*ptr).name() << std::endl;
        std::cout << "Polymorphic name: " << ptr->type_name() << std::endl;
    }

    delete ptr;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check pointer for null before `typeid` | When using polymorphic pointers |
| Use virtual functions instead | When type-specific behavior is needed |
| Use `typeid` on references/objects | When you have a valid (non-null) instance |
| Enable RTTI (`-frtti`) | When compiler has RTTI disabled |

## Related Errors

- [std::bad_cast]({{< relref "/languages/cpp/bad-cast" >}}) — failed `dynamic_cast` on references.
- [std::bad_any_cast]({{< relref "/languages/cpp/badany-cast" >}}) — invalid `std::any` type cast.
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type on variant.

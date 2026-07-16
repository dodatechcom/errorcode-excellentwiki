---
title: "[Solution] C++ dynamic_cast Failed — Static Cast Safety Fix"
description: "Fix C++ dynamic_cast failures when downcasting polymorphic types. Learn safe casting patterns and RTTI usage."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["dynamic-cast", "static-cast", "rtti", "polymorphism"]
weight: 5
---

# [Solution] C++ dynamic_cast Failed — Static Cast Safety Fix

When `dynamic_cast` fails, it either returns `nullptr` (for pointers) or throws `std::bad_cast` (for references). Using `static_cast` instead bypasses runtime type checking and leads to undefined behavior if the cast is invalid. This error occurs when code incorrectly assumes a polymorphic object's type.

## Why dynamic_cast Failures Occur

Common causes include downcasting a base pointer to a derived type when the object is not actually that derived type, using `static_cast` instead of `dynamic_cast` when the type is uncertain, and missing virtual functions in the base class (preventing RTTI).

## Wrong: Using static_cast for Downcast

```cpp
// WRONG — static_cast bypasses type checking, may cause UB
#include <iostream>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void do_work() { std::cout << "Derived::do_work" << std::endl; }
};

class Other : public Base {};

int main() {
    Other obj;
    Base* ptr = &obj;

    Derived* d = static_cast<Derived*>(ptr);  // UB — wrong type
    d->do_work();  // undefined behavior
    return 0;
}
```

## Correct: Use dynamic_cast With Null Check

```cpp
// CORRECT — dynamic_cast returns nullptr on failure
#include <iostream>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void do_work() { std::cout << "Derived::do_work" << std::endl; }
};

int main() {
    Derived obj;
    Base* ptr = &obj;

    if (auto* d = dynamic_cast<Derived*>(ptr)) {
        d->do_work();
    } else {
        std::cerr << "Cast failed" << std::endl;
    }
    return 0;
}
```

## Use typeid for Type Comparison

```cpp
// CORRECT — check type before casting
#include <iostream>
#include <typeinfo>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {};

int main() {
    Derived obj;
    Base& ref = obj;

    if (typeid(ref) == typeid(Derived)) {
        const Derived& d = static_cast<const Derived&>(ref);
        std::cout << "Cast verified" << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `dynamic_cast` | When type is uncertain at compile time |
| Use pointer `dynamic_cast` with null check | When failure is expected |
| Ensure base class has virtual functions | Always — enables RTTI |
| Use `static_cast` only when certain | When the type relationship is guaranteed |

## Related Errors

- [std::bad_cast]({{< relref "/languages/cpp/bad-cast" >}}) — reference dynamic_cast failure.
- [std::bad_typeid]({{< relref "/languages/cpp/bad-typeid" >}}) — typeid on null pointer.
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type on variant.

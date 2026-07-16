---
title: "[Solution] C++ std::bad_cast — Failed Dynamic Cast Fix"
description: "Fix C++ std::bad_cast when dynamic_cast fails in reference contexts. Handle polymorphic type casting safely and validate types before casting."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["bad-cast", "dynamic-cast", "rtti", "exception"]
weight: 50
---

# [Solution] C++ std::bad_cast — Failed Dynamic Cast Fix

A `std::bad_cast` is thrown when you use `dynamic_cast` to convert a reference to a type that the object is not actually an instance of. Unlike pointer-based `dynamic_cast` (which returns `nullptr` on failure), reference-based `dynamic_cast` has no null concept, so it throws `std::bad_cast` instead.

## Why std::bad_cast Occurs

Common causes include using `dynamic_cast` on a reference to an incompatible derived type, casting a base class reference to an unrelated derived class, and attempting downcasts without verifying the actual object type.

## Wrong: Using dynamic_cast on a Reference Without Try-Catch

```cpp
// WRONG — throws std::bad_cast
#include <iostream>
#include <typeinfo>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void specific() { std::cout << "Derived" << std::endl; }
};

class Other : public Base {};

int main() {
    Other obj;
    Base& ref = obj;

    Derived& d = dynamic_cast<Derived&>(ref);  // throws std::bad_cast
    d.specific();
    return 0;
}
```

## Correct: Catch std::bad_cast When Using Reference Casts

```cpp
// CORRECT — catch the exception
#include <iostream>
#include <typeinfo>
#include <stdexcept>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void specific() { std::cout << "Derived" << std::endl; }
};

int main() {
    Derived obj;
    Base& ref = obj;

    try {
        Derived& d = dynamic_cast<Derived&>(ref);
        d.specific();
    } catch (const std::bad_cast& e) {
        std::cerr << "Bad cast: " << e.what() << std::endl;
    }
    return 0;
}
```

## Use Pointer Cast for Safer Pattern

```cpp
// CORRECT — pointer dynamic_cast returns nullptr instead of throwing
#include <iostream>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void specific() { std::cout << "Derived" << std::endl; }
};

int main() {
    Derived obj;
    Base* ptr = &obj;

    if (auto* derived = dynamic_cast<Derived*>(ptr)) {
        derived->specific();
    } else {
        std::cerr << "Cast failed" << std::endl;
    }
    return 0;
}
```

## Safe Downcast Helper

```cpp
// CORRECT — helper for safe reference downcasting
#include <iostream>
#include <typeinfo>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void specific() { std::cout << "Derived" << std::endl; }
};

template <typename Target, typename Source>
Target& safe_cast(Source& src) {
    try {
        return dynamic_cast<Target&>(src);
    } catch (const std::bad_cast&) {
        throw std::bad_cast();
    }
}

int main() {
    Derived obj;
    Base& ref = obj;

    Derived& d = safe_cast<Derived&>(ref);
    d.specific();
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use pointer `dynamic_cast` | When failure is expected — returns `nullptr` |
| Catch `std::bad_cast` | When using reference `dynamic_cast` |
| Check `typeid` before casting | When you need to verify types first |
| Use `static_cast` when certain | When the type relationship is guaranteed |

## Related Errors

- [std::bad_typeid]({{< relref "/languages/cpp/badtypeinfo" >}}) — `typeid` on null pointer.
- [std::bad_any_cast]({{< relref "/languages/cpp/badany-cast" >}}) — invalid `std::any` cast.
- [std::bad_function_call]({{< relref "/languages/cpp/badfunctioncall" >}}) — invoking an empty callable.

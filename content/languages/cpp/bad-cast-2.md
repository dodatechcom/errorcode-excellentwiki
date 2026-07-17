---
title: "[Solution] C++ std::bad_cast — Reference Dynamic Cast Failure Fix"
description: "Fix C++ std::bad_cast when reference-based dynamic_cast fails. Learn safe polymorphic casting patterns and type checking techniques."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::bad_cast — Reference Dynamic Cast Failure Fix

A `std::bad_cast` is thrown when a reference-based `dynamic_cast` fails because the object is not of the target type. Unlike pointer-based `dynamic_cast` which returns `nullptr`, reference casts must throw because references cannot be null. This exception is defined in `<typeinfo>`.

## Why std::bad_cast Occurs

Common causes include downcasting a base class reference to an incompatible derived class, casting references across unrelated class hierarchies, and using `typeid`-based casts in `use_facet` or `dynamic_cast` without verifying the actual type.

## Wrong: Using Reference dynamic_cast Without Handling Failure

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
    void do_work() { std::cout << "Derived::do_work" << std::endl; }
};

class Unrelated : public Base {};

int main() {
    Unrelated obj;
    Base& ref = obj;

    Derived& d = dynamic_cast<Derived&>(ref);  // throws
    d.do_work();
    return 0;
}
```

## Correct: Use Pointer Cast for Safe Downcasting

```cpp
// CORRECT — pointer dynamic_cast returns nullptr on failure
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

    if (auto* derived = dynamic_cast<Derived*>(ptr)) {
        derived->do_work();
    } else {
        std::cerr << "Cast failed" << std::endl;
    }
    return 0;
}
```

## Catch std::bad_cast When Reference Cast Is Required

```cpp
// CORRECT — catch bad_cast for reference casts
#include <iostream>
#include <typeinfo>
#include <stdexcept>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void do_work() { std::cout << "Derived::do_work" << std::endl; }
};

int main() {
    Base* ptr = new Base();

    try {
        Derived& d = dynamic_cast<Derived&>(*ptr);
        d.do_work();
    } catch (const std::bad_cast& e) {
        std::cerr << "Bad cast: " << e.what() << std::endl;
    }
    delete ptr;
    return 0;
}
```

## Use typeid to Check Before Casting

```cpp
// CORRECT — check type before reference cast
#include <iostream>
#include <typeinfo>

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
    Base& ref = obj;

    if (typeid(ref) == typeid(Derived)) {
        Derived& d = static_cast<Derived&>(ref);
        d.do_work();
    } else {
        std::cerr << "Type mismatch" << std::endl;
    }
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use pointer `dynamic_cast` | When failure is expected — returns `nullptr` |
| Catch `std::bad_cast` | When reference `dynamic_cast` is required |
| Check `typeid` first | When you need to verify type before casting |
| Use `static_cast` when certain | When the type relationship is guaranteed |

## Related Errors

- [std::bad_typeid]({{< relref "/languages/cpp/bad-typeid" >}}) — `typeid` on null pointer.
- [std::bad_any_cast]({{< relref "/languages/cpp/badany-cast" >}}) — invalid `std::any` cast.
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type on variant.

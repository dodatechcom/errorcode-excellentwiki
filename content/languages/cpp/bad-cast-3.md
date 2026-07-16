---
title: "[Solution] C++ std::bad_cast — Dynamic Cast Reference Failure Fix"
description: "Fix C++ std::bad_cast when dynamic_cast fails on a reference. Handle polymorphic type casting safely with try-catch and pointer casts."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-cast", "dynamic-cast", "rtti", "exception", "polymorphism"]
weight: 5
---

# [Solution] C++ std::bad_cast — Dynamic Cast Reference Failure Fix

A `std::bad_cast` is thrown when `dynamic_cast<T&>(ref)` is used to cast a reference to a type that the underlying object is not actually an instance of. Unlike pointer-based `dynamic_cast` (which returns `nullptr`), reference-based `dynamic_cast` cannot return null, so it throws `std::bad_cast` from `<typeinfo>`.

## Common Causes

- **Downcasting a base reference to the wrong derived type** — the object is not the target type
- **Casting an unrelated class reference** — no inheritance relationship exists between types
- **Using dynamic_cast without try-catch** — unhandled exception propagates up the call stack
- **Missing virtual destructor** — RTTI may not work correctly without virtual functions

## How to Fix

### Fix 1: Wrap reference dynamic_cast in try-catch

```cpp
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
    Base* obj = new Derived();
    Base& ref = *obj;

    try {
        Derived& d = dynamic_cast<Derived&>(ref);
        d.specific();
    } catch (const std::bad_cast& e) {
        std::cerr << "Cast failed: " << e.what() << std::endl;
    }

    delete obj;
    return 0;
}
```

### Fix 2: Use pointer dynamic_cast (returns nullptr on failure)

```cpp
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
    Base* obj = new Derived();

    if (auto* derived = dynamic_cast<Derived*>(obj)) {
        derived->specific();  // safe
    } else {
        std::cerr << "Not a Derived" << std::endl;
    }

    delete obj;
    return 0;
}
```

### Fix 3: Check typeid before casting

```cpp
#include <iostream>
#include <typeinfo>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {};

int main() {
    Base* obj = new Derived();

    if (typeid(*obj) == typeid(Derived)) {
        Derived& d = static_cast<Derived&>(*obj);  // safe after typeid check
        std::cout << "Confirmed Derived" << std::endl;
    }

    delete obj;
    return 0;
}
```

## Examples

```cpp
#include <iostream>
#include <typeinfo>

class Animal { public: virtual ~Animal() = default; };
class Dog : public Animal {};
class Cat : public Animal {};

int main() {
    Cat cat;
    Animal& ref = cat;

    try {
        Dog& dog = dynamic_cast<Dog&>(ref);  // throws std::bad_cast
        (void)dog;
    } catch (const std::bad_cast& e) {
        std::cerr << e.what() << std::endl;  // std::bad_cast
    }

    return 0;
}
```

## Related Errors

- [std::bad_typeid]({{< relref "/languages/cpp/bad-typeid" >}}) — `typeid` on a null pointer
- [std::bad_any_cast]({{< relref "/languages/cpp/any-cast-error" >}}) — invalid `std::any` cast
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong `std::variant` alternative

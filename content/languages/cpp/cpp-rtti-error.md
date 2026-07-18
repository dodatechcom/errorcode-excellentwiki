---
title: "[Solution] C++ RTTI Error — How to Fix"
description: "Fix C++ RTTI errors including typeid failures, bad_typeid exceptions, and dynamic_cast returns in hierarchies without virtual destructors."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime", "compile-time"]
weight: 5
comments: true
---

# [Solution] C++ RTTI Error — How to Fix

Runtime Type Information (RTTI) in C++ can fail when using `typeid` on polymorphic types without virtual destructors, when `dynamic_cast` returns null on invalid conversions, or when RTTI is disabled in the build configuration.

## Why It Happens

RTTI errors occur when classes lack virtual destructors preventing polymorphic type identification, when `dynamic_cast` is used on non-polymorphic types, when RTTI is disabled via compiler flags like `-fno-rtti`, or when typeid is called on prvalue types that don't propagate expected type info.

## Common Error Messages

1. `error: 'dynamic_cast' not valid — type is not polymorphic`
2. `error: RTTI disabled — cannot use typeid`
3. `std::bad_typeid: typeid of polymorphic type with NULL pointer`
4. `error: cannot use 'typeid' on incomplete type`

## How to Fix It

### Fix 1: Add Virtual Destructors for Polymorphic Types

```cpp
#include <iostream>
#include <typeinfo>

class Base {
public:
    // WRONG — missing virtual destructor
    // ~Base() {}  // not polymorphic

    // CORRECT — virtual destructor makes type polymorphic
    virtual ~Base() = default;
    virtual void identify() const {}
};

class Derived : public Base {
public:
    void identify() const override { std::cout << "Derived\n"; }
};

int main() {
    Base* ptr = new Derived();
    std::cout << typeid(*ptr).name() << "\n";  // Derived
    delete ptr;
    return 0;
}
```

### Fix 2: Handle dynamic_cast Failures

```cpp
#include <iostream>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void specific() { std::cout << "Derived specific\n"; }
};

class Other : public Base {};

int main() {
    Base* base = new Other();

    // CORRECT — check dynamic_cast result
    Derived* d = dynamic_cast<Derived*>(base);
    if (d) {
        d->specific();
    } else {
        std::cout << "Cast failed — wrong type\n";
    }

    delete base;
    return 0;
}
```

### Fix 3: Enable RTTI in Build Configuration

```cpp
// Compile with RTTI enabled:
// g++ -frtti file.cpp
// NOT: g++ -fno-rtti file.cpp

#include <iostream>
#include <typeinfo>

class Animal {
public:
    virtual ~Animal() = default;
};

class Dog : public Animal {};

int main() {
    Dog d;
    Animal& ref = d;
    // This requires RTTI to be enabled
    std::cout << "Type: " << typeid(ref).name() << "\n";
    std::cout << "Is Dog: " << (typeid(ref) == typeid(Dog)) << "\n";
    return 0;
}
```

### Fix 4: Usetypeid Safely with Pointers

```cpp
#include <iostream>
#include <typeinfo>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {};

int main() {
    Derived* valid = new Derived();
    Derived* null_ptr = nullptr;

    // CORRECT — check for null before typeid
    if (valid) {
        std::cout << typeid(*valid).name() << "\n";
    }

    // WRONG — dereferencing null in typeid is UB
    // typeid(*null_ptr);  // undefined behavior

    // CORRECT — use pointer form
    std::cout << typeid(*valid).name() << "\n";

    delete valid;
    return 0;
}
```

## Common Scenarios

- **Missing virtual dtor**: Non-polymorphic classes can't use `typeid` on references correctly.
- **RTTI disabled**: Libraries built with `-fno-rtti` break dynamic_cast and typeid at link time.
- **Null pointer dereference**: Calling `typeid(*ptr)` where `ptr` is null causes `std::bad_typeid`.

## Prevent It

1. Always add virtual destructors to base classes that will be used polymorphically.
2. Check `dynamic_cast` results before using the returned pointer.
3. Ensure all translation units use consistent RTTI settings — no mixing of `-frtti` and `-fno-rtti`.

## Related Errors

- [Bad typeid]({{< relref "/languages/cpp/bad-typeid-2" >}}) — typeid failures.
- [Bad cast]({{< relref "/languages/cpp/bad-cast-dynamic" >}}) — dynamic_cast failures.
- [Bad variant access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong variant type.

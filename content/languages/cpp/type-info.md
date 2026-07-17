---
title: "[Solution] C++ std::type_info — RTTI Usage Fix"
description: "Fix C++ std::type_info and typeid issues including RTTI disabled, type comparison errors, and name() portability problems."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::type_info — RTTI Usage Fix

`std::type_info` provides runtime type information through `typeid`. Issues arise when RTTI is disabled by the compiler (`-fno-rtti`), when `typeid` is used on null pointers, or when `name()` output is not portable across compilers.

## Why type_info Issues Occur

Common causes include compiler flags disabling RTTI (`-fno-rtti`), using `typeid` on a dereferenced null polymorphic pointer, relying on `name()` output which is compiler-specific, and comparing `type_info` objects across shared library boundaries.

## Wrong: Using typeid With RTTI Disabled

```cpp
// WRONG — compilation error if RTTI is disabled
// Compile with: g++ -fno-rtti
#include <iostream>
#include <typeinfo>

class Base { public: virtual ~Base() = default; };
class Derived : public Base {};

int main() {
    Derived d;
    Base& ref = d;
    std::cout << typeid(ref).name() << std::endl;  // error with -fno-rtti
    return 0;
}
```

## Correct: Use typeid With RTTI Enabled

```cpp
// CORRECT — ensure RTTI is enabled (default)
#include <iostream>
#include <typeinfo>

class Base { public: virtual ~Base() = default; };
class Derived : public Base {};

int main() {
    Derived d;
    Base& ref = d;

    std::cout << "Type: " << typeid(ref).name() << std::endl;

    if (typeid(ref) == typeid(Derived)) {
        std::cout << "ref is Derived" << std::endl;
    }
    return 0;
}
```

## Use Virtual Function for Portable Type Names

```cpp
// CORRECT — custom type_name for portable output
#include <iostream>
#include <string>

class Base {
public:
    virtual ~Base() = default;
    virtual std::string type_name() const = 0;
};

class Derived : public Base {
public:
    std::string type_name() const override { return "Derived"; }
};

int main() {
    Derived d;
    Base& ref = d;
    std::cout << "Type: " << ref.type_name() << std::endl;
    return 0;
}
```

## Safe Type Comparison

```cpp
// CORRECT — portable type comparison
#include <iostream>
#include <typeinfo>

class Animal { public: virtual ~Animal() = default; };
class Dog : public Animal {};
class Cat : public Animal {};

void identify(Animal* a) {
    if (!a) {
        std::cout << "null" << std::endl;
        return;
    }

    if (typeid(*a) == typeid(Dog)) {
        std::cout << "It's a Dog" << std::endl;
    } else if (typeid(*a) == typeid(Cat)) {
        std::cout << "It's a Cat" << std::endl;
    } else {
        std::cout << "Unknown animal" << std::endl;
    }
}

int main() {
    Dog d;
    Cat c;
    identify(&d);
    identify(&c);
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Ensure RTTI is enabled | When using `typeid` or `dynamic_cast` |
| Use virtual functions for type names | When portable type names are needed |
| Compare types with `typeid` | When checking exact type matches |
| Prefer `dynamic_cast` over `typeid` | When you need a typed pointer/reference |

## Related Errors

- [std::bad_typeid]({{< relref "/languages/cpp/bad-typeid" >}}) — typeid on null pointer.
- [std::bad_cast]({{< relref "/languages/cpp/bad-cast" >}}) — failed dynamic_cast.
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type on variant.

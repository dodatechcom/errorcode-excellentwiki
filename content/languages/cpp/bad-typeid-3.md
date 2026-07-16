---
title: "[Solution] C++ std::bad_typeid — Typeid of NULL Pointer Fix"
description: "Fix C++ std::bad_typeid when typeid is called on a null pointer. Understand RTTI requirements and handle polymorphic types safely."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bad-typeid", "typeid", "rtti", "null-pointer", "typeinfo"]
weight: 5
---

# [Solution] C++ std::bad_typeid — Typeid of NULL Pointer Fix

A `std::bad_typeid` (sometimes reported as `std::bad_typeid: typeid of NULL`) is thrown when `typeid()` is called on a dereferenced null pointer. In C++, calling `typeid(*ptr)` when `ptr` is `nullptr` throws `std::bad_typeid` from `<typeinfo>`.

## Common Causes

- **Passing a null pointer to typeid** — `typeid(*ptr)` where `ptr == nullptr`
- **Forgetting to check for null before RTTI operations** — common with polymorphic hierarchies
- **Using typeid on a pointer instead of a dereferenced object** — `typeid(ptr)` gives type info, `typeid(*ptr)` gives object info
- **Returning null from a factory function and immediately calling typeid**

## How to Fix

### Fix 1: Always check for null before using typeid

```cpp
#include <iostream>
#include <typeinfo>

class Base {
public:
    virtual ~Base() = default;
    virtual void identify() { std::cout << "Base" << std::endl; }
};

class Derived : public Base {
public:
    void identify() override { std::cout << "Derived" << std::endl; }
};

void print_type(Base* ptr) {
    if (ptr == nullptr) {
        std::cerr << "ptr is null" << std::endl;
        return;
    }
    std::cout << "Type: " << typeid(*ptr).name() << std::endl;
}

int main() {
    Derived d;
    print_type(&d);    // OK
    print_type(nullptr); // handled safely
    return 0;
}
```

### Fix 2: Use pointer typeid (no exception) when possible

```cpp
#include <iostream>
#include <typeinfo>

int main() {
    Base* ptr = nullptr;

    // This is safe — typeid on the pointer itself never throws
    std::cout << "Pointer type: " << typeid(ptr).name() << std::endl;

    // This would throw if ptr is null
    // std::cout << typeid(*ptr).name() << std::endl;
    return 0;
}
```

### Fix 3: Use dynamic_cast which returns nullptr instead of throwing

```cpp
#include <iostream>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {};

void process(Base* ptr) {
    if (auto* d = dynamic_cast<Derived*>(ptr)) {
        std::cout << "It's a Derived" << std::endl;
    } else {
        std::cout << "Not a Derived or null" << std::endl;
    }
}

int main() {
    process(nullptr);  // safe — prints "Not a Derived or null"
    return 0;
}
```

## Examples

```cpp
#include <iostream>
#include <typeinfo>

class Base { public: virtual ~Base() = default; };
class Derived : public Base {};

int main() {
    /* This throws std::bad_typeid */
    try {
        Base* null_ptr = nullptr;
        const std::type_info& ti = typeid(*null_ptr);  // throws!
        std::cout << ti.name() << std::endl;
    } catch (const std::bad_typeid& e) {
        std::cerr << e.what() << std::endl;
    }

    return 0;
}
```

## Related Errors

- [std::bad_cast]({{< relref "/languages/cpp/bad-cast-3" >}}) — failed reference dynamic_cast
- [std::bad_any_cast]({{< relref "/languages/cpp/any-cast-error" >}}) — invalid std::any cast
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong variant alternative

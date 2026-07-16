---
title: "[Solution] C++ std::bad_typeid — Null Pointer Type ID Fix"
description: "Fix C++ std::bad_typeid when using typeid on null pointers. Handle RTTI safely and validate pointers before type identification."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["bad-typeid", "typeid", "rtti", "exception"]
weight: 50
---

# [Solution] C++ std::bad_typeid — Null Pointer Type ID Fix

A `std::bad_typeid` is thrown when you use `typeid` on a dereferenced null pointer in a polymorphic context. If the expression is a null pointer dereference and the type has virtual functions (polymorphic), `typeid` throws `std::bad_typeid`. For non-polymorphic types or value types, `typeid` does not throw even if the expression is null.

## Why std::bad_typeid Occurs

Common causes include dereferencing a null pointer in `typeid()` for polymorphic types, passing a null pointer with virtual functions to `typeid`, and incorrect casting that results in null pointers before type checking.

## Wrong: Using typeid on Null Polymorphic Pointer

```cpp
// WRONG — throws std::bad_typeid
#include <typeinfo>
#include <iostream>

class Base {
public:
    virtual ~Base() = default;
};

int main() {
    Base* ptr = nullptr;
    const std::type_info& ti = typeid(*ptr);  // throws std::bad_typeid
    std::cout << ti.name() << std::endl;
    return 0;
}
```

## Correct: Check for Null Before Using typeid

```cpp
// CORRECT — verify pointer is not null
#include <typeinfo>
#include <iostream>

class Base {
public:
    virtual ~Base() = default;
};

int main() {
    Base* ptr = nullptr;

    if (ptr != nullptr) {
        const std::type_info& ti = typeid(*ptr);
        std::cout << "Type: " << ti.name() << std::endl;
    } else {
        std::cerr << "Cannot identify type of null pointer" << std::endl;
    }
    return 0;
}
```

## Safe Dynamic Cast with typeid Check

```cpp
// CORRECT — use dynamic_cast which returns nullptr on failure
#include <typeinfo>
#include <iostream>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void specific() { std::cout << "Derived specific" << std::endl; }
};

void process(Base* obj) {
    if (obj == nullptr) {
        std::cerr << "Null pointer" << std::endl;
        return;
    }

    // dynamic_cast is safer than typeid for type checking
    if (auto* derived = dynamic_cast<Derived*>(obj)) {
        derived->specific();
    } else {
        std::cout << "Type: " << typeid(*obj).name() << std::endl;
    }
}

int main() {
    Derived d;
    process(&d);
    process(nullptr);
    return 0;
}
```

## Using typeid Safely with Smart Pointers

```cpp
// CORRECT — check smart pointer before dereferencing
#include <memory>
#include <typeinfo>
#include <iostream>

class Animal {
public:
    virtual ~Animal() = default;
    virtual void speak() = 0;
};

class Dog : public Animal {
public:
    void speak() override { std::cout << "Woof" << std::endl; }
};

void identify(const std::unique_ptr<Animal>& animal) {
    if (!animal) {
        std::cerr << "Null animal" << std::endl;
        return;
    }
    std::cout << "Type: " << typeid(*animal).name() << std::endl;
}

int main() {
    std::unique_ptr<Animal> dog = std::make_unique<Dog>();
    identify(dog);

    std::unique_ptr<Animal> empty;
    identify(empty);
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Check pointer for null before `typeid(*ptr)` | Always with polymorphic pointers |
| Use `dynamic_cast` for type checking | When you need safe downcasting |
| Check smart pointers before dereferencing | When using `typeid` on managed objects |
| Avoid `typeid` on raw pointers | Prefer smart pointers for safety |

## Related Errors

- [std::bad_cast]({{< relref "/languages/cpp/badany-cast" >}}) — failed `dynamic_cast`.
- [std::bad_weak_ptr]({{< relref "/languages/cpp/badweak-ptr" >}}) — expired `weak_ptr` lock.
- [std::bad_function_call]({{< relref "/languages/cpp/badfunctioncall" >}}) — invoking an empty callable.

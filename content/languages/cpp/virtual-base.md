---
title: "[Solution] C++ Pure Virtual Function Called — Virtual Base Fix"
description: "Fix C++ pure virtual function called error during construction and destruction. Learn safe virtual dispatch patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
tags: ["pure-virtual", "virtual-function", "construction", "destruction"]
weight: 5
---

# [Solution] C++ Pure Virtual Function Called — Virtual Base Fix

A "pure virtual function called" error occurs when a virtual function is dispatched during object construction or destruction, and the most-derived class has not yet been constructed (or has already been destroyed). The runtime calls `std::terminate()` — this is not an exception you can catch.

## Why Pure Virtual Function Called Occurs

Common causes include calling a virtual function from a base class constructor or destructor, storing `this` pointer during construction and using it later, and destroying derived objects through base class pointers without virtual destructors.

## Wrong: Calling Virtual Function From Constructor

```cpp
// WRONG — calls pure virtual function during construction
#include <iostream>

class Base {
public:
    Base() { init(); }  // virtual dispatch to derived — UB
    virtual void init() = 0;
    virtual ~Base() = default;
};

class Derived : public Base {
    int data_;
public:
    void init() override { data_ = 42; }
    int data() const { return data_; }
};

int main() {
    Derived d;  // terminates
    return 0;
}
```

## Correct: Avoid Virtual Calls During Construction

```cpp
// CORRECT — do not call virtual functions in constructors
#include <iostream>

class Base {
protected:
    int data_ = 0;

public:
    virtual ~Base() = default;

    int data() const { return data_; }
};

class Derived : public Base {
public:
    Derived() { data_ = 42; }  // direct member init — safe
};

int main() {
    Derived d;
    std::cout << "Data: " << d.data() << std::endl;
    return 0;
}
```

## Use Two-Phase Initialization

```cpp
// CORRECT — separate construction from initialization
#include <iostream>

class Base {
public:
    virtual ~Base() = default;
    virtual void init() = 0;
};

class Derived : public Base {
    int data_ = 0;
public:
    void init() override { data_ = 42; }
    int data() const { return data_; }
};

int main() {
    Derived d;
    d.init();  // after construction — safe
    std::cout << "Data: " << d.data() << std::endl;
    return 0;
}
```

## Use CRTP to Avoid Virtual Dispatch

```cpp
// CORRECT — CRTP avoids virtual dispatch entirely
#include <iostream>

template <typename Derived>
class Base {
public:
    void interface() {
        static_cast<Derived*>(this)->implementation();
    }
};

class MyClass : public Base<MyClass> {
public:
    void implementation() { std::cout << "MyClass implementation" << std::endl; }
};

int main() {
    MyClass obj;
    obj.interface();
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Never call virtual functions in constructors/destructors | Always |
| Use two-phase initialization | When base class needs derived data during init |
| Use CRTP for static polymorphism | When virtual dispatch overhead is unwanted |
| Use factory functions | When construction requires virtual dispatch |

## Related Errors

- [std::bad_cast]({{< relref "/languages/cpp/bad-cast" >}}) — failed dynamic_cast.
- [std::bad_typeid]({{< relref "/languages/cpp/bad-typeid" >}}) — typeid on null pointer.
- [std::bad_variant_access]({{< relref "/languages/cpp/bad-variant-access" >}}) — wrong type on variant.

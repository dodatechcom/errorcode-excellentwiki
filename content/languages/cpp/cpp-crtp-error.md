---
title: "[Solution] C++ CRTP Error — How to Fix"
description: "Fix C++ Curiously Recurring Template Pattern errors including incomplete type issues, missing static polymorphism, and CRTP diamond problems."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time"]
weight: 5
comments: true
---

# [Solution] C++ CRTP Error — How to Fix

The Curiously Recurring Template Pattern (CRTP) embeds static polymorphism in C++ but frequently produces errors from incomplete types, incorrect template parameter usage, and failures when combining with virtual inheritance.

## Why It Happens

CRTP errors occur when the derived class isn't fully defined when the base class template is instantiated, when static members are incorrectly shared across specializations, when CRTP is combined with virtual inheritance creating ambiguity, or when forward declarations don't match the CRTP parameter.

## Common Error Messages

1. `error: invalid use of incomplete type 'class Derived'`
2. `error: no member named 'derived' in 'Base<Derived>'`
3. `error: ambiguous base class for 'Derived'`
4. `error: template parameter 'D' is not used in partial specialization`

## How to Fix It

### Fix 1: Ensure Derived Class Is Complete

```cpp
#include <iostream>

// CORRECT — forward declare, define after Derived
template <typename Derived>
class Base {
public:
    void interface() {
        static_cast<Derived*>(this)->implementation();
    }
};

class Derived : public Base<Derived> {
public:
    void implementation() {
        std::cout << "Derived implementation\n";
    }
};

int main() {
    Derived d;
    d.interface();  // calls Derived::implementation
    return 0;
}
```

### Fix 2: Use CRTP with Static polymorphism Correctly

```cpp
#include <iostream>
#include <string>

template <typename Derived>
class Printable {
public:
    void print() const {
        std::cout << static_cast<const Derived*>(this)->toString() << "\n";
    }
};

class Point : public Printable<Point> {
    double x, y;
public:
    Point(double x, double y) : x(x), y(y) {}
    std::string toString() const {
        return "(" + std::to_string(x) + ", " + std::to_string(y) + ")";
    }
};

int main() {
    Point p(3.0, 4.0);
    p.print();  // Output: (3.000000, 4.000000)
    return 0;
}
```

### Fix 3: Avoid Static Member Conflicts

```cpp
#include <iostream>

template <typename Derived>
class Counter {
    static int count;
public:
    Counter() { ++count; }
    static int getCount() { return count; }
};

// CORRECT — define static member per specialization
template <typename Derived>
int Counter<Derived>::count = 0;

class A : public Counter<A> {};
class B : public Counter<B> {};

int main() {
    A a1, a2;
    B b1;
    std::cout << "A count: " << A::getCount() << "\n";  // 2
    std::cout << "B count: " << B::getCount() << "\n";  // 1
    return 0;
}
```

### Fix 4: Handle CRTP with Multiple Bases

```cpp
#include <iostream>

template <typename Derived>
class Printable {
public:
    void print() const {
        std::cout << "Printable\n";
    }
};

template <typename Derived>
class Serializable {
public:
    void serialize() const {
        std::cout << "Serializable\n";
    }
};

class Widget : public Printable<Widget>, public Serializable<Widget> {};

int main() {
    Widget w;
    w.print();
    w.serialize();
    return 0;
}
```

## Common Scenarios

- **Incomplete type**: Calling CRTP methods before the derived class is fully defined fails.
- **Static member sharing**: All CRTP instantiations with different `Derived` types get separate static members.
- **Diamond inheritance**: Combining CRTP with multiple CRTP bases requires careful handling.

## Prevent It

1. Always define the complete derived class before using CRTP base class methods.
2. Never rely on shared static state across CRTP specializations — each `Derived` gets its own.
3. Prefer C++20 concepts and `if constexpr` over CRTP for simpler static polymorphism.

## Related Errors

- [SFINAE error]({{< relref "/languages/cpp/cpp-sfinae-error" >}}) — substitution failures.
- [Template instantiation]({{< relref "/languages/cpp/template-error" >}}) — template failures.
- [Virtual inheritance]({{< relref "/languages/cpp/cpp-virtual-inheritance-error" >}}) — virtual base issues.

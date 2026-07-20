---
title: "[Solution] C++ Reference Collapsing Error — Fix"
description: "Fix reference collapsing errors by using std::forward correctly, understanding T&& vs const T&, and mastering universal references."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 913
---

# C++ Reference Collapsing Error — Fix

Reference collapsing occurs when template type deduction produces references to references (e.g., `int& &&`). C++ resolves these using collapsing rules: `T& &&` becomes `T&`, `T&& &` becomes `T&`, and `T&& &&` becomes `T&&`. Errors arise when you misunderstand these rules or fail to forward correctly.

## Common Causes

```cpp
// Cause 1: Forgetting std::forward in universal reference
template <typename T>
void wrapper(T&& arg) {
    // WRONG: always creates lvalue reference
    process(arg);  // arg is always an lvalue here, even if arg was an rvalue

    // CORRECT: forward preserves value category
    process(std::forward<T>(arg));
}
```

```cpp
// Cause 2: Confusing universal reference with rvalue reference
template <typename T>
void func(T&& param);  // universal reference (deduced T)

void func(int&& param);  // rvalue reference (not deduced)

// The rules differ:
// Universal reference: can bind to lvalues or rvalues
// Rvalue reference: can only bind to rvalues
```

```cpp
// Cause 3: Reference collapsing with const
template <typename T>
void wrapper(T&& arg) {
    // If T = int& (lvalue passed to universal reference):
    // T&& = int& && = int&  (collapses to lvalue ref)
    // If T = int (rvalue passed):
    // T&& = int&&  (rvalue ref)
}
```

```cpp
// Cause 4: Misusing auto&&
int x = 42;
auto&& ref1 = x;       // ref1 is int& (lvalue ref, because x is lvalue)
auto&& ref2 = 42;      // ref2 is int&& (rvalue ref)
// But if you pass ref1 to another template, the reference category may change
```

```cpp
// Cause 5: Forwards in multiple layers
template <typename T>
void outer(T&& arg) {
    inner(std::forward<T>(arg));  // correct
    inner(arg);  // WRONG — arg is always lvalue in outer's body
}
```

## How to Fix

### Fix 1: Use std::forward to Preserve Value Category

```cpp
#include <utility>
#include <string>

void process(std::string& s) { s += " lvalue"; }
void process(std::string&& s) { s += " rvalue"; }

template <typename T>
void wrapper(T&& arg) {
    // std::forward<T>(arg) preserves:
    // - lvalue reference if arg was an lvalue
    // - rvalue reference if arg was an rvalue
    process(std::forward<T>(arg));
}

int main() {
    std::string s = "hello";
    wrapper(s);           // calls process(string&)
    wrapper(std::move(s)); // calls process(string&&)
    return 0;
}
```

### Fix 2: Understand T&& vs const T&

```cpp
#include <string>

// Universal reference (deduced T) — binds to anything
template <typename T>
void universal(T&& arg) {}

// Const lvalue reference — binds to anything but can't modify
template <typename T>
void const_ref(const T& arg) {}

// Rvalue reference — binds only to rvalues
template <typename T>
void rvalue_ref(T&& arg) requires (!std::is_reference_v<T>) {}

int main() {
    std::string s = "hello";

    universal(s);            // T = string&, arg = string& (lvalue)
    universal(std::move(s)); // T = string, arg = string&& (rvalue)

    const_ref(s);            // const string&
    const_ref(std::move(s)); // const string& (rvalue binds to const ref)

    // rvalue_ref(s);  // ERROR: can't bind lvalue to rvalue reference
    rvalue_ref(std::move(s)); // OK: rvalue
    return 0;
}
```

### Fix 3: Use Perfect Forwarding Pattern

```cpp
#include <utility>
#include <string>
#include <iostream>

class Widget {
    std::string name_;
public:
    // Perfect forwarding constructor
    template <typename T>
    explicit Widget(T&& name) : name_(std::forward<T>(name)) {}

    // Without forwarding: always copies
    // Widget(const std::string& name) : name_(name) {}
    // Widget(std::string&& name) : name_(std::move(name)) {}
};

int main() {
    Widget w1("hello");          // constructs string from const char*
    std::string s = "world";
    Widget w2(s);                // copies s
    Widget w3(std::move(s));     // moves s

    return 0;
}
```

### Fix 4: Use auto&& for Universal References

```cpp
#include <iostream>
#include <string>

int main() {
    std::string s = "hello";

    // auto&& is a universal reference
    auto&& ref1 = s;            // ref1 is string& (lvalue ref)
    auto&& ref2 = std::move(s); // ref2 is string&& (rvalue ref)

    // Useful in range-for to handle any value category
    for (auto&& item : {1, 2, 3}) {
        std::cout << item << " ";  // item is const int&
    }

    return 0;
}
```

### Fix 5: Forward Through Multiple Layers

```cpp
#include <utility>
#include <string>

void inner(std::string& s) { s += " inner lvalue"; }
void inner(std::string&& s) { s += " inner rvalue"; }

template <typename T>
void middle(T&& arg) {
    inner(std::forward<T>(arg));  // forward, not just arg
}

template <typename T>
void outer(T&& arg) {
    middle(std::forward<T>(arg));  // forward again
}

int main() {
    std::string s = "hello";
    outer(s);              // inner receives lvalue
    outer(std::move(s));   // inner receives rvalue
    return 0;
}
```

## Examples

```cpp
// Real-world: perfect forwarding factory
#include <utility>
#include <string>
#include <memory>
#include <iostream>

class Connection {
    std::string endpoint_;
    int timeout_;
public:
    Connection(std::string ep, int t)
        : endpoint_(std::move(ep)), timeout_(t) {}

    void connect() const {
        std::cout << "Connecting to " << endpoint_
                  << " with timeout " << timeout_ << "s" << std::endl;
    }
};

template <typename... Args>
std::unique_ptr<Connection> make_connection(Args&&... args) {
    return std::make_unique<Connection>(std::forward<Args>(args)...);
}

int main() {
    auto conn1 = make_connection("localhost:8080", 30);
    std::string host = "remote:443";
    auto conn2 = make_connection(std::move(host), 60);

    conn1->connect();
    conn2->connect();
    return 0;
}
```

## Related Errors

- [Forwarding reference error]({{< relref "/languages/cpp/forwarding-reference-error" >}}) — template argument deduction failure.
- [std::move on const]({{< relref "/languages/cpp/std-move-const-error" >}}) — moving from const objects.
- [Use after move]({{< relref "/languages/cpp/use-after-move" >}}) — accessing moved-from objects.

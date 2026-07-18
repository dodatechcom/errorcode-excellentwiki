---
title: "[Solution] C++ Type Erasure Error — How to Fix"
description: "Fix C++ type erasure errors including slicing, undefined behavior in virtual dispatch, and incorrect use of std::function and std::any."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time", "runtime"]
weight: 5
comments: true
---

# [Solution] C++ Type Erasure Error — How to Fix

Type erasure in C++ hides concrete types behind abstract interfaces, but incorrect implementations lead to object slicing, undefined behavior from dangling pointers, and failure to preserve value semantics across erasure boundaries.

## Why It Happens

Type erasure errors occur when objects are sliced during copy into erased containers, when the erased wrapper doesn't preserve move semantics, when internal storage uses wrong allocation strategies for large objects, or when the virtual dispatch table doesn't match the concrete type's behavior.

## Common Error Messages

1. `error: use of deleted function 'operator='`
2. `runtime error: type mismatch in erased function call`
3. `error: object sliced during type erasure`
4. `error: incomplete type used in type-erased wrapper`

## How to Fix It

### Fix 1: Avoid Object Slicing with Proper Erasure

```cpp
#include <functional>
#include <iostream>
#include <memory>

struct Base {
    virtual void print() const = 0;
    virtual ~Base() = default;
};

struct Derived : Base {
    int value;
    Derived(int v) : value(v) {}
    void print() const override { std::cout << "Derived: " << value << "\n"; }
};

int main() {
    // WRONG — slicing occurs
    // Base b = Derived(42);  // slices Derived

    // CORRECT — use type erasure via std::function
    std::function<void()> func = [obj = Derived(42)]() {
        obj.print();
    };
    func();

    return 0;
}
```

### Fix 2: Use unique_ptr for Polymorphic Type Erasure

```cpp
#include <memory>
#include <iostream>
#include <vector>

struct Shape {
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

struct Circle : Shape {
    double r;
    Circle(double r) : r(r) {}
    double area() const override { return 3.14159 * r * r; }
};

int main() {
    // CORRECT — ownership with unique_ptr preserves polymorphism
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(5.0));

    for (const auto& s : shapes) {
        std::cout << "Area: " << s->area() << "\n";
    }
    return 0;
}
```

### Fix 3: Implement a Simple Type-Erased Wrapper

```cpp
#include <memory>
#include <iostream>
#include <utility>

class AnyFunction {
    struct Concept {
        virtual ~Concept() = default;
        virtual void call() = 0;
    };

    template <typename F>
    struct Model : Concept {
        F func;
        Model(F f) : func(std::move(f)) {}
        void call() override { func(); }
    };

    std::unique_ptr<Concept> impl_;

public:
    template <typename F>
    AnyFunction(F f) : impl_(std::make_unique<Model<F>>(std::move(f))) {}

    void operator()() { if (impl_) impl_->call(); }
};

int main() {
    AnyFunction f = []() { std::cout << "Hello from type erasure\n"; };
    f();
    return 0;
}
```

### Fix 4: Preserve Const and Reference Qualifiers

```cpp
#include <iostream>
#include <functional>

void process(const std::function<void(const int&)>& func) {
    int val = 42;
    func(val);  // passes const reference correctly
}

int main() {
    process([](const int& v) {
        std::cout << "Value: " << v << "\n";
    });
    return 0;
}
```

## Common Scenarios

- **Object slicing**: Copying derived objects into base-typed erased containers loses derived data.
- **Dangling captures**: Lambda captures in type-erased wrappers may dangle if the captured object is destroyed first.
- **Small buffer optimization**: Large objects may not fit in small-buffer-optimized type erasure, causing heap allocation.

## Prevent It

1. Use `std::unique_ptr` or `std::shared_ptr` for polymorphic type erasure instead of raw copies.
2. Never slice objects — always use pointers or reference semantics.
3. Test type-erased wrappers with both small and large types to verify storage strategy.

## Related Errors

- [Bad cast]({{< relref "/languages/cpp/bad-cast-dynamic" >}}) — failed dynamic_cast.
- [Bad function call]({{< relref "/languages/cpp/bad-function-call" >}}) — null function invocation.
- [Bad any cast]({{< relref "/languages/cpp/any-cast-error" >}}) — std::any type mismatch.

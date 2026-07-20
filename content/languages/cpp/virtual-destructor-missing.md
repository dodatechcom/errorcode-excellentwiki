---
title: "[Solution] C++ Missing Virtual Destructor — Fix"
description: "Fix missing virtual destructor errors by adding virtual destructors to polymorphic base classes, using final, and following best practices."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 931
---

# C++ Missing Virtual Destructor — Fix

When you delete a derived class object through a base class pointer and the base class lacks a virtual destructor, the derived class's destructor is never called. This causes resource leaks, incomplete cleanup, and undefined behavior. The fix is to add a virtual destructor to any class used polymorphically.

## Common Causes

```cpp
// Cause 1: Deleting derived through base without virtual destructor
#include <iostream>

class Base {
public:
    ~Base() { std::cout << "Base destroyed" << std::endl; }  // NOT virtual
};

class Derived : public Base {
    int* data_;
public:
    Derived() : data_(new int[100]) {}
    ~Derived() { delete[] data_; std::cout << "Derived destroyed" << std::endl; }
};

int main() {
    Base* ptr = new Derived();
    delete ptr;  // only Base destructor called — Derived::data_ leaked
    return 0;
}
```

```cpp
// Cause 2: Polymorphic class without virtual destructor
#include <string>

class Animal {
    std::string name_;
public:
    Animal(std::string n) : name_(std::move(n)) {}
    virtual std::string speak() const = 0;
    // Missing: virtual ~Animal() = default;
};

class Dog : public Animal {
public:
    Dog(std::string n) : Animal(std::move(n)) {}
    std::string speak() const override { return "Woof"; }
};

void adopt(Animal* a) {
    delete a;  // undefined behavior — no virtual destructor
}
```

```cpp
// Cause 3: Container of base pointers without virtual destructor
#include <vector>
#include <memory>

class Shape {
public:
    virtual void draw() const = 0;
    // Missing virtual destructor
};

class Circle : public Shape {
public:
    void draw() const override {}
};

int main() {
    std::vector<Shape*> shapes;
    shapes.push_back(new Circle());
    for (auto s : shapes) delete s;  // UB — Shape has no virtual destructor
    return 0;
}
```

```cpp
// Cause 4: Base class used in dynamic_cast but no virtual destructor
class Base {
    // virtual functions but no virtual destructor
    virtual void method() {}
};

class Derived : public Base {
    void method() override {}
};

void process(Base* b) {
    if (auto* d = dynamic_cast<Derived*>(b)) {
        // dynamic_cast works, but delete b is UB without virtual dtor
    }
}
```

```cpp
// Cause 5: Inherited from standard library class without virtual dtor
// This is actually fine for standard library, but custom base classes need it
class MyWidget {
public:
    virtual void render() = 0;
    // Must have virtual destructor
};
```

## How to Fix

### Fix 1: Add Virtual Destructor to Base Class

```cpp
#include <iostream>

class Base {
public:
    virtual ~Base() { std::cout << "Base destroyed" << std::endl; }
};

class Derived : public Base {
    int* data_;
public:
    Derived() : data_(new int[100]) {}
    ~Derived() override { delete[] data_; std::cout << "Derived destroyed" << std::endl; }
};

int main() {
    Base* ptr = new Derived();
    delete ptr;  // Both destructors called correctly
    return 0;
}
```

### Fix 2: Use = default for Virtual Destructor

```cpp
#include <string>

class Animal {
    std::string name_;
public:
    Animal(std::string n) : name_(std::move(n)) {}
    virtual ~Animal() = default;  // virtual, defaulted
    virtual std::string speak() const = 0;
};

class Dog : public Animal {
public:
    Dog(std::string n) : Animal(std::move(n)) {}
    std::string speak() const override { return "Woof"; }
};
```

### Fix 3: Use final to Prevent Inheritance

```cpp
class NonPolymorphic final {  // final prevents inheritance
    int value_;
public:
    NonPolymorphic(int v) : value_(v) {}
    int get() const { return value_; }
    // No virtual destructor needed — can't be inherited
};

// If you want to mark individual methods as final:
class Base {
public:
    virtual ~Base() = default;
    virtual void method() final {}  // can't be overridden
};
```

### Fix 4: Use Smart Pointers with Virtual Destructors

```cpp
#include <memory>
#include <iostream>

class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
};

class Circle : public Shape {
    double radius_;
public:
    Circle(double r) : radius_(r) {}
    double area() const override { return 3.14159 * radius_ * radius_; }
};

int main() {
    std::unique_ptr<Shape> s = std::make_unique<Circle>(5.0);
    std::cout << s->area() << std::endl;
    // Smart pointer calls virtual destructor correctly
    return 0;
}
```

### Fix 5: Polymorphic Base Class Pattern

```cpp
#include <string>
#include <memory>

// Pattern: any class with virtual functions should have virtual destructor
class AbstractWidget {
public:
    virtual ~AbstractWidget() = default;

    // Pure virtual interface
    virtual void render() const = 0;
    virtual std::string get_type() const = 0;

    // Non-virtual interface (NVI pattern)
    void display() const {
        render();
    }
};

class TextWidget : public AbstractWidget {
    std::string text_;
public:
    TextWidget(std::string t) : text_(std::move(t)) {}
    void render() const override { /* render text */ }
    std::string get_type() const override { return "TextWidget"; }
};
```

## Examples

```cpp
// Real-world: polymorphic factory with virtual destructor
#include <memory>
#include <string>
#include <iostream>
#include <vector>

class Plugin {
public:
    virtual ~Plugin() = default;
    virtual void execute() const = 0;
    virtual std::string name() const = 0;
};

class LoggerPlugin : public Plugin {
public:
    void execute() const override { std::cout << "Logging..." << std::endl; }
    std::string name() const override { return "Logger"; }
};

class AuthPlugin : public Plugin {
public:
    void execute() const override { std::cout << "Authenticating..." << std::endl; }
    std::string name() const override { return "Auth"; }
};

std::unique_ptr<Plugin> create_plugin(const std::string& type) {
    if (type == "logger") return std::make_unique<LoggerPlugin>();
    if (type == "auth") return std::make_unique<AuthPlugin>();
    return nullptr;
}

int main() {
    std::vector<std::unique_ptr<Plugin>> plugins;
    plugins.push_back(create_plugin("logger"));
    plugins.push_back(create_plugin("auth"));

    for (const auto& p : plugins) {
        p->execute();  // safe — virtual destructor ensures proper cleanup
    }
    return 0;
}
```

## Related Errors

- [Object slicing]({{< relref "/languages/cpp/object-slicing" >}}) — losing derived class info through copies.
- [Calling virtual in constructor]({{< relref "/languages/cpp/calling-virtual-in-constructor" >}}) — virtual dispatch in constructors.
- [Diamond inheritance]({{< relref "/languages/cpp/diamond-inheritance" >}}) — ambiguous base class.

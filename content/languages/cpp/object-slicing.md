---
title: "[Solution] C++ Object Slicing — Fix"
description: "Fix object slicing by passing by reference, using pointers, and preventing copying of polymorphic objects."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 932
---

# C++ Object Slicing — Fix

Object slicing occurs when a derived class object is assigned to a base class value (not reference or pointer), causing the derived-specific members to be "sliced off." The result is a plain base class object that loses all polymorphic behavior and derived data.

## Common Causes

```cpp
// Cause 1: Passing by value to a function
#include <iostream>
#include <string>

class Animal {
public:
    std::string name;
    virtual std::string speak() const { return "..."; }
};

class Dog : public Animal {
public:
    std::string breed;
    std::string speak() const override { return "Woof!"; }
};

void print_animal(Animal a) {  // SLICING — Dog becomes Animal
    std::cout << a.speak() << std::endl;
}

int main() {
    Dog d;
    d.name = "Rex";
    d.breed = "Labrador";
    print_animal(d);  // prints "..." not "Woof!" — derived part sliced off
    return 0;
}
```

```cpp
// Cause 2: Storing in base class container by value
#include <vector>
#include <iostream>

class Shape {
public:
    virtual double area() const { return 0; }
};

class Circle : public Shape {
    double radius_;
public:
    Circle(double r) : radius_(r) {}
    double area() const override { return 3.14159 * radius_ * radius_; }
};

int main() {
    std::vector<Shape> shapes;  // SLICING — stores base objects
    shapes.push_back(Circle(5.0));  // Circle sliced to Shape
    std::cout << shapes[0].area() << std::endl;  // prints 0, not 78.54
    return 0;
}
```

```cpp
// Cause 3: Assigning derived to base variable
class Base {
public:
    int base_val;
    virtual void method() { std::cout << "Base" << std::endl; }
};

class Derived : public Base {
public:
    int derived_val;
    void method() override { std::cout << "Derived" << std::endl; }
};

int main() {
    Derived d;
    d.base_val = 1;
    d.derived_val = 2;

    Base b = d;  // SLICING — derived_val is lost
    b.method();  // calls Base::method, not Derived::method
    return 0;
}
```

```cpp
// Cause 4: Returning by value from factory
class Base {
public:
    virtual ~Base() = default;
    virtual int value() const { return 0; }
};

class Derived : public Base {
    int val_;
public:
    Derived(int v) : val_(v) {}
    int value() const override { return val_; }
};

Base create_derived(int v) {  // SLICING on return
    return Derived(v);
}

int main() {
    Base b = create_derived(42);
    std::cout << b.value() << std::endl;  // prints 0, not 42
    return 0;
}
```

```cpp
// Cause 5: Implicit conversion to base
class Window {
public:
    virtual void draw() { std::cout << "draw base" << std::endl; }
};

class Button : public Window {
public:
    void draw() override { std::cout << "draw button" << std::endl; }
};

void render(Window w) {  // implicit conversion slices Button
    w.draw();
}

int main() {
    Button btn;
    render(btn);  // draws "draw base", not "draw button"
    return 0;
}
```

## How to Fix

### Fix 1: Pass by Reference or Pointer

```cpp
#include <iostream>
#include <string>

class Animal {
public:
    std::string name;
    virtual std::string speak() const { return "..."; }
    virtual ~Animal() = default;
};

class Dog : public Animal {
public:
    std::string breed;
    std::string speak() const override { return "Woof!"; }
};

void print_animal(const Animal& a) {  // no slicing — reference
    std::cout << a.name << ": " << a.speak() << std::endl;
}

int main() {
    Dog d;
    d.name = "Rex";
    d.breed = "Labrador";
    print_animal(d);  // prints "Rex: Woof!"
    return 0;
}
```

### Fix 2: Use Polymorphic Pointers or Smart Pointers

```cpp
#include <vector>
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

class Rectangle : public Shape {
    double w_, h_;
public:
    Rectangle(double w, double h) : w_(w), h_(h) {}
    double area() const override { return w_ * h_; }
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(5.0));
    shapes.push_back(std::make_unique<Rectangle>(3.0, 4.0));

    for (const auto& s : shapes) {
        std::cout << s->area() << std::endl;  // polymorphic — no slicing
    }
    return 0;
}
```

### Fix 3: Use a Polymorphic Base Class Container

```cpp
#include <memory>
#include <vector>
#include <iostream>

class Widget {
public:
    virtual ~Widget() = default;
    virtual void render() const = 0;
};

class Label : public Widget {
    std::string text_;
public:
    Label(std::string t) : text_(std::move(t)) {}
    void render() const override { std::cout << "Label: " << text_ << std::endl; }
};

class Button : public Widget {
    std::string label_;
public:
    Button(std::string l) : label_(std::move(l)) {}
    void render() const override { std::cout << "Button: " << label_ << std::endl; }
};

// Accept by reference to prevent slicing
void render_all(const std::vector<std::unique_ptr<Widget>>& widgets) {
    for (const auto& w : widgets) {
        w->render();
    }
}
```

### Fix 4: Return Smart Pointers from Factories

```cpp
#include <memory>
#include <iostream>

class Base {
public:
    virtual ~Base() = default;
    virtual int value() const { return 0; }
};

class Derived : public Base {
    int val_;
public:
    Derived(int v) : val_(v) {}
    int value() const override { return val_; }
};

std::unique_ptr<Base> create_derived(int v) {
    return std::make_unique<Derived>(v);  // no slicing
}

int main() {
    auto b = create_derived(42);
    std::cout << b->value() << std::endl;  // prints 42
    return 0;
}
```

### Fix 5: Prevent Copying with = delete

```cpp
class NonCopyableBase {
public:
    NonCopyableBase() = default;
    NonCopyableBase(const NonCopyableBase&) = delete;
    NonCopyableBase& operator=(const NonCopyableBase&) = delete;
    virtual ~NonCopyableBase() = default;
    virtual void method() = 0;
};

class Derived : public NonCopyableBase {
    int data_;
public:
    Derived(int v) : data_(v) {}
    void method() override {}
};

int main() {
    Derived d(42);
    // NonCopyableBase b = d;  // compile error — slicing prevented
    NonCopyableBase& ref = d;  // OK — no slicing
    ref.method();
    return 0;
}
```

## Examples

```cpp
// Real-world: polymorphic event system without slicing
#include <memory>
#include <vector>
#include <string>
#include <iostream>
#include <functional>

class Event {
public:
    virtual ~Event() = default;
    virtual std::string type() const = 0;
};

class ClickEvent : public Event {
    int x_, y_;
public:
    ClickEvent(int x, int y) : x_(x), y_(y) {}
    std::string type() const override { return "click"; }
    int x() const { return x_; }
    int y() const { return y_; }
};

class KeyEvent : public Event {
    char key_;
public:
    KeyEvent(char k) : key_(k) {}
    std::string type() const override { return "key"; }
    char key() const { return key_; }
};

void dispatch(const Event& event) {  // pass by reference — no slicing
    if (const auto* click = dynamic_cast<const ClickEvent*>(&event)) {
        std::cout << "Click at (" << click->x() << "," << click->y() << ")" << std::endl;
    } else if (const auto* key = dynamic_cast<const KeyEvent*>(&event)) {
        std::cout << "Key: " << key->key() << std::endl;
    }
}
```

## Related Errors

- [Missing virtual destructor]({{< relref "/languages/cpp/virtual-destructor-missing" >}}) — cleanup issues with polymorphism.
- [Calling virtual in constructor]({{< relref "/languages/cpp/calling-virtual-in-constructor" >}}) — virtual dispatch during construction.
- [Diamond inheritance]({{< relref "/languages/cpp/diamond-inheritance" >}}) — ambiguous inheritance.

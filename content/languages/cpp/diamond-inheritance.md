---
title: "[Solution] C++ Diamond Inheritance — Virtual Base Fix"
description: "Fix diamond inheritance with virtual base classes, understand most-derived class initialization, and resolve constructor call ambiguity."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 933
---

# C++ Diamond Inheritance — Virtual Base Fix

The diamond problem occurs when a class inherits from two classes that both inherit from a common base. Without virtual inheritance, the most derived class gets two copies of the base subobject, causing ambiguity and duplicated state. Virtual inheritance ensures only one shared base subobject exists.

## Common Causes

```cpp
// Cause 1: Ambiguous member access without virtual inheritance
#include <iostream>

class Animal {
public:
    int age;
    void eat() { std::cout << "eating" << std::endl; }
};

class Mammal : public Animal {
public:
    void walk() { std::cout << "walking" << std::endl; }
};

class Bird : public Animal {
public:
    void fly() { std::cout << "flying" << std::endl; }
};

class Bat : public Mammal, public Bird {
    // Bat has TWO Animal subobjects — ambiguous
};

int main() {
    Bat b;
    // b.age = 5;        // ERROR: ambiguous — Mammal::age or Bird::age?
    // b.eat();          // ERROR: ambiguous
    b.Mammal::eat();    // must disambiguate
    b.Bird::eat();      // different Animal subobject
    return 0;
}
```

```cpp
// Cause 2: Constructor ambiguity
class Base {
public:
    int value;
    Base() : value(0) {}
    Base(int v) : value(v) {}
};

class Left : public Base {
public:
    Left() : Base(1) {}
};

class Right : public Base {
public:
    Right() : Base(2) {}
};

class Diamond : public Left, public Right {
    // Diamond has two Base subobjects:
    // Left::Base::value == 1
    // Right::Base::value == 2
};

int main() {
    Diamond d;
    // d.value = 10;  // ERROR: ambiguous
    // d.Left::Base::value = 10;   // ok but confusing
    // d.Right::Base::value = 20;  // modifies different subobject
    return 0;
}
```

```cpp
// Cause 3: Slicing with diamond hierarchy
class Base {
public:
    int id;
};

class Left : public Base {};
class Right : public Base {};
class Diamond : public Left, public Right {};

void process(Base& b) {
    b.id = 42;  // which Base subobject?
}

int main() {
    Diamond d;
    process(d);  // ERROR: cannot convert Diamond& to Base& — ambiguous
    return 0;
}
```

```cpp
// Cause 4: dynamic_cast ambiguity
class Base {
public:
    virtual ~Base() = default;
};

class Left : public Base {};
class Right : public Base {};
class Diamond : public Left, public Right {};

int main() {
    Diamond d;
    Base* b = static_cast<Left*>(&d);
    // auto* result = dynamic_cast<Diamond*>(b);  // may have ambiguity issues
    return 0;
}
```

```cpp
// Cause 5: Template diamond
template <typename T>
class BaseT {
public:
    T value;
};

template <typename T>
class LeftT : public BaseT<T> {};

template <typename T>
class RightT : public BaseT<T> {};

template <typename T>
class DiamondT : public LeftT<T>, public RightT<T> {
    // Two copies of BaseT<T>::value
};
```

## How to Fix

### Fix 1: Use Virtual Inheritance

```cpp
#include <iostream>

class Animal {
public:
    int age;
    Animal() : age(0) {}
    virtual ~Animal() = default;
};

class Mammal : public virtual Animal {  // virtual inheritance
public:
    void walk() { std::cout << "walking" << std::endl; }
};

class Bird : public virtual Animal {  // virtual inheritance
public:
    void fly() { std::cout << "flying" << std::endl; }
};

class Bat : public Mammal, public Bird {
    // Only ONE Animal subobject — no ambiguity
};

int main() {
    Bat b;
    b.age = 5;   // unambiguous — single Animal subobject
    b.eat();     // unambiguous
    return 0;
}
```

### Fix 2: Most-Derived Class Initializes Virtual Base

```cpp
#include <iostream>

class Base {
public:
    int value;
    Base() : value(0) { std::cout << "Base()" << std::endl; }
    Base(int v) : value(v) { std::cout << "Base(" << v << ")" << std::endl; }
};

class Left : public virtual Base {
public:
    Left() : Base(1) {}  // ignored for virtual base
};

class Right : public virtual Base {
public:
    Right() : Base(2) {}  // ignored for virtual base
};

class Diamond : public Left, public Right {
public:
    // Most-derived class must initialize virtual base
    Diamond() : Base(42) {}  // THIS constructor runs
};

int main() {
    Diamond d;
    std::cout << d.value << std::endl;  // prints 42
    return 0;
}
```

### Fix 3: Use Interface Pattern to Avoid Diamond

```cpp
#include <iostream>

// Interface-only classes (pure virtual, no data)
class Walkable {
public:
    virtual ~Walkable() = default;
    virtual void walk() = 0;
};

class Flyable {
public:
    virtual ~Flyable() = default;
    virtual void fly() = 0;
};

// Bat implements both interfaces — no diamond
class Bat : public Walkable, public Flyable {
public:
    void walk() override { std::cout << "walking" << std::endl; }
    void fly() override { std::cout << "flying" << std::endl; }
};
```

### Fix 4: Use CRTP to Avoid Runtime Diamond

```cpp
#include <iostream>

// CRTP avoids diamond by using templates instead of inheritance
template <typename Derived>
class Walkable {
public:
    void walk() { static_cast<Derived*>(this)->walk_impl(); }
};

template <typename Derived>
class Flyable {
public:
    void fly() { static_cast<Derived*>(this)->fly_impl(); }
};

class Bat : public Walkable<Bat>, public Flyable<Bat> {
public:
    void walk_impl() { std::cout << "bat walking" << std::endl; }
    void fly_impl() { std::cout << "bat flying" << std::endl; }
};

int main() {
    Bat b;
    b.walk();
    b.fly();
    return 0;
}
```

### Fix 5: Use Composition Over Inheritance

```cpp
#include <iostream>

class WalkBehavior {
public:
    void walk() { std::cout << "walking" << std::endl; }
};

class FlyBehavior {
public:
    void fly() { std::cout << "flying" << std::endl; }
};

// Composition: no diamond problem
class Bat {
    WalkBehavior walk_behavior_;
    FlyBehavior fly_behavior_;
public:
    void walk() { walk_behavior_.walk(); }
    void fly() { fly_behavior_.fly(); }
};
```

## Examples

```cpp
// Real-world: virtual inheritance in a class hierarchy
#include <string>
#include <iostream>

class Person {
protected:
    std::string name_;
public:
    Person(std::string name) : name_(std::move(name)) {}
    virtual ~Person() = default;
    std::string name() const { return name_; }
};

class Student : public virtual Person {
protected:
    int student_id_;
public:
    Person(std::string name, int id)
        : Person(std::move(name)), student_id_(id) {}
};

class Employee : public virtual Person {
protected:
    int employee_id_;
public:
    Employee(std::string name, int id)
        : Person(std::move(name)), employee_id_(id) {}
};

class WorkingStudent : public Student, public Employee {
public:
    // Most-derived class initializes virtual base
    WorkingStudent(std::string name, int sid, int eid)
        : Person(std::move(name)), Student(name, sid), Employee(name, eid) {}
};
```

## Related Errors

- [Missing virtual destructor]({{< relref "/languages/cpp/virtual-destructor-missing" >}}) — cleanup issues with polymorphism.
- [Object slicing]({{< relref "/languages/cpp/object-slicing" >}}) — losing derived class info.
- [Calling virtual in constructor]({{< relref "/languages/cpp/calling-virtual-in-constructor" >}}) — virtual dispatch during construction.

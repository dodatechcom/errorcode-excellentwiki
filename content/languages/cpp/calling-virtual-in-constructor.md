---
title: "[Solution] C++ Calling Virtual Function in Constructor — Fix"
description: "Fix virtual function calls in constructors by using final overrides, separate init methods, or the CRTP pattern."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 935
---

# C++ Calling Virtual Function in Constructor — Fix

When you call a virtual function from a constructor, the virtual dispatch does not work as expected. During base class construction, the derived class does not yet exist, so the base class version of the virtual function is called. This is a common source of bugs where derived class overrides appear to be ignored.

## Common Causes

```cpp
// Cause 1: Calling virtual function in base constructor
#include <iostream>

class Base {
public:
    Base() {
        log();  // calls Base::log, NOT Derived::log — derived doesn't exist yet
    }
    virtual void log() { std::cout << "Base::log" << std::endl; }
};

class Derived : public Base {
public:
    void log() override { std::cout << "Derived::log" << std::endl; }
};

int main() {
    Derived d;  // prints "Base::log", not "Derived::log"
    return 0;
}
```

```cpp
// Cause 2: Using virtual function in initializer list
#include <iostream>

class Widget {
public:
    Widget() : name_(compute_name()) {}  // calls Widget::compute_name
    virtual std::string compute_name() const { return "Widget"; }
    std::string name_;
};

class Button : public Widget {
public:
    std::string compute_name() const override { return "Button"; }
};

int main() {
    Button b;
    std::cout << b.name_ << std::endl;  // prints "Widget", not "Button"
    return 0;
}
```

```cpp
// Cause 3: Virtual dispatch in destructor (reverse problem)
class Base {
public:
    virtual ~Base() {
        cleanup();  // calls Base::cleanup, not Derived::cleanup
    }
    virtual void cleanup() { std::cout << "Base cleanup" << std::endl; }
};

class Derived : public Base {
    int* data_;
public:
    Derived() : data_(new int[100]) {}
    ~Derived() { delete[] data_; }
    void cleanup() override { std::cout << "Derived cleanup" << std::endl; }
};
```

```cpp
// Cause 4: Passing this to a function that uses virtual dispatch
#include <iostream>

class Base {
public:
    Base() {
        register_object(this);  // passing partially constructed object
    }
    virtual void process() { std::cout << "Base::process" << std::endl; }
};

class Derived : public Base {
public:
    void process() override { std::cout << "Derived::process" << std::endl; }
};

void register_object(Base* obj) {
    obj->process();  // undefined behavior — derived part not initialized
}
```

```cpp
// Cause 5: Template method pattern in constructor
class AbstractParser {
public:
    AbstractParser() {
        parse();  // virtual call — calls base version
    }
    virtual void parse() = 0;
};

class JsonParser : public AbstractParser {
public:
    void parse() override { std::cout << "parsing JSON" << std::endl; }
};
```

## How to Fix

### Fix 1: Use Two-Phase Initialization

```cpp
#include <iostream>
#include <string>

class Base {
protected:
    std::string name_;
public:
    Base() : name_("") {}  // don't call virtual in constructor

    void initialize() {
        name_ = compute_name();  // safe — object fully constructed
    }

    virtual std::string compute_name() const { return "Base"; }
};

class Derived : public Base {
public:
    Derived() { initialize(); }  // call after construction
    std::string compute_name() const override { return "Derived"; }
};

int main() {
    Derived d;
    std::cout << d.name_ << std::endl;  // prints "Derived"
    return 0;
}
```

### Fix 2: Use final Override in Derived Constructor

```cpp
#include <iostream>

class Base {
public:
    virtual void setup() { std::cout << "Base setup" << std::endl; }
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    Derived() {
        setup();  // calls Derived::setup if marked final
    }

    // Mark as final — compiler knows this is the final override
    void setup() final { std::cout << "Derived setup" << std::endl; }
};
```

### Fix 3: Use CRTP for Static Polymorphism

```cpp
#include <iostream>

template <typename Derived>
class Base {
public:
    void initialize() {
        static_cast<Derived*>(this)->init();
    }
    virtual ~Base() = default;
};

class Widget : public Base<Widget> {
public:
    void init() { std::cout << "Widget initialized" << std::endl; }
};

class Button : public Base<Button> {
public:
    void init() { std::cout << "Button initialized" << std::endl; }
};

int main() {
    Button b;
    b.initialize();  // calls Button::init directly — no virtual dispatch
    return 0;
}
```

### Fix 4: Pass Factory Function Instead of Virtual Constructor Call

```cpp
#include <iostream>
#include <string>
#include <memory>

class Widget {
    std::string name_;
public:
    Widget(std::string name) : name_(std::move(name)) {}
    virtual ~Widget() = default;
    const std::string& name() const { return name_; }
};

class Button : public Widget {
    std::string label_;
public:
    Button(std::string name, std::string label)
        : Widget(std::move(name)), label_(std::move(label)) {}
};

// Factory avoids virtual call in constructor
std::unique_ptr<Widget> create_widget(const std::string& type) {
    if (type == "button") return std::make_unique<Button>("btn1", "OK");
    return nullptr;
}
```

### Fix 5: Don't Call Virtual Functions in Destructors Either

```cpp
#include <iostream>

class Resource {
public:
    virtual ~Resource() {
        // WRONG: virtual dispatch goes to base during destruction
        // cleanup();
    }

    void safe_cleanup() {
        cleanup();  // call from non-virtual context
    }

    virtual void cleanup() { std::cout << "Base cleanup" << std::endl; }
};

class ManagedResource : public Resource {
public:
    ~ManagedResource() {
        safe_cleanup();  // call before base destructor runs
    }
    void cleanup() override { std::cout << "Managed cleanup" << std::endl; }
};
```

## Examples

```cpp
// Real-world: initialization pattern avoiding virtual calls
#include <string>
#include <iostream>
#include <memory>

class Logger {
protected:
    std::string prefix_;

    // Called after full construction
    void setup_logging() {
        log("Logger initialized");
    }

public:
    Logger() : prefix_("BASE") {}  // no virtual calls

    virtual ~Logger() = default;

    virtual void log(const std::string& msg) const {
        std::cout << "[" << prefix_ << "] " << msg << std::endl;
    }
};

class AppLogger : public Logger {
public:
    AppLogger() {
        prefix_ = "APP";  // set before calling setup
        setup_logging();   // safe — object fully constructed
    }
};

int main() {
    AppLogger logger;
    logger.log("started");  // "[APP] started"
    return 0;
}
```

## Related Errors

- [Missing virtual destructor]({{< relref "/languages/cpp/virtual-destructor-missing" >}}) — cleanup issues.
- [Object slicing]({{< relref "/languages/cpp/object-slicing" >}}) — losing derived class info.
- [Diamond inheritance]({{< relref "/languages/cpp/diamond-inheritance" >}}) — ambiguous inheritance.

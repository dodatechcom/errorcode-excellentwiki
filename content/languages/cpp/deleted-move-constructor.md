---
title: "[Solution] C++ Deleted Move Constructor — Fix"
description: "Fix deleted implicit move constructor errors by defining explicit move operations, understanding destructor effects, and handling copy-only types."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 912
---

# C++ Deleted Move Constructor — Fix

When a class has a user-declared destructor, copy constructor, or copy assignment operator, the compiler may implicitly delete the move constructor and move assignment operator. This forces copies instead of moves, causing performance issues or compilation errors when move semantics are expected.

## Common Causes

```cpp
// Cause 1: User-declared destructor deletes implicit move
class Resource {
    int* data_;
public:
    ~Resource() { delete data_; }  // user-declared destructor
    // Move constructor is implicitly deleted!
};

void process(Resource r) {}

int main() {
    Resource r;
    process(std::move(r));  // error — move constructor deleted, copy used instead
    return 0;
}
```

```cpp
// Cause 2: User-declared copy constructor
class Buffer {
    char* data_;
    size_t size_;
public:
    Buffer(const Buffer& other);  // user-declared copy constructor
    // Move constructor implicitly deleted
};
```

```cpp
// Cause 3: User-declared copy assignment
class Config {
    std::string settings_;
public:
    Config& operator=(const Config& other);  // user-declared copy assignment
    // Move constructor implicitly deleted
};
```

```cpp
// Cause 4: Const member prevents move
class Fixed {
    const int value_;
public:
    Fixed(int v) : value_(v) {}
    // Move constructor can't move from const members — falls back to copy
};
```

```cpp
// Cause 5: Base class has deleted move
class Base {
public:
    ~Base() {}
};

class Derived : public Base {
    std::string name_;
};
// Derived's move constructor is deleted because Base's move is deleted
```

## How to Fix

### Fix 1: Define Explicit Move Operations

```cpp
#include <utility>

class Resource {
    int* data_;
public:
    Resource(int val) : data_(new int(val)) {}
    ~Resource() { delete data_; }

    // Explicit move constructor
    Resource(Resource&& other) noexcept
        : data_(other.data_) {
        other.data_ = nullptr;
    }

    // Explicit move assignment
    Resource& operator=(Resource&& other) noexcept {
        if (this != &other) {
            delete data_;
            data_ = other.data_;
            other.data_ = nullptr;
        }
        return *this;
    }

    // Delete copy if move-only
    Resource(const Resource&) = delete;
    Resource& operator=(const Resource&) = delete;
};

void process(Resource r) {}

int main() {
    Resource r(42);
    process(std::move(r));  // works — move constructor called
    return 0;
}
```

### Fix 2: Use Rule of Five

```cpp
#include <utility>
#include <cstring>

class Buffer {
    char* data_;
    size_t size_;
public:
    // Constructor
    Buffer(size_t sz) : data_(new char[sz]{}), size_(sz) {}

    // Destructor
    ~Buffer() { delete[] data_; }

    // Copy constructor
    Buffer(const Buffer& other)
        : data_(new char[other.size_]), size_(other.size_) {
        std::memcpy(data_, other.data_, size_);
    }

    // Copy assignment
    Buffer& operator=(const Buffer& other) {
        if (this != &other) {
            delete[] data_;
            size_ = other.size_;
            data_ = new char[size_];
            std::memcpy(data_, other.data_, size_);
        }
        return *this;
    }

    // Move constructor
    Buffer(Buffer&& other) noexcept
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
    }

    // Move assignment
    Buffer& operator=(Buffer&& other) noexcept {
        if (this != &other) {
            delete[] data_;
            data_ = other.data_;
            size_ = other.size_;
            other.data_ = nullptr;
            other.size_ = 0;
        }
        return *this;
    }
};
```

### Fix 3: Use = default for Move Operations

```cpp
class Widget {
    std::string name_;
    int value_;
public:
    Widget(std::string name, int val) : name_(std::move(name)), value_(val) {}

    // Let compiler generate move operations
    Widget(Widget&&) = default;
    Widget& operator=(Widget&&) = default;

    // But still define copy if needed
    Widget(const Widget&) = default;
    Widget& operator=(const Widget&) = default;

    ~Widget() {}  // user-defined destructor, but move ops are explicitly defaulted
};
```

### Fix 4: Avoid Unnecessary User-Declared Destructors

```cpp
// WRONG: unnecessary destructor deletes move ops
class Bad {
    std::string data_;
public:
    ~Bad() {}  // don't need this — let compiler handle it
};

// CORRECT: rely on compiler-generated destructor
class Good {
    std::string data_;
    // Compiler generates: destructor, copy, move — all correct
};
```

### Fix 5: Use RAII to Avoid Custom Destructors

```cpp
#include <memory>
#include <vector>

// WRONG: manual memory management requires custom destructor
class BadBuffer {
    int* data_;
public:
    BadBuffer(size_t n) : data_(new int[n]) {}
    ~BadBuffer() { delete[] data_; }  // deletes implicit move
};

// CORRECT: use smart pointers — no custom destructor needed
class GoodBuffer {
    std::unique_ptr<int[]> data_;
    size_t size_;
public:
    GoodBuffer(size_t n) : data_(new int[n]), size_(n) {}
    // Compiler generates all special members correctly
};
```

## Examples

```cpp
// Real-world: move-only type with RAII
#include <memory>
#include <string>
#include <iostream>

class FileHandle {
    std::unique_ptr<FILE, decltype(&fclose)> file_;
    std::string path_;

public:
    FileHandle(const std::string& path)
        : file_(fopen(path.c_str(), "r"), &fclose)
        , path_(path) {
        if (!file_) throw std::runtime_error("Cannot open: " + path);
    }

    // Move-only: unique_ptr handles the move semantics
    FileHandle(FileHandle&&) = default;
    FileHandle& operator=(FileHandle&&) = default;

    // Deleted copy
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;

    ~FileHandle() = default;

    std::string read_line() {
        char buf[256];
        if (fgets(buf, sizeof(buf), file_.get())) {
            return buf;
        }
        return "";
    }
};
```

## Related Errors

- [Use after move]({{< relref "/languages/cpp/use-after-move" >}}) — accessing moved-from objects.
- [Forwarding reference error]({{< relref "/languages/cpp/forwarding-reference-error" >}}) — template deduction failures.
- [Object slicing]({{< relref "/languages/cpp/object-slicing" >}}) — losing derived class info through copies.

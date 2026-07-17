---
title: "[Solution] C++ auto_ptr Deprecated — Replace with unique_ptr"
description: "Replace std::auto_ptr with std::unique_ptr in C++11 and later. Migration guide with code examples."
deprecated_function: "std::auto_ptr"
replacement_function: "std::unique_ptr"
languages: ["cpp"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C++ auto_ptr Deprecated — Replace with unique_ptr

`std::auto_ptr` was deprecated in C++11 and removed in C++17 because its copy semantics were confusing and dangerous — copying an `auto_ptr` transferred ownership, leaving the source as `nullptr`. This violated the principle of least surprise and made `auto_ptr` behave differently from every other copyable type. `std::unique_ptr` provides move semantics explicitly, making ownership transfer clear.

## What You'll See

In C++11/14:

```
warning: 'std::auto_ptr' is deprecated: Use std::unique_ptr instead
```

In C++17:

```
error: 'auto_ptr' is not a member of 'std'
```

## Why Deprecated

`std::auto_ptr` was deprecated because:

- **Copy = ownership transfer**: Copying an `auto_ptr` silently nullifies the source, breaking expectations.
- **Cannot use in containers**: `std::vector<auto_ptr>` would silently transfer ownership during copies.
- **No move semantics**: Pre-C++11 workaround for move semantics was error-prone.
- **Dangling references**: After copy, the source becomes null, leading to crashes.
- **Confusing API**: `auto_ptr<int> p1(p2)` transfers ownership, unlike every other type.

## Old Code (Deprecated)

```cpp
#include <memory>
#include <iostream>

void process(std::auto_ptr<int> p) {
    std::cout << "Value: " << *p << std::endl;
}

int main() {
    std::auto_ptr<int> p1(new int(42));

    std::auto_ptr<int> p2 = p1;  // p1 is now nullptr!

    // This crashes — p1 was nullified
    // std::cout << *p1 << std::endl;

    process(p2);  // Ownership transferred to function parameter

    // p2 is now nullptr
    return 0;
}
```

## New Code — unique_ptr Replacement

```cpp
#include <memory>
#include <iostream>

void process(std::unique_ptr<int> p) {
    std::cout << "Value: " << *p << std::endl;
}

int main() {
    auto p1 = std::make_unique<int>(42);

    // Move ownership explicitly — intent is clear
    auto p2 = std::move(p1);

    // This won't compile — p1 is in moved-from state
    // std::cout << *p1 << std::endl;

    process(std::move(p2));  // Explicit ownership transfer

    // p2 is now nullptr
    return 0;
}
```

## New Code — unique_ptr with Containers

```cpp
#include <memory>
#include <vector>
#include <iostream>

class Resource {
    int id;
public:
    explicit Resource(int i) : id(i) {}
    ~Resource() { std::cout << "Destroying " << id << std::endl; }
    int getId() const { return id; }
};

int main() {
    std::vector<std::unique_ptr<Resource>> resources;

    resources.push_back(std::make_unique<Resource>(1));
    resources.push_back(std::make_unique<Resource>(2));
    resources.push_back(std::make_unique<Resource>(3));

    for (const auto& r : resources) {
        std::cout << "Resource " << r->getId() << std::endl;
    }

    // All resources destroyed when vector goes out of scope
    return 0;
}
```

## Migration Steps

1. **Find all auto_ptr usage**:

```bash
grep -rn "\bauto_ptr\b" --include="*.h" --include="*.hpp" --include="*.cpp" /path/to/project/
```

2. **Replace `auto_ptr<T>` with `std::unique_ptr<T>`**.

3. **Replace `auto_ptr<T>(new T)` with `std::make_unique<T>()`**.

4. **Replace copies with `std::move()`** where ownership transfer was intended.

5. **Replace `ptr.get()` calls** — they work the same way.

6. **Remove null checks after copy** — `unique_ptr` copy is a compile error.

7. **For shared ownership**, use `std::shared_ptr` instead of `unique_ptr`.

## Related Deprecations

- [bind1st/bind2nd → lambda]({{< relref "/deprecated/cpp/bind1st" >}}) — functional programming modernization.
- [ptr_fun → std::function]({{< relref "/deprecated/cpp/ptr_fun" >}}) — function wrapper modernization.
- [random_shuffle → shuffle]({{< relref "/deprecated/cpp/random_shuffle" >}}) — random number modernization.

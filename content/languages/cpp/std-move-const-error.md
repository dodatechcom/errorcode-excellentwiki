---
title: "[Solution] C++ std::move on Const Object — Fix"
description: "Fix std::move on const objects by not moving from const, removing const, or copying instead. Understand why const prevents move semantics."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 915
---

# C++ std::move on Const Object — Fix

Calling `std::move` on a `const` object does not produce an rvalue reference — it produces a `const` rvalue reference (`const T&&`). Since move constructors and move assignment operators take non-const rvalue references, the move is silently downgraded to a copy. This defeats the purpose of `std::move` and can cause confusion.

## Common Causes

```cpp
// Cause 1: Moving from a const local variable
#include <string>
#include <iostream>

int main() {
    const std::string s = "hello";
    std::string dest = std::move(s);  // copies, not moves! s is const
    std::cout << dest << std::endl;
    return 0;
}
```

```cpp
// Cause 2: Moving from a const reference parameter
#include <string>

void process(const std::string& input) {
    std::string output = std::move(input);  // copies — input is const ref
}
```

```cpp
// Cause 3: Moving from const member variable
#include <string>

class Config {
    const std::string name_;
public:
    Config(std::string name) : name_(std::move(name)) {}

    std::string get_name() const {
        return std::move(name_);  // copies — name_ is const
    }
};
```

```cpp
// Cause 4: Moving from elements in a const container
#include <vector>
#include <string>

void print_all(const std::vector<std::string>& vec) {
    for (const auto& s : vec) {
        std::string copy = std::move(s);  // copies — s is const
    }
}
```

```cpp
// Cause 5: Accidental const through auto
#include <string>
#include <utility>

int main() {
    const auto s = std::string("hello");  // const std::string
    std::string dest = std::move(s);      // copies
    return 0;
}
```

## How to Fix

### Fix 1: Don't Move From Const Objects — Just Copy

```cpp
#include <string>
#include <iostream>

int main() {
    const std::string s = "hello";
    std::string dest = s;  // explicit copy — clearer intent
    std::cout << dest << std::endl;
    return 0;
}
```

### Fix 2: Remove Const When Move Is Needed

```cpp
#include <string>
#include <iostream>

int main() {
    std::string s = "hello";  // non-const
    std::string dest = std::move(s);  // actual move
    std::cout << dest << std::endl;
    std::cout << s.size() << std::endl;  // s is in moved-from state
    return 0;
}
```

### Fix 3: Use Non-const Reference Parameters

```cpp
#include <string>

// WRONG: const ref prevents moving out
void process_bad(const std::string& input) {
    std::string output = std::move(input);  // copies
}

// CORRECT: non-const ref allows moving
void process_good(std::string& input) {
    std::string output = std::move(input);  // moves
}

// CORRECT: by-value parameter allows moving at call site
void process_best(std::string input) {
    std::string output = std::move(input);  // moves from parameter
}
```

### Fix 4: Don't Use const on Variables You Plan to Move

```cpp
#include <string>
#include <vector>

int main() {
    std::vector<std::string> names = {"Alice", "Bob", "Charlie"};

    // WRONG: const auto makes each element const
    // for (const auto& name : names) {
    //     std::string upper = std::move(name);  // copies
    // }

    // CORRECT: non-const reference
    for (auto& name : names) {
        std::string upper = std::move(name);  // moves
    }
    return 0;
}
```

### Fix 5: Use const_cast When You Must Move From const (Carefully)

```cpp
#include <string>
#include <iostream>

class Cache {
    mutable std::string data_;
public:
    Cache(std::string d) : data_(std::move(d)) {}

    // Take from cache — const method that moves (mutable data_)
    std::string take() const {
        return std::move(data_);  // OK because data_ is mutable
    }
};

int main() {
    Cache cache("cached value");
    std::string val = cache.take();  // moves from cache
    std::cout << val << std::endl;
    return 0;
}
```

## Examples

```cpp
// Real-world: factory that moves from non-const sources
#include <string>
#include <vector>
#include <iostream>

class ResourcePool {
    std::vector<std::string> available_;
public:
    void add(std::string resource) {
        available_.push_back(std::move(resource));
    }

    // Take a resource — modifies the pool (non-const)
    std::string acquire() {
        if (available_.empty()) return "";
        std::string res = std::move(available_.back());
        available_.pop_back();
        return res;
    }

    // Peek at available count — const, no move
    size_t count() const {
        return available_.size();
    }
};

int main() {
    ResourcePool pool;
    pool.add("resource1");
    pool.add("resource2");

    std::string r = pool.acquire();  // moves
    std::cout << r << std::endl;
    std::cout << "Remaining: " << pool.count() << std::endl;

    return 0;
}
```

## Related Errors

- [Use after move]({{< relref "/languages/cpp/use-after-move" >}}) — accessing moved-from objects.
- [Forwarding reference error]({{< relref "/languages/cpp/forwarding-reference-error" >}}) — template deduction failure.
- [Reference collapsing error]({{< relref "/languages/cpp/reference-collapsing-error" >}}) — reference to reference issues.

---
title: "[Solution] C++ Use After Move — Undefined Behavior Fix"
description: "Fix use-after-std::move bugs by reassigning moved objects, checking moved-from state, and avoiding access to moved objects."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 911
---

# C++ Use After Move — Undefined Behavior Fix

Using an object after it has been moved from with `std::move` leads to undefined behavior or unexpected results. The object is left in a valid but unspecified state — it may be empty, zeroed, or contain garbage depending on the type's move constructor.

## Common Causes

```cpp
// Cause 1: Using a string after moving it
#include <string>
#include <iostream>

int main() {
    std::string s = "hello";
    std::string dest = std::move(s);
    std::cout << s.size() << std::endl;  // UB or 0 — s was moved from
    return 0;
}
```

```cpp
// Cause 2: Using a vector after moving it
#include <vector>
#include <iostream>

void process(std::vector<int> v) {
    for (int x : v) std::cout << x << " ";
}

int main() {
    std::vector<int> data = {1, 2, 3, 4, 5};
    process(std::move(data));
    std::cout << data.size() << std::endl;  // data is empty or unspecified
    return 0;
}
```

```cpp
// Cause 3: Moving in a loop iteration
#include <string>
#include <vector>

int main() {
    std::vector<std::string> names = {"Alice", "Bob", "Charlie"};
    for (auto& name : names) {
        std::string upper = std::move(name);  // moves each element
        // name is now in moved-from state
    }
    // All elements in names are now in unspecified state
    return 0;
}
```

```cpp
// Cause 4: Moving from a function parameter and using it again
#include <string>

std::string process(std::string input) {
    std::string result = std::move(input);
    input.clear();  // redundant and confusing — input already moved from
    return result;
}
```

```cpp
// Cause 5: Moving from object used in multiple places
#include <memory>
#include <iostream>

int main() {
    auto ptr = std::make_unique<int>(42);
    auto backup = std::move(ptr);  // ptr is now nullptr
    std::cout << *ptr << std::endl;  // dereferencing nullptr — crash
    return 0;
}
```

## How to Fix

### Fix 1: Reassign After Moving

```cpp
#include <string>
#include <iostream>

int main() {
    std::string s = "hello";
    std::string dest = std::move(s);

    // Reassign to a valid state
    s = "reassigned";
    std::cout << s.size() << std::endl;  // safe: s = "reassigned"
    return 0;
}
```

### Fix 2: Check Moved-From State Before Use

```cpp
#include <string>
#include <iostream>
#include <utility>

int main() {
    std::string s = "hello";
    std::string dest = std::move(s);

    // Check if the object is in a usable state
    if (!s.empty()) {
        std::cout << s << std::endl;
    } else {
        std::cout << "string was moved from" << std::endl;
    }
    return 0;
}
```

### Fix 3: Don't Move From Objects You Still Need

```cpp
#include <string>
#include <vector>
#include <iostream>

int main() {
    std::vector<std::string> names = {"Alice", "Bob"};

    // WRONG: moves from names elements
    // for (auto& name : names) {
    //     std::string copy = std::move(name);
    // }

    // CORRECT: use const reference or copy
    for (const auto& name : names) {
        std::string copy = name;  // copy instead of move
        std::cout << copy << std::endl;
    }

    // Or if you need to modify but keep original:
    for (auto& name : names) {
        std::string upper = name;  // copy
        // transform upper...
        std::cout << upper << std::endl;
    }
    return 0;
}
```

### Fix 4: Use std::move Only for Final Transfer

```cpp
#include <string>
#include <vector>

int main() {
    std::vector<std::string> results;

    std::string temp = "computed value";

    // Move only when transferring ownership permanently
    results.push_back(std::move(temp));

    // temp is now in moved-from state — don't use it
    // If needed, assign a new value:
    temp = "next value";
    results.push_back(std::move(temp));

    return 0;
}
```

### Fix 5: Avoid Moving Smart Pointers Then Dereferencing

```cpp
#include <memory>
#include <iostream>

int main() {
    auto ptr = std::make_unique<int>(42);

    // Save raw pointer before moving if you still need access
    int* raw = ptr.get();
    auto backup = std::move(ptr);

    // Use backup (the new owner)
    std::cout << *backup << std::endl;

    // raw pointer is still valid as long as backup exists
    std::cout << *raw << std::endl;

    return 0;
}
```

## Examples

```cpp
// Real-world: safe move in a class method
#include <string>
#include <vector>
#include <iostream>

class TaskQueue {
    std::vector<std::string> tasks_;
public:
    void add_task(std::string task) {
        tasks_.push_back(std::move(task));
        // task is now moved-from — don't use it
    }

    std::string take_task() {
        if (tasks_.empty()) return "";
        std::string task = std::move(tasks_.back());
        tasks_.pop_back();
        // tasks_.back() was moved — pop_back removes it
        return task;  // return by value triggers move or RVO
    }

    void list_all() const {
        for (const auto& t : tasks_) {
            std::cout << t << std::endl;
        }
    }
};
```

## Related Errors

- [Deleted move constructor]({{< relref "/languages/cpp/deleted-move-constructor" >}}) — move semantics not available for type.
- [std::move on const]({{< relref "/languages/cpp/std-move-const-error" >}}) — moving from const objects.
- [Reference collapsing error]({{< relref "/languages/cpp/reference-collapsing-error" >}}) — forwarding reference issues.

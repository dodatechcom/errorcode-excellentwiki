---
title: "[Solution] C++ Erase-Remove Idiom Error — Fix"
description: "Fix erase-remove idiom errors by using erase on the result of std::remove, understanding std::remove doesn't shrink, and using correct remove-erase order."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 944
---

# C++ Erase-Remove Idiom Error — Fix

The erase-remove idiom in C++ is the correct way to remove elements from a container. A common mistake is to use `std::remove` without `erase`, or forget that `std::remove` doesn't actually remove elements — it just moves them to the end and returns an iterator to the new logical end.

## Common Causes

```cpp
// Cause 1: Using std::remove without erase
#include <vector>
#include <algorithm>
#include <iostream>

int main() {
    std::vector<int> v = {1, 2, 3, 2, 4, 2, 5};

    // WRONG: std::remove doesn't shrink the vector
    std::remove(v.begin(), v.end(), 2);

    std::cout << v.size() << std::endl;  // still 7 — elements not actually removed
    return 0;
}
```

```cpp
// Cause 2: Using erase with wrong iterator pair
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3, 2, 4, 2, 5};

    // WRONG: wrong arguments to erase
    auto result = std::remove(v.begin(), v.end(), 2);
    v.erase(v.begin(), v.end());  // removes everything, not just removed elements
    return 0;
}
```

```cpp
// Cause 3: Forgetting std::remove is constrained by element order
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 2, 3, 4};
    auto it = std::remove(v.begin(), v.end(), 2);
    // v is now {1, 3, 4, ?, ?} — elements after it are invalid/don't matter
    for (size_t i = 0; i < v.size(); ++i) {
        std::cout << v[i] << " ";  // prints 1 3 4 3 4 — last 2 are garbage
    }
    return 0;
}
```

```cpp
// Cause 4: Using erase-remove on a map or set
#include <map>
#include <algorithm>

int main() {
    std::map<int, int> m = {{1, 10}, {2, 20}, {3, 30}};

    // WRONG: std::remove doesn't work with associative containers
    // auto it = std::remove_if(m.begin(), m.end(), 
    //     [](const auto& p) { return p.second > 15; });

    // Correct: use m.erase(iterator) directly
    return 0;
}
```

```cpp
// Cause 5: Not using proper erase after remove_if
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, -2, 3, -4, 5, -6};

    auto it = std::remove_if(v.begin(), v.end(), 
                             [](int x) { return x < 0; });

    // Forgot: v.erase(it, v.end());
    // Without erase, vector still has the full capacity
    std::cout << v.size() << std::endl;  // 6 — negative values still in vector
    return 0;
}
```

## How to Fix

### Fix 1: Proper Erase-Remove Idiom

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

int main() {
    std::vector<int> v = {1, 2, 3, 2, 4, 2, 5};

    // CORRECT: erase with remove's return value
    v.erase(std::remove(v.begin(), v.end(), 2), v.end());

    for (int x : v) std::cout << x << " ";  // 1 3 4 5
    std::cout << std::endl;
    std::cout << v.size() << std::endl;  // 4

    return 0;
}
```

### Fix 2: Erase-Remove with Custom Predicate

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

int main() {
    std::vector<int> v = {1, -2, 3, -4, 5, -6};

    // Remove elements matching a predicate
    v.erase(std::remove_if(v.begin(), v.end(),
                           [](int x) { return x < 0; }),
            v.end());

    for (int x : v) std::cout << x << " ";  // 1 3 5
    return 0;
}
```

### Fix 3: Erase Directly from Associative Containers

```cpp
#include <map>
#include <set>
#include <vector>
#include <iostream>

int main() {
    // For associative containers, erase individually or use erase_if
    std::map<int, int> m = {{1, 10}, {2, 20}, {3, 30}};

    // Erase by key
    m.erase(2);

    // Erase by iterator
    for (auto it = m.begin(); it != m.end(); ) {
        if (it->second > 15) {
            it = m.erase(it);  // map::erase returns next iterator
        } else {
            ++it;
        }
    }

    for (const auto& [k, v] : m) {
        std::cout << k << ":" << v << " ";
    }
    return 0;
}
```

### Fix 4: Reset Elements After remove Unless Using erase

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

int main() {
    std::vector<int> v = {1, 2, 2, 3, 4, 2, 5};
    size_t original_size = v.size();

    auto it = std::remove(v.begin(), v.end(), 2);

    // Elements at and after `it` are in moved-from state — don't use them
    // Until you erase:
    v.erase(it, v.end());

    std::cout << v.size() << std::endl;  // 4

    // Alternative: use std::erase (C++20)
    // std::erase(v, 2);  // single container erase — does remove + erase

    return 0;
}
```

### Fix 5: Use C++20 std::erase and std::erase_if

```cpp
#include <vector>
#include <iostream>

// C++20: container-version of erase-remove
void demo_cpp20_erase() {
    std::vector<int> v = {1, -2, 3, -4, 5, -6};

    // Remove all 3s
    std::erase(v, 3);

    // Remove all negative numbers
    std::erase_if(v, [](int x) { return x < 0; });

    for (int x : v) std::cout << x << " ";  // 1 5
}

// For C++17 and earlier, use the traditional idiom
void demo_traditional() {
    std::vector<int> v = {1, -2, 3, -4, 5, -6};

    v.erase(std::remove_if(v.begin(), v.end(),
                           [](int x) { return x < 0; }),
            v.end());
}
```

## Examples

```cpp
// Real-world: removing duplicates from a vector
#include <vector>
#include <algorithm>
#include <iostream>

int main() {
    std::vector<int> v = {5, 1, 3, 5, 2, 3, 4, 2, 1, 5};

    // Step 1: Sort
    std::sort(v.begin(), v.end());

    // Step 2: Unique (similar to remove — moves duplicates to end)
    auto it = std::unique(v.begin(), v.end());

    // Step 3: Erase the duplicates
    v.erase(it, v.end());

    for (int x : v) std::cout << x << " ";  // 1 2 3 4 5
    return 0;
}
```

## Related Errors

- [Iterator invalidation]({{< relref "/languages/cpp/iterator-invalidation" >}}) — modifying containers during iteration.
- [emplace_back error]({{< relref "/languages/cpp/emplace-back-error" >}}) — forwarding constructor arguments.
- [unordered_map rehash error]({{< relref "/languages/cpp/unordered-map-rehash-error" >}}) — rehash during insertion.

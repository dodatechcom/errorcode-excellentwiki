---
title: "[Solution] C++ Iterator Invalidation — Fix"
description: "Fix iterator invalidation by not modifying containers during iteration, using indices, and following the erase-remove idiom."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 941
---

# C++ Iterator Invalidation — Fix

Iterator invalidation occurs when a container is modified while iterating over it. After certain operations (insert, erase, push_back that causes reallocation), iterators to the container may become invalid. Dereferencing an invalid iterator is undefined behavior.

## Common Causes

```cpp
// Cause 1: Erasing during iteration
#include <vector>
#include <iostream>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    for (auto it = v.begin(); it != v.end(); ++it) {
        if (*it % 2 == 0) {
            v.erase(it);  // INVALIDATES it — next ++it is UB
        }
    }
    return 0;
}
```

```cpp
// Cause 2: push_back during range-for loop
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3};
    for (int x : v) {
        if (x == 2) {
            v.push_back(4);  // may invalidate all iterators — UB
        }
    }
    return 0;
}
```

```cpp
// Cause 3: Inserting into vector while iterating
#include <vector>
#include <string>

int main() {
    std::vector<std::string> words = {"hello", "world"};
    for (auto it = words.begin(); it != words.end(); ++it) {
        if (it->size() > 4) {
            words.insert(it, "long word");  // invalidates all iterators
        }
    }
    return 0;
}
```

```cpp
// Cause 4: Modifying unordered_map while iterating
#include <unordered_map>
#include <string>

int main() {
    std::unordered_map<int, std::string> m = {{1, "a"}, {2, "b"}};
    for (auto it = m.begin(); it != m.end(); ++it) {
        m[it->first + 10] = "new";  // rehash may invalidate all iterators
    }
    return 0;
}
```

```cpp
// Cause 5: Storing iterators from previous operations
#include <vector>
#include <iostream>

int main() {
    std::vector<int> v = {1, 2, 3};
    auto it = v.begin();  // points to v[0]
    v.push_back(4);       // may reallocate — it is now invalid
    std::cout << *it << std::endl;  // UB
    return 0;
}
```

## How to Fix

### Fix 1: Use erase's Return Value (Validates Next Iterator)

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    // erase returns iterator to next element
    for (auto it = v.begin(); it != v.end(); ) {
        if (*it % 2 == 0) {
            it = v.erase(it);  // it points to next element after erase
        } else {
            ++it;
        }
    }

    for (int x : v) std::cout << x << " ";  // 1 3 5
    return 0;
}
```

### Fix 2: Use Index-Based Iteration for Mutating Loops

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    // Erase by index — no iterator invalidation concern
    for (size_t i = 0; i < v.size(); ) {
        if (v[i] % 2 == 0) {
            v.erase(v.begin() + i);  // vector shifts elements, i stays valid
        } else {
            ++i;
        }
    }

    for (int x : v) std::cout << x << " ";  // 1 3 5
    return 0;
}
```

### Fix 3: Use erase-remove Idiom

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    // erase-remove idiom — single-pass, no iterator invalidation
    v.erase(std::remove_if(v.begin(), v.end(),
                           [](int x) { return x % 2 == 0; }),
            v.end());

    for (int x : v) std::cout << x << " ";  // 1 3 5
    return 0;
}
```

### Fix 4: Reserve Capacity Before Iterating

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> v = {1, 2, 3};

    // Reserve enough capacity to prevent reallocation
    v.reserve(100);  // at least 100 elements

    for (auto it = v.begin(); it != v.end(); ++it) {
        // push_back is safe because capacity is sufficient
        v.push_back(*it * 10);  // no reallocation — iterators stay valid
    }

    for (int x : v) std::cout << x << " ";
    return 0;
}
```

### Fix 5: Collect Actions, Apply Later

```cpp
#include <vector>
#include <iostream>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    std::vector<int> to_erase;

    // Collect indices to erase
    for (size_t i = 0; i < v.size(); ++i) {
        if (v[i] % 2 == 0) {
            to_erase.push_back(i);
        }
    }

    // Erase in reverse order to preserve indices
    std::sort(to_erase.rbegin(), to_erase.rend());
    for (int idx : to_erase) {
        v.erase(v.begin() + idx);
    }

    for (int x : v) std::cout << x << " ";  // 1 3 5
    return 0;
}
```

## Examples

```cpp
// Real-world: safe iteration patterns for containers
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <iostream>

template <typename Container, typename Pred>
void erase_if(Container& c, Pred pred) {
    for (auto it = c.begin(); it != c.end(); ) {
        if (pred(*it)) {
            it = c.erase(it);
        } else {
            ++it;
        }
    }
}

int main() {
    std::set<int> s = {1, 2, 3, 4, 5};
    std::vector<int> v = {1, 2, 3, 4, 5};
    std::list<int> l = {1, 2, 3, 4, 5};

    // Same pattern works for all container types
    erase_if(s, [](int x) { return x % 2 == 0; });
    erase_if(v, [](int x) { return x % 2 == 0; });
    erase_if(l, [](int x) { return x % 2 == 0; });

    for (int x : s) std::cout << x << " "; std::cout << std::endl;  // 1 3 5
    for (int x : v) std::cout << x << " "; std::cout << std::endl;  // 1 3 5

    return 0;
}
```

## Related Errors

- [Erase-remove idiom error]({{< relref "/languages/cpp/erase-remove-idiom-error" >}}) — incorrect erase-remove usage.
- [emplace_back error]({{< relref "/languages/cpp/emplace-back-error" >}}) — forwarding constructor arguments.
- [unordered_map rehash error]({{< relref "/languages/cpp/unordered-map-rehash-error" >}}) — rehash during iteration.

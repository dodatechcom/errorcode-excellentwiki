---
title: "[Solution] C++ unordered_map Rehash Exception — Fix"
description: "Fix unordered_map rehash exceptions by pre-reserving capacity, setting max_load_factor, and understanding exception guarantees."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 943
---

# C++ unordered_map Rehash Exception — Fix

The unordered associative containers (`unordered_map`, `unordered_set`, etc.) automatically rehash when the load factor exceeds the threshold. Rehashing allocates new buckets and moves all elements, which can throw exceptions. Errors occur when the hash function throws, the allocator fails, or when iterators are invalidated during rehashing.

## Common Causes

```cpp
// Cause 1: Rehash throws due to bad_alloc
#include <unordered_map>
#include <string>

int main() {
    std::unordered_map<int, std::string> m;
    for (int i = 0; i < 1000000; ++i) {
        m[i] = "value " + std::to_string(i);  // may throw std::bad_alloc during rehash
    }
    return 0;
}
```

```cpp
// Cause 2: Rehashing invalidates iterators
#include <unordered_map>
#include <iostream>

int main() {
    std::unordered_map<int, int> m = {{1, 10}, {2, 20}, {3, 30}};
    auto it = m.find(2);

    m[4] = 40;  // may rehash — it is now invalid
    m[5] = 50;  // may rehash again

    std::cout << it->second << std::endl;  // UB if rehash happened
    return 0;
}
```

```cpp
// Cause 3: Hash function throws during rehash
#include <unordered_map>
#include <string>
#include <stdexcept>

struct BadHash {
    std::size_t operator()(int key) const {
        if (key < 0) throw std::runtime_error("negative key");
        return static_cast<std::size_t>(key);
    }
};

int main() {
    std::unordered_map<int, std::string, BadHash> m({{1, "a"}, {-1, "b"}});
    // BadHash throws for -1 — rehash may call hash on existing elements
    return 0;
}
```

```cpp
// Cause 4: Key/Value copy constructors throw during rehash
#include <unordered_map>
#include <stdexcept>

struct ThrowingKey {
    int id;
    ThrowingKey(int i) : id(i) {}
    ThrowingKey(const ThrowingKey& other) {
        if (other.id == 42) throw std::runtime_error("copy failed");
        id = other.id;
    }
    bool operator==(const ThrowingKey& other) const { return id == other.id; }
};

struct std::hash<ThrowingKey> {
    std::size_t operator()(const ThrowingKey& k) const {
        return static_cast<std::size_t>(k.id);
    }
};

int main() {
    std::unordered_map<ThrowingKey, int> m;
    m.emplace(1, 10);
    m.emplace(2, 20);
    m.emplace(42, 420);  // ThrowingKey copy during rehash — exception
    return 0;
}
```

```cpp
// Cause 5: Custom allocator throws during rehash
#include <unordered_map>
#include <memory>

template <typename T>
struct ThrowingAllocator : std::allocator<T> {
    T* allocate(size_t n) {
        if (n > 10) throw std::bad_alloc();
        return std::allocator<T>::allocate(n);
    }
};
```

## How to Fix

### Fix 1: Pre-Reserve Capacity with reserve()

```cpp
#include <unordered_map>
#include <string>

int main() {
    std::unordered_map<int, std::string> m;

    // Pre-reserve enough space to avoid rehashes
    m.reserve(1000000);

    for (int i = 0; i < 1000000; ++i) {
        m[i] = "value " + std::to_string(i);  // no rehash
    }
    return 0;
}
```

### Fix 2: Set max_load_factor

```cpp
#include <unordered_map>
#include <string>

int main() {
    std::unordered_map<int, std::string> m;

    // Lower load factor = less dense = fewer rehashes
    // Default is typically 1.0
    m.max_load_factor(0.5);

    m[1] = "a";
    m[2] = "b";
    m[3] = "c";

    // With lower max_load_factor, rehash happens sooner but more gradually
    // between insertions

    return 0;
}
```

### Fix 3: Use rehash() to Control Bucket Count

```cpp
#include <unordered_map>
#include <string>

int main() {
    std::unordered_map<int, std::string> m;

    // Explicitly set number of buckets
    m.rehash(1000);  // at least 1000 buckets

    for (int i = 0; i < 1000; ++i) {
        m[i] = "value " + std::to_string(i);
        // No rehash because buckets >= element count / max_load_factor
    }
    return 0;
}
```

### Fix 4: Re-acquire Iterators After Insertions

```cpp
#include <unordered_map>
#include <iostream>

int main() {
    std::unordered_map<int, int> m = {{1, 10}, {2, 20}, {3, 30}};

    // Don't store iterators across insertions
    m[4] = 40;

    // Find again after modification
    auto it = m.find(2);
    if (it != m.end()) {
        std::cout << it->second << std::endl;  // safe
    }

    return 0;
}
```

### Fix 5: Use noexcept Hash Functions

```cpp
#include <unordered_map>
#include <string>
#include <cstddef>

struct SafeHash {
    std::size_t operator()(int key) const noexcept {
        return static_cast<std::size_t>(key >= 0 ? key : -key);
    }
};

int main() {
    // noexcept hash function ensures rehash won't throw from hashing
    std::unordered_map<int, std::string, SafeHash> m;

    m[1] = "one";
    m[-1] = "negative one";  // SafeHash handles negative keys

    // Pre-reserve for added safety
    m.reserve(100);

    return 0;
}
```

## Examples

```cpp
// Real-world: exception-safe unordered_map usage
#include <unordered_map>
#include <string>
#include <iostream>
#include <cstddef>

class UserDatabase {
    struct User {
        std::string name;
        std::string email;
    };

    std::unordered_map<int, User> users_;

public:
    UserDatabase() {
        // Allocate space upfront for expected size
        users_.reserve(1000);
    }

    void add_user(int id, std::string name, std::string email) {
        // Pre-reserve if we're approaching capacity
        if (users_.size() >= users_.capacity()) {
            users_.reserve(users_.size() * 2);
        }

        users_.emplace(id, User{std::move(name), std::move(email)});
    }

    const User* find_user(int id) const {
        auto it = users_.find(id);
        return it != users_.end() ? &it->second : nullptr;
    }

    size_t capacity() const { return users_.bucket_count() * users_.max_load_factor(); }
};
```

## Related Errors

- [Iterator invalidation]({{< relref "/languages/cpp/iterator-invalidation" >}}) — modifying containers during iteration.
- [Emplace_back error]({{< relref "/languages/cpp/emplace-back-error" >}}) — forwarding constructor arguments.
- [Exception safety guarantees]({{< relref "/languages/cpp/exception-safety-guarantees" >}}) — guarantee violations.

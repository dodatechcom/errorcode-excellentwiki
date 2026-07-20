---
title: "[Solution] C++ emplace_back Error — Fix"
description: "Fix emplace_back errors by providing correct constructor arguments, handling explicit constructors, and using proper forwarding."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
weight: 942
---

# C++ emplace_back Error — Fix

`emplace_back` constructs an element in-place by forwarding its arguments to the element's constructor. Errors occur when the arguments don't match any constructor, when forwarding fails, or when an explicit constructor prevents implicit construction.

## Common Causes

```cpp
// Cause 1: Wrong number of arguments
#include <vector>
#include <string>

struct Person {
    std::string name;
    int age;
    Person(std::string n, int a) : name(std::move(n)), age(a) {}
};

int main() {
    std::vector<Person> people;
    people.emplace_back("Alice");  // ERROR: no Person constructor with 1 arg
    return 0;
}
```

```cpp
// Cause 2: Explicit constructor blocks emplace_back
#include <vector>

struct ExplicitType {
    int value;
    explicit ExplicitType(int v) : value(v) {}
};

int main() {
    std::vector<ExplicitType> v;
    v.emplace_back(42);  // OK: emplace_back uses direct initialization

    // But this only compiles if the constructor is not explicit:
    // v.push_back(42);  // ERROR: implicit conversion from int
    return 0;
}
```

```cpp
// Cause 3: Braced init lists don't deduce with emplace_back
#include <vector>

struct Point {
    int x, y;
    Point(int a, int b) : x(a), y(b) {}
};

int main() {
    std::vector<Point> points;
    // points.emplace_back({1, 2});  // ERROR: braced-init-list can't deduce
    points.emplace_back(1, 2);  // OK: forwarded as (1, 2)
    return 0;
}
```

```cpp
// Cause 4: Forwarding reference mismatch
#include <vector>
#include <string>

class Wrapper {
    std::string str_;
public:
    Wrapper(const std::string& s) : str_(s) {}
    Wrapper(std::string&& s) : str_(std::move(s)) {}
};

int main() {
    std::vector<Wrapper> v;
    const std::string s = "hello";
    v.emplace_back(s);  // OK: forwards to const std::string&
    // v.emplace_back(std::move(s));  // ERROR: s is const, can't move
    return 0;
}
```

```cpp
// Cause 5: Ambiguity with multiple constructors
#include <vector>
#include <string>

struct Config {
    Config(std::string a, std::string b)
        : path_(std::move(a)), value_(std::move(b)) {}
    Config(std::string a, int b)
        : path_(std::move(a)), timeout_(b) {}
    std::string path_;
    std::string value_;
    int timeout_ = 30;
};

int main() {
    std::vector<Config> configs;
    configs.emplace_back("/cfg", 42);  // ambiguous? no — int and string are distinct
    configs.emplace_back("/cfg", "value");  // ambiguous? no — both strings
    return 0;
}
```

## How to Fix

### Fix 1: Match Constructor Arguments Exactly

```cpp
#include <vector>
#include <string>

struct Person {
    std::string name;
    int age;
    Person(std::string n, int a) : name(std::move(n)), age(a) {}
};

int main() {
    std::vector<Person> people;
    people.emplace_back("Alice", 30);  // OK: matches Person(string, int)
    people.emplace_back("Bob", 25);    // OK
    return 0;
}
```

### Fix 2: Use explicit Syntax for Explicit Constructors

```cpp
#include <vector>

struct Money {
    long cents;
    explicit Money(long c) : cents(c) {}
};

int main() {
    std::vector<Money> amounts;

    // emplace_back with direct initialization — works with explicit
    amounts.emplace_back(1000);

    // push_back with explicit — won't compile:
    // amounts.push_back(1000);  // ERROR: explicit constructor

    // But emplace_back is fine — it's direct, not copy initialization
    return 0;
}
```

### Fix 3: Use Named Type or Wrapper for Braced Init Lists

```cpp
#include <vector>
#include <utility>

struct Point {
    int x, y;
    Point(int a, int b) : x(a), y(b) {}
};

int main() {
    std::vector<Point> points;

    // WRONG: braced-init-list
    // points.emplace_back({1, 2});

    // CORRECT: pass individual arguments
    points.emplace_back(1, 2);
    points.emplace_back(3, 4);

    // Also correct: use explicit temporary
    points.push_back(Point(5, 6));

    return 0;
}
```

### Fix 4: Use std::piecewise_construct for Pairs

```cpp
#include <vector>
#include <map>
#include <string>

int main() {
    std::vector<std::pair<int, std::string>> v;

    // emplace_back for pair
    v.emplace_back(1, "one");  // OK: pair(piecewise_construct, ...) is tried

    // For complex pairs with piecewise construction:
    v.emplace_back(std::piecewise_construct,
                   std::forward_as_tuple(2),
                   std::forward_as_tuple(3, 'a'));  // string(3, 'a') = "aaa"

    return 0;
}
```

### Fix 5: Create a Temporary for Complex Construction

```cpp
#include <vector>
#include <string>

struct ComplexResource {
    std::string id;
    std::vector<int> data;

    ComplexResource(std::string id, std::vector<int> data)
        : id(std::move(id)), data(std::move(data)) {}
};

int main() {
    std::vector<ComplexResource> resources;

    // Option 1: emplace_back with explicit temporaries
    resources.emplace_back("res1", std::vector<int>{1, 2, 3});

    // Option 2: move an existing object
    ComplexResource r("res2", {4, 5, 6});
    resources.push_back(std::move(r));

    // Option 3: construct then move
    resources.push_back(ComplexResource("res3", {7, 8, 9}));

    return 0;
}
```

## Examples

```cpp
// Real-world: emplace_back in a config storage
#include <vector>
#include <string>
#include <chrono>
#include <iostream>

struct ConfigEntry {
    std::string key;
    std::string value;
    std::chrono::system_clock::time_point created;

    ConfigEntry() : created(std::chrono::system_clock::now()) {}

    ConfigEntry(std::string k, std::string v)
        : key(std::move(k)), value(std::move(v))
        , created(std::chrono::system_clock::now()) {}
};

class ConfigStore {
    std::vector<ConfigEntry> entries_;
public:
    void set(const std::string& key, const std::string& value) {
        // emplace_back constructs ConfigEntry in-place
        entries_.emplace_back(key, value);
    }

    void set_default() {
        // default construct in-place
        entries_.emplace_back();
    }

    const ConfigEntry& get(size_t idx) const {
        return entries_.at(idx);
    }
};

int main() {
    ConfigStore store;
    store.set("host", "localhost");
    store.set("port", "8080");
    store.set_default();
    return 0;
}
```

## Related Errors

- [Iterator invalidation]({{< relref "/languages/cpp/iterator-invalidation" >}}) — modifying containers during iteration.
- [Erase-remove idiom error]({{< relref "/languages/cpp/erase-remove-idiom-error" >}}) — incorrect erase-remove usage.
- [Forwarding reference error]({{< relref "/languages/cpp/forwarding-reference-error" >}}) — template deduction failures.

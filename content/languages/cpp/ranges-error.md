---
title: "[Solution] C++ std::ranges Error — Ranges Algorithm Fix"
description: "Fix C++ std::ranges errors including iterator requirements, range concepts, and projection failures. Learn correct ranges usage patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ std::ranges Error — Ranges Algorithm Fix

`std::ranges` errors occur when algorithms receive ranges that don't satisfy the required concepts — such as providing a non-sorted range to `ranges::sort`, using iterators that don't satisfy the required category, or failing to provide a valid projection or comparator.

## Why std::ranges Errors Occur

Common causes include passing ranges with iterators that don't meet requirements (e.g., input iterators for random-access algorithms), using projections that return non-comparable types, providing comparators that don't satisfy strict weak ordering, and mixing incompatible range types.

## Wrong: Using Ranges With Wrong Iterator Category

```cpp
// WRONG — ranges::sort requires random_access_iterator
#include <ranges>
#include <iostream>
#include <list>

int main() {
    std::list<int> lst = {3, 1, 4, 1, 5};

    // Error — list iterators are bidirectional, not random access
    // std::ranges::sort(lst);

    std::ranges::sort(lst.begin(), lst.end());  // also fails

    return 0;
}
```

## Correct: Use Compatible Range Types

```cpp
// CORRECT — use random-access containers with ranges::sort
#include <ranges>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {3, 1, 4, 1, 5};

    std::ranges::sort(vec);

    for (int val : vec) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## Use Ranges With Projections

```cpp
// CORRECT — use projections for custom sorting
#include <ranges>
#include <iostream>
#include <vector>
#include <string>

struct Person {
    std::string name;
    int age;
};

int main() {
    std::vector<Person> people = {
        {"Alice", 30}, {"Bob", 25}, {"Charlie", 35}
    };

    std::ranges::sort(people, {}, &Person::age);

    for (const auto& p : people) {
        std::cout << p.name << " (" << p.age << ")" << std::endl;
    }
    return 0;
}
```

## Use Ranges Views for Lazy Evaluation

```cpp
// CORRECT — use views for efficient pipelines
#include <ranges>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    auto result = nums
        | std::views::filter([](int n) { return n % 2 == 0; })
        | std::views::transform([](int n) { return n * n; });

    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Use `std::vector` with `ranges::sort` | When random-access iterators are needed |
| Use projections for custom comparisons | When sorting by specific members |
| Use views for lazy pipelines | When chaining multiple operations |
| Check iterator category requirements | When algorithms fail with certain containers |

## Related Errors

- [template instantiation error]({{< relref "/languages/cpp/template-error" >}}) — template issues.
- [C++20 concept error]({{< relref "/languages/cpp/concept-error" >}}) — concept constraint failures.
- [constexpr evaluation]({{< relref "/languages/cpp/constexpr-error" >}}) — constexpr failures.

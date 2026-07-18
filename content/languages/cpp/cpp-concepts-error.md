---
title: "[Solution] C++ Concepts Error — How to Fix"
description: "Fix C++20 concept constraint errors including substitution failures, hard errors in requires expressions, and concept refinements."
languages: ["cpp"]
severities: ["error"]
error_types: ["compile-time"]
weight: 5
comments: true
---

# [Solution] C++ Concepts Error — How to Fix

C++20 concepts provide compile-time constraints on template parameters, but incorrect concept definitions, refinements, and requires expressions can produce cryptic substitution failure errors.

## Why It Happens

Concept errors arise when template arguments don't satisfy the specified constraints, when requires expressions contain ill-formed clauses, when concepts are not properly refined from base concepts, or when constrained auto parameters deduce unexpected types.

## Common Error Messages

1. `error: constraints not satisfied: no match for 'concept_name<int>'`
2. `error: no type named 'type' in 'std::enable_if<false>'`
3. `error: requires expression contains invalid expressions`
4. `error: ambiguous partial specialization`

## How to Fix It

### Fix 1: Validate Concept Constraints Explicitly

```cpp
#include <concepts>
#include <iostream>

template <typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

// WRONG — will fail for non-numeric types
template <Numeric T>
T add(T a, T b) { return a + b; }

// Use static_assert for clearer errors
template <typename T>
requires requires(T a, T b) { { a + b } -> std::convertible_to<T>; }
T add_checked(T a, T b) { return a + b; }
```

### Fix 2: Fix Requires Expression Syntax

```cpp
#include <concepts>
#include <vector>

// WRONG — missing braces around sub-expression
template <typename T>
concept HasSize = requires(T t) {
    t.size();  // needs braces for nested requirement
};

// CORRECT — proper requires expression
template <typename T>
concept HasSizeCorrect = requires(T t) {
    { t.size() } -> std::convertible_to<std::size_t>;
};
```

### Fix 3: Use Constrained Auto Parameters

```cpp
#include <concepts>
#include <iostream>

// CORRECT — constrained auto deduces correctly
void process(std::integral auto val) {
    std::cout << "Integer: " << val << "\n";
}

void process(std::floating_point auto val) {
    std::cout << "Float: " << val << "\n";
}
```

## Common Scenarios

- **Concept refinement**: Refining multiple base concepts can create ambiguities if constraints overlap.
- **Nested requires**: Substitution failures inside nested requires expressions are hard to diagnose.
- **Concept negation**: `!Concept<T>` behaves differently than `requires { !concept<T>; }`.

## Prevent It

1. Always test concepts with both valid and invalid types using `static_assert(concept<T>)`.
2. Keep concept definitions simple and compose small concepts rather than writing monolithic ones.
3. Use `requires` clauses on functions rather than constrained class templates for better error messages.

## Related Errors

- [SFINAE error]({{< relref "/languages/cpp/cpp-sfinae-error" >}}) — substitution failure in older templates.
- [CRTP error]({{< relref "/languages/cpp/cpp-crtp-error" >}}) — curiously recurring template issues.
- [Ranges error]({{< relref "/languages/cpp/cpp-ranges-error" >}}) — range concept violations.

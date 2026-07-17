---
title: "[Solution] C++ Catch2 - test error"
description: "Fix C++ Catch2 test errors. Resolve test assertion failures."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Catch2 - test error

Catch2 test errors occur when test assertions (REQUIRE, CHECK) fail.

## Common Causes

```cpp
// Cause 1: Value mismatch
REQUIRE(1 + 1 == 3); // fails

// Cause 2: Missing exception
REQUIRE_THROWS(safe_func()); // fails if no throw

// Cause 3: Approximate comparison
REQUIRE(1.0 == Approx(2.0)); // fails
```

## How to Fix

### Fix 1: Correct the assertion

```cpp
REQUIRE(1 + 1 == 2);
```

### Fix 2: Fix the code

```cpp
// If test is correct, fix the implementation
int add(int a, int b) { return a + b; }
REQUIRE(add(1, 1) == 2);
```

### Fix 3: Use sections for debugging

```cpp
SECTION("debugging") {
    auto result = compute();
    INFO("result = " << result);
    REQUIRE(result == 42);
}
```

## Examples

```cpp
#include <catch2/catch_test_macros.hpp>

TEST_CASE("Addition", "[math]") {
    REQUIRE(1 + 1 == 2);
}
```

## Related Errors

- [Google Test - test error]({{< relref "/languages/cpp/google-test-error" >}}) — gtest errors.
- [doctest - test error]({{< relref "/languages/cpp/doctest-error" >}}) — doctest errors.
- [Boost.Test - test error]({{< relref "/languages/cpp/boost-test-error" >}}) — Boost.Test errors.

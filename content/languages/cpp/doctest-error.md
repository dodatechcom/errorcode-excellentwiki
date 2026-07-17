---
title: "[Solution] C++ doctest - test error"
description: "Fix C++ doctest test errors. Resolve test assertion failures."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["doctest", "unit-test", "assertion", "test", "testing"]
weight: 5
---

# doctest - test error

doctest test errors occur when test assertions (REQUIRE, CHECK) fail.

## Common Causes

```cpp
// Cause 1: Value mismatch
REQUIRE(1 + 1 == 3); // fails

// Cause 2: Missing exception
REQUIRE_THROWS(safe_func()); // fails if no throw

// Cause 3: Approximate comparison
CHECK(Approx(1.0) == 2.0); // fails
```

## How to Fix

### Fix 1: Correct the assertion

```cpp
REQUIRE(1 + 1 == 2);
```

### Fix 2: Fix the code

```cpp
int add(int a, int b) { return a + b; }
REQUIRE(add(1, 1) == 2);
```

### Fix 3: Run specific test case

```bash
./my_tests --test-case="Addition"
```

## Examples

```cpp
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>

TEST_CASE("Addition") {
    REQUIRE(1 + 1 == 2);
}
```

## Related Errors

- [Google Test - test error]({{< relref "/languages/cpp/google-test-error" >}}) — gtest errors.
- [Catch2 - test error]({{< relref "/languages/cpp/catch2-error" >}}) — Catch2 errors.
- [Boost.Test - test error]({{< relref "/languages/cpp/boost-test-error" >}}) — Boost.Test errors.

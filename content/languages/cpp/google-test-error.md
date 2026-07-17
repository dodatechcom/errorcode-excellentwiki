---
title: "[Solution] C++ Google Test - test error"
description: "Fix C++ Google Test (gtest) test errors. Resolve test failures and assertion errors."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["google-test", "gtest", "unit-test", "assertion", "test"]
weight: 5
---

# Google Test - test error

Google Test errors occur when test assertions fail, indicating the code did not behave as expected.

## Common Causes

```cpp
// Cause 1: Value mismatch
EXPECT_EQ(1 + 1, 3); // fails

// Cause 2: Missing expected exception
EXPECT_THROW(safe_func(), std::runtime_error); // fails if no throw

// Cause 3: Null pointer
EXPECT_NE(ptr, nullptr); // fails if null
```

## How to Fix

### Fix 1: Fix the code or test

```cpp
EXPECT_EQ(1 + 1, 2); // correct expectation
```

### Fix 2: Add debugging output

```cpp
int result = compute();
EXPECT_EQ(result, 42) << "Expected 42 but got " << result;
```

### Fix 3: Run specific test

```bash
./my_tests --gtest_filter="MyTestSuite.MyTest"
```

## Examples

```cpp
#include <gtest/gtest.h>

TEST(MathTest, Addition) {
    EXPECT_EQ(1 + 1, 2);
}

TEST(MathTest, Division) {
    EXPECT_DOUBLE_EQ(10.0 / 3.0, 3.333333333333);
}
```

## Related Errors

- [Catch2 - test error]({{< relref "/languages/cpp/catch2-error" >}}) — Catch2 errors.
- [doctest - test error]({{< relref "/languages/cpp/doctest-error" >}}) — doctest errors.
- [Boost.Test - test error]({{< relref "/languages/cpp/boost-test-error" >}}) — Boost.Test errors.

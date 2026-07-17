---
title: "[Solution] C++ Google Test - assertion error"
description: "Fix C++ Google Test (gtest) assertion errors. Handle EXPECT and ASSERT macro failures."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["gtest", "google-test", "assertion", "expect", "assert"]
weight: 5
---

# Google Test - assertion error

Google Test assertion errors are reported by EXPECT_* and ASSERT_* macros when conditions are not met.

## Common Causes

```cpp
// Cause 1: EXPECT_* failure (non-fatal)
EXPECT_EQ(a, b); // logs failure but continues

// Cause 2: ASSERT_* failure (fatal)
ASSERT_NE(ptr, nullptr); // stops current test

// Cause 3: Floating point comparison
EXPECT_EQ(0.1 + 0.2, 0.3); // fails due to precision
```

## How to Fix

### Fix 1: Use correct comparison

```cpp
// For floating point
EXPECT_NEAR(0.1 + 0.2, 0.3, 1e-9);

// For containers
EXPECT_THAT(vec, testing::ElementsAre(1, 2, 3));
```

### Fix 2: Add failure messages

```cpp
int result = compute();
EXPECT_EQ(result, 42) << "compute() returned " << result << ", expected 42";
```

### Fix 3: Use death tests for crashes

```cpp
EXPECT_DEATH(func_that_crashes(), ".*");
```

## Related Errors

- [Catch2 - test error]({{< relref "/languages/cpp/catch2-error" >}}) — Catch2 errors.
- [doctest - test error]({{< relref "/languages/cpp/doctest-error" >}}) — doctest errors.
- [Boost.Test - test error]({{< relref "/languages/cpp/boost-test-error" >}}) — Boost.Test errors.

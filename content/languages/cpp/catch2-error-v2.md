---
title: "[Solution] Catch2 Test Assertion Failed Fix"
description: "Fix Catch2 assertion failures. Handle REQUIRE, CHECK, and SECTION failures in Catch2 tests."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["catch2", "testing", "assertion", "unit-test"]
weight: 5
---

# Catch2 Test Assertion Failed Fix

Fix Catch2 assertion failures. Handle REQUIRE, CHECK, and SECTION failures in Catch2 tests.

## What This Error Means

Catch2 assertions fail when test expectations are not met:

```
FAILED:
  REQUIRE( result == expected )
with expansion:
  42 == 43
```

## Common Causes

```cpp
// Cause 1: Wrong expected value
TEST_CASE("Math") {
    REQUIRE(add(2, 3) == 6); // Should be 5
}

// Cause 2: REQUIRE stops at first failure
// Cause 3: SECTIONs sharing mutable state
// Cause 4: Approximate comparison without Approx()
```

## How to Fix

### Fix 1: Use CHECK for non-fatal assertions

```cpp
#include <catch2/catch_test_macros.hpp>

TEST_CASE("Multiple checks") {
    CHECK(add(2, 3) == 5);   // Continues even if fails
    CHECK(add(1, 1) == 2);   // Independent check
    CHECK(add(0, 0) == 0);
}
```

### Fix 2: Use Approx for floating-point comparisons

```cpp
#include <catch2/catch_test_macros.hpp>
#include <catch2/catch_approx.hpp>

TEST_CASE("Floating point") {
    double result = 3.14159 * 2;
    REQUIRE(result == Catch::Approx(6.28318).epsilon(0.001));
}
```

### Fix 3: Use SECTIONs with proper isolation

```cpp
#include <catch2/catch_test_macros.hpp>

TEST_CASE("User operations") {
    User user{"Alice", 25};

    SECTION("Name is correct") {
        REQUIRE(user.name == "Alice");
    }

    SECTION("Age is correct") {
        REQUIRE(user.age == 25);
    }

    // Each SECTION gets a fresh copy of user
}
```

## Examples

```cpp
#include <catch2/catch_test_macros.hpp>
#include <string>

std::string trim(const std::string& s) {
    auto start = s.find_first_not_of(" \t\n");
    auto end = s.find_last_not_of(" \t\n");
    return (start == std::string::npos) ? "" : s.substr(start, end - start + 1);
}

TEST_CASE("String trim") {
    CHECK(trim("") == "");
    CHECK(trim("  hello  ") == "hello");
    CHECK(trim("no_spaces") == "no_spaces");
    CHECK(trim("   ") == "");
}

TEST_CASE("Trim with REQUIRE on critical path") {
    REQUIRE(trim("test") == "test");
}
```

## Related Errors

- [Google Test Error]({{< relref "/languages/cpp/google-test-error" >}}) — Google Test error
- [Google Test Error V2]({{< relref "/languages/cpp/google-test-v2" >}}) — Google Test error
- [Doctest Error]({{< relref "/languages/cpp/doctest-error" >}}) — doctest error

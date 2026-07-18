---
title: "[Solution] C++ Catch2 Error — How to Fix"
description: "Fix C++ Catch2 test errors including assertion failures, incorrect test case configuration, and BDD section nesting problems in unit testing."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ Catch2 Error — How to Fix

Catch2 test errors occur when assertions fail due to incorrect expected values, when test fixtures aren't properly set up, when BDD-style sections are misconfigured, or when test discovery fails due to missing macros.

## Why It Happens

Catch2 errors arise when REQUIRE/CHECK assertions don't match actual values, when test cases aren't registered with TEST_CASE macros, when SECTION nesting exceeds capabilities, when Approx() is used incorrectly for floating-point comparisons, or when GENERATE() creates unexpected values.

## Common Error Messages

1. `FAILED: REQUIRE( a == b ) with expansion: 1 == 2`
2. `error: no such test case — test not registered`
3. `error: SECTION nesting too deep`
4. `error: GENERATE value out of expected range`

## How to Fix It

### Fix 1: Correct Test Assertions

```cpp
#include <catch2/catch_test_macros.hpp>
#include <catch2/catch_approx.hpp>

int add(int a, int b) { return a + b; }

TEST_CASE("Addition", "[math]") {
    REQUIRE(add(1, 1) == 2);

    // CORRECT — use Approx for floating point
    double result = 3.14159;
    REQUIRE(result == Catch::Approx(3.14159).margin(0.001));
}
```

### Fix 2: Use BDD Style Correctly

```cpp
#include <catch2/catch_test_macros.hpp>

SCENARIO("User login") {
    GIVEN("valid credentials") {
        std::string username = "admin";
        std::string password = "secret";

        WHEN("user logs in") {
            bool success = (username == "admin" && password == "secret");

            THEN("login succeeds") {
                REQUIRE(success);
            }
        }
    }
}
```

### Fix 3: Use GENERATE for Parameterized Tests

```cpp
#include <catch2/catch_test_macros.hpp>
#include <catch2/generators/catch_generators_all.hpp>

TEST_CASE("Division", "[math]") {
    auto [a, b, expected] = GENERATE(
        table<int, int, int>({
            {10, 2, 5},
            {20, 4, 5},
            {100, 10, 10}
        }));

    REQUIRE(a / b == expected);
}
```

### Fix 4: Use Sections for Debugging

```cpp
#include <catch2/catch_test_macros.hpp>
#include <string>

std::string process(int value) {
    if (value < 0) return "negative";
    if (value == 0) return "zero";
    return "positive";
}

TEST_CASE("Process", "[utility]") {
    SECTION("negative input") {
        REQUIRE(process(-1) == "negative");
    }
    SECTION("zero input") {
        REQUIRE(process(0) == "zero");
    }
    SECTION("positive input") {
        REQUIRE(process(5) == "positive");
    }
}
```

## Common Scenarios

- **Floating point comparison**: Exact equality fails for floating-point values — use `Approx`.
- **Missing TEST_CASE**: Functions containing assertions without `TEST_CASE` aren't discovered.
- **Section duplication**: Each SECTION runs in its own context, creating many test combinations.

## Prevent It

1. Always use `Catch::Approx` for floating-point comparisons.
2. Use `REQUIRE` for fatal checks and `CHECK` for non-fatal checks.
3. Keep sections shallow — deep nesting creates exponentially many test paths.

## Related Errors

- [Google test error]({{< relref "/languages/cpp/google-test-error" >}}) — gtest issues.
- [doctest error]({{< relref "/languages/cpp/doctest-error" >}}) — doctest issues.
- [Benchmark error]({{< relref "/languages/cpp/cpp-benchmark-error.md" >}}) — performance testing issues.

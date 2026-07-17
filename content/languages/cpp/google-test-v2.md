---
title: "[Solution] Google Test Assertion Failed Fix"
description: "Fix Google Test assertion failures. Handle EXPECT_EQ, ASSERT_TRUE failures, and test setup/teardown issues."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Google Test Assertion Failed Fix

Fix Google Test assertion failures. Handle EXPECT_EQ, ASSERT_TRUE failures, and test setup/teardown issues.

## What This Error Means

Google Test assertions fail when test expectations are not met:

```
[  FAILED  ] MathTest.Add (0 ms)
Expected equality of these values:
  add(2, 3)
    Which is: 5
  6
```

## Common Causes

```cpp
// Cause 1: Expected value wrong
TEST(MathTest, Add) {
    EXPECT_EQ(add(2, 3), 6); // Wrong - should be 5
}

// Cause 2: State mutation in tests without cleanup
// Cause 3: ASSERT_* stops test execution
// Cause 4: Flaky tests due to timing or ordering
// Cause 5: Missing test fixture initialization
```

## How to Fix

### Fix 1: Use meaningful test names and correct expectations

```cpp
#include <gtest/gtest.h>

int add(int a, int b) { return a + b; }

TEST(MathTest, AddPositiveNumbers) {
    EXPECT_EQ(add(2, 3), 5);
}

TEST(MathTest, AddNegativeNumbers) {
    EXPECT_EQ(add(-1, -1), -2);
}
```

### Fix 2: Use EXPECT_* for non-critical checks

```cpp
TEST(StringTest, ParseCSV) {
    auto fields = parse_csv("a,b,c");
    EXPECT_EQ(fields.size(), 3u);
    EXPECT_EQ(fields[0], "a");
    EXPECT_EQ(fields[1], "b");
    EXPECT_EQ(fields[2], "c");
}
```

### Fix 3: Use test fixtures for setup/teardown

```cpp
#include <gtest/gtest.h>

class DatabaseTest : public ::testing::Test {
protected:
    void SetUp() override {
        db_.connect("test.db");
        db_.create_table("users");
    }

    void TearDown() override {
        db_.drop_table("users");
        db_.disconnect();
    }

    Database db_;
};

TEST_F(DatabaseTest, InsertUser) {
    db_.insert_user("Alice");
    EXPECT_TRUE(db_.user_exists("Alice"));
}
```

## Examples

```cpp
#include <gtest/gtest.h>

class Calculator {
public:
    int add(int a, int b) { return a + b; }
    int divide(int a, int b) {
        if (b == 0) throw std::runtime_error("Division by zero");
        return a / b;
    }
};

class CalculatorTest : public ::testing::Test {
protected:
    Calculator calc;
};

TEST_F(CalculatorTest, Add) {
    EXPECT_EQ(calc.add(2, 3), 5);
    EXPECT_EQ(calc.add(-1, 1), 0);
}

TEST_F(CalculatorTest, Divide) {
    EXPECT_EQ(calc.divide(10, 2), 5);
    EXPECT_THROW(calc.divide(1, 0), std::runtime_error);
}

int main(int argc, char** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```

## Related Errors

- [Google Test Error]({{< relref "/languages/cpp/google-test-error" >}}) — Google Test error
- [Catch2 Error]({{< relref "/languages/cpp/catch2-error-v2" >}}) — Catch2 error
- [Doctest Error]({{< relref "/languages/cpp/doctest-error" >}}) — doctest error

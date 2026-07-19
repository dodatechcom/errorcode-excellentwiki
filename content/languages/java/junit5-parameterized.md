---
title: "[Solution] ParameterizedTestExtension Error — JUnit 5 Fix"
description: "Fix ParameterizedTestExtension errors in JUnit 5. Resolve parameterized test discovery and execution failures."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ParameterizedTestExtension Error — JUnit 5 Fix

A `ParameterizedTestExtension` error occurs when JUnit 5's parameterized test mechanism fails to discover, supply, or execute test arguments. This is common when the arguments provider returns incompatible types or when the test method signature does not match the supplied arguments.

## What This Error Means

Common messages:

- `org.junit.jupiter.params.ParameterizedTestExtension`
- `ParameterizedTestExtension: No ArgumentsSource annotation found`
- `ParameterResolutionException: Could not find a suitable method`

## Common Causes

```java
// Cause 1: Argument count does not match parameters
@ParameterizedTest
@CsvSource({"1, foo", "2, bar"})
void testWithTwoParams(String a) { } // Only 1 param, but CSV has 2

// Cause 2: Wrong type conversion
@ParameterizedTest
@ValueSource(ints = {1, 2, 3})
void testStringParam(String value) { } // int supplied, String expected

// Cause 3: Empty arguments source
@ParameterizedTest
@CsvSource({})
void testEmpty() { } // No arguments provided
```

## How to Fix

### Fix 1: Match parameter count and types with @CsvSource

Ensure the number and types of parameters in your test method match the CSV values provided.

```java
@ParameterizedTest
@CsvSource({
    "Alice, 30, true",
    "Bob, 25, false",
    "Charlie, 35, true"
})
void shouldProcessUsers(String name, int age, boolean active) {
    User user = new User(name, age, active);
    assertNotNull(user.getName());
    assertEquals(age, user.getAge());
}

// Use quoted strings for values with commas
@ParameterizedTest
@CsvSource({
    "'New York, NY', 8336817",
    "'Los Angeles, CA', 3979576"
})
void shouldParseCity(String city, int population) {
    assertTrue(population > 0);
}
```

### Fix 2: Use @MethodSource for complex parameter types

For complex test data that cannot be expressed in CSV, use @MethodSource with a static method that returns argument streams.

```java
@ParameterizedTest
@MethodSource("userProvider")
void shouldValidateAllUsers(User user, ExpectedResult expected) {
    ValidationResult result = validator.validate(user);
    assertEquals(expected.isValid(), result.isValid());
}

static Stream<Arguments> userProvider() {
    return Stream.of(
        Arguments.of(
            new User("Alice", 30),
            ExpectedResult.valid()
        ),
        Arguments.of(
            new User("", -1),
            ExpectedResult.invalid("name", "age")
        )
    );
}

// For enum-based parameterized tests
@ParameterizedTest
@EnumSource(value = PaymentMethod.class, names = {"CREDIT_CARD", "DEBIT_CARD"})
void shouldProcessCardPayments(PaymentMethod method) {
    assertTrue(method.isCardBased());
}
```

### Fix 3: Use @CsvFileSource for large datasets

When parameterized tests need many test cases, load them from a CSV file instead of inline values.

```java
@ParameterizedTest
@CsvFileSource(
    resources = "/test-data/users.csv",
    numLinesToSkip = 1
)
void shouldImportUsers(String name, String email, int age) {
    User user = importService.importUser(name, email, age);
    assertNotNull(user);
    assertEquals(name, user.getName());
}

// resources/test-data/users.csv:
// name,email,age
// Alice,alice@example.com,30
// Bob,bob@example.com,25
// Charlie,charlie@example.com,35
```

## Related Errors

- {{< relref "junit5-extension" >}} — ExtensionConfigurationException
- {{< relref "junit5-assertion" >}} — Assertion Failure

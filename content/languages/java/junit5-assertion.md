---
title: "[Solution] AssertionFailedError — JUnit 5 Assertion Failure Fix"
description: "Fix JUnit 5 assertion failures. Resolve 'expected: <X> but was: <Y>' errors and assertion message issues."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# AssertionFailedError — JUnit 5 Assertion Failure Fix

An `AssertionFailedError` with "expected: <X> but was: <Y>" means a JUnit 5 assertion detected that the actual result does not match the expected value. While this is normal test behavior for failing tests, persistent assertion failures indicate bugs in the code being tested or incorrect test expectations.

## What This Error Means

Common messages:

- `org.opentest4j.AssertionFailedError: expected: <true> but was: <false>`
- `AssertionFailedError: expected: <42> but was: <0>`
- `AssertionFailedError: expected: <[Alice, Bob]> but was: <[]>`

## Common Causes

```java
// Cause 1: Incorrect expected value
@Test
void shouldCalculateTax() {
    assertEquals(0.08, calculator.calculateTax(100.0)); // Actual: 0.08
    assertEquals(0.08, calculator.calculateTax(100.0)); // Precision issue?
}

// Cause 2: Floating point comparison without tolerance
@Test
void shouldComputePi() {
    assertEquals(3.14159, math.pi(), 0.00001); // Too precise
}

// Cause 3: Comparing objects without equals() override
@Test
void shouldMatchUsers() {
    User expected = new User("Alice", 30);
    User actual = userService.findById(1L);
    assertEquals(expected, actual); // No equals() — always fails
}

// Cause 4: Side effects not accounted for
@Test
void shouldNotModifyOriginalList() {
    List<String> original = new ArrayList<>(List.of("a", "b"));
    service.sort(original);
    assertEquals(List.of("a", "b"), original); // sort modified it!
}
```

## How to Fix

### Fix 1: Use descriptive assertion messages and expected values

Provide clear assertion messages and verify expected values match the actual behavior of the code.

```java
class CalculatorTest {

    @Test
    void shouldAddTwoNumbers() {
        Calculator calc = new Calculator();
        int result = calc.add(2, 3);
        assertEquals(5, result, "2 + 3 should equal 5");
    }

    @Test
    void shouldCalculateTax() {
        Calculator calc = new Calculator();
        double tax = calc.calculateTax(100.0, 0.08);
        assertEquals(8.0, tax, 0.001,
            "8% tax on $100 should be $8.00");
    }

    @Test
    void shouldReturnEmptyListForNoMatches() {
        List<String> results = searchService.find("nonexistent");
        assertTrue(results.isEmpty(),
            "Search for nonexistent term should return empty list");
    }
}
```

### Fix 2: Use appropriate assertions for collection comparisons

Use assertThat with AssertJ or specific collection assertions for better error messages and readability.

```java
import static org.assertj.core.api.Assertions.*;

class UserServiceTest {

    @Test
    void shouldReturnActiveUsers() {
        List<User> users = userService.getActiveUsers();

        assertThat(users)
            .isNotEmpty()
            .hasSize(3)
            .extracting(User::getName)
            .containsExactly("Alice", "Bob", "Charlie");
    }

    @Test
    void shouldSortUsersByName() {
        List<User> sorted = userService.sortByName();

        assertThat(sorted)
            .isSortedAccordingTo(
                Comparator.comparing(User::getName))
            .allSatisfy(user -> {
                assertThat(user.getName()).isNotBlank();
            });
    }

    @Test
    void shouldThrowOnInvalidInput() {
        assertThatThrownBy(() -> userService.register("", null))
            .isInstanceOf(IllegalArgumentException.class)
            .hasMessageContaining("name cannot be blank");
    }
}
```

### Fix 3: Implement equals() and hashCode() for domain objects

Implement proper equals() and hashCode() methods on domain objects to enable reliable object comparison in tests.

```java
public class User {
    private final Long id;
    private final String name;
    private final String email;

    // Constructor...

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return Objects.equals(id, user.id)
            && Objects.equals(name, user.name)
            && Objects.equals(email, user.email);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name, email);
    }
}

// Or use records for automatic equals/hashCode
public record User(Long id, String name, String email) {}
```

## Related Errors

- {{< relref "junit5-timeout" >}} — Test Timeout Error
- {{< relref "junit5" >}} — JUnit Platform Launcher Error

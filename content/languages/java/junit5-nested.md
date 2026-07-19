---
title: "[Solution] JUnitException — Nested Test Class Error Fix"
description: "Fix JUnit5 nested test class errors. Resolve 'Cannot resolve method' and test discovery failures with @Nested inner classes."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# JUnitException — Nested Test Class Error Fix

A `JUnitException` with "Cannot resolve method" in the context of nested test classes means JUnit 5 cannot properly discover or execute tests within `@Nested` inner classes. This is often caused by incorrect test class structure, missing `@Nested` annotation, or static inner classes.

## What This Error Means

Common messages:

- `org.junit.platform.commons.JUnitException: Cannot resolve method`
- `JUnitException: Method 'testSomething' not found in class`
- `NoClassDefFoundError when executing nested tests`

## Common Causes

```java
// Cause 1: Missing @Nested annotation
class OrderTest {
    class OrderCreationTest { // Missing @Nested!
        @Test
        void shouldCreateOrder() { }
    }
}

// Cause 2: Static nested class used as @Nested
class OrderTest {
    @Nested
    static class OrderCreationTest { // Static not allowed!
        @Test
        void shouldCreateOrder() { }
    }
}

// Cause 3: @BeforeEach in outer class accessing inner state
class OrderTest {
    private Order order;

    @BeforeEach
    void setUp() {
        order = new Order(); // Used by nested tests
    }

    @Nested
    class ValidOrderTest {
        @Test
        void shouldValidate() {
            order.validate(); // order is null!
        }
    }
}
```

## How to Fix

### Fix 1: Structure nested test classes properly

Use @Nested on non-static inner classes and organize tests by behavior within the outer class.

```java
class OrderTest {

    private Order order;

    @BeforeEach
    void setUp() {
        order = new Order();
    }

    @Nested
    class WhenOrderIsEmpty {

        @Test
        void shouldNotAllowCheckout() {
            assertFalse(order.canCheckout());
        }

        @Test
        void shouldHaveZeroTotal() {
            assertEquals(Money.ZERO, order.total());
        }
    }

    @Nested
    class WhenOrderHasItems {

        @BeforeEach
        void addItems() {
            order.addItem(new OrderItem("Widget", 2, Money.of(9.99)));
            order.addItem(new OrderItem("Gadget", 1, Money.of(19.99)));
        }

        @Test
        void shouldCalculateTotal() {
            assertEquals(Money.of(39.97), order.total());
        }

        @Test
        void shouldAllowCheckout() {
            assertTrue(order.canCheckout());
        }
    }
}
```

### Fix 2: Use @DisplayName for clear nested test reporting

Add @DisplayName to nested test classes for human-readable test output in build reports.

```java
@DisplayName("Order Processing")
class OrderTest {

    @Nested
    @DisplayName("when the cart is empty")
    class EmptyCartTests {
        @Test
        @DisplayName("should show empty cart message")
        void shouldShowEmptyMessage() {
            Cart cart = new Cart();
            assertEquals("Your cart is empty", cart.getMessage());
        }
    }

    @Nested
    @DisplayName("when items are added to the cart")
    class CartWithItemsTests {
        @Test
        @DisplayName("should calculate total with tax")
        void shouldCalculateTotal() {
            Cart cart = new Cart();
            cart.add(new Item("Book", 10.00));
            assertEquals(10.80, cart.totalWithTax());
        }
    }
}
```

### Fix 3: Share state using outer class fields with proper lifecycle

Use non-static fields in the outer class to share state, relying on JUnit 5's lifecycle to initialize them correctly.

```java
class UserServiceTest {

    private UserRepository userRepository;
    private UserService userService;

    @BeforeEach
    void setUp() {
        userRepository = Mockito.mock(UserRepository.class);
        userService = new UserService(userRepository);
    }

    @Nested
    class Registration {

        @Test
        void shouldRegisterNewUser() {
            when(userRepository.save(any())).thenAnswer(
                inv -> inv.getArgument(0));

            User user = userService.register("alice@example.com");
            assertNotNull(user.getId());
            assertEquals("alice@example.com", user.getEmail());
        }
    }

    @Nested
    class Authentication {

        @Test
        void shouldAuthenticateWithValidCredentials() {
            when(userRepository.findByEmail("alice@example.com"))
                .thenReturn(Optional.of(new User("Alice", "pass123")));

            assertTrue(userService.authenticate(
                "alice@example.com", "pass123"));
        }
    }
}
```

## Related Errors

- {{< relref "junit5" >}} — JUnit Platform Launcher Error
- {{< relref "junit5-timeout" >}} — Test Timeout Error

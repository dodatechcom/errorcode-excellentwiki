---
title: "[Solution] AssertionFailedError — JUnit 5 Test Timeout Fix"
description: "Fix JUnit 5 test timeout errors. Resolve 'execution timed out' and slow test issues with proper timeout configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# AssertionFailedError — JUnit 5 Test Timeout Fix

A test timeout error occurs when a test method takes longer than the configured maximum execution time. JUnit 5 interrupts or fails the test when it exceeds the timeout, causing an `AssertionFailedError` with "execution timed out".

## What This Error Means

Common messages:

- `org.junit.opentest4j.AssertionFailedError: execution timed out`
- `AssertionFailedError: Execution timed out after 5000 ms`
- `TestTimedOutException: test timed out after 10 seconds`

## Common Causes

```java
// Cause 1: Infinite loop in test
@Test
void testWithInfiniteLoop() {
    while (true) { } // Never terminates
}

// Cause 2: Network call in test without mock
@Test
void testExternalService() {
    // Calls real external service — slow or hangs
    response = httpClient.get("https://external-api.com/data");
}

// Cause 3: Waiting on lock or resource
@Test
void testWithBlockingCall() {
    blockingQueue.take(); // Blocks indefinitely if queue is empty
}

// Cause 4: Timeout too short for actual workload
@Test
@Timeout(1) // 1 second too short for complex operation
void complexOperation() { }
```

## How to Fix

### Fix 1: Use @Timeout annotation with appropriate value

Set reasonable timeouts based on the operation being tested. Use TimeUnit for clarity.

```java
import org.junit.jupiter.api.Timeout;
import java.util.concurrent.TimeUnit;

class UserServiceTest {

    @Test
    @Timeout(value = 5, unit = TimeUnit.SECONDS)
    void shouldProcessOrderInReasonableTime() {
        Order order = createLargeOrder();
        OrderResult result = service.process(order);
        assertNotNull(result);
    }

    @Nested
    @Timeout(value = 30, unit = TimeUnit.SECONDS)
    class IntegrationTests {

        @Test
        void shouldCompleteEndToEndWorkflow() {
            // Long-running integration test
        }
    }
}
```

### Fix 2: Mock external dependencies to avoid real calls

Replace real network calls, database queries, and file I/O with mocks to ensure tests run quickly and reliably.

```java
@SpringBootTest
class PaymentServiceTest {

    @MockBean
    private PaymentGateway paymentGateway;

    @MockBean
    private EmailService emailService;

    @Autowired
    private PaymentService paymentService;

    @Test
    @Timeout(5)
    void shouldProcessPayment() {
        when(paymentGateway.charge(any()))
            .thenReturn(PaymentResult.success("txn_123"));

        PaymentResult result = paymentService.processPayment(
            new PaymentRequest(100.00, "card_4242"));

        assertTrue(result.isSuccess());
        assertEquals("txn_123", result.getTransactionId());
        verify(emailService).sendConfirmation(any());
    }
}
```

### Fix 3: Use assertTimeoutPreemptively for deadline assertions

Use assertTimeoutPreemptively to fail a test if an operation takes too long, without requiring the @Timeout annotation.

```java
import static org.junit.jupiter.api.Assertions.assertTimeoutPreemptively;
import java.time.Duration;

class PerformanceTest {

    @Test
    void shouldCompleteSearchWithinDeadline() {
        assertTimeoutPreemptively(Duration.ofSeconds(3), () -> {
            List<Result> results = searchService
                .search("complex query with many filters");
            assertFalse(results.isEmpty());
        });
    }

    @Test
    void databaseQueryShouldBeFast() {
        assertTimeoutPreemptively(Duration.ofMillis(500), () -> {
            User user = userRepository.findById(1L)
                .orElseThrow();
            assertNotNull(user.getName());
        });
    }
}
```

## Related Errors

- {{< relref "junit5-assertion" >}} — Assertion Failure
- {{< relref "junit5-extension" >}} — ExtensionConfigurationException

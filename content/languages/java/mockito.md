---
title: "[Solution] Mockito Misuse Error — Mock Framework Fix"
description: "Fix common Mockito misuse: strict stubbing, unstubbed method calls, and verification errors in unit tests."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["mockito", "testing", "mock", "stubbing", "unit-test"]
weight: 5
---

# Mockito Misuse Error — Mock Framework Fix

Mockito misuse errors occur when mocking is done incorrectly. Common issues include strict stubbing violations, calling unstubbed methods, and verification failures.

## What This Error Means

Common messages:

- `Unnecessary stubbings detected`
- `Wanted but not invoked`
- `Actually, there were zero interactions with this mock`

## Common Causes

```java
// Cause 1: Strict stubbing — unused stubs
when(mockService.getData()).thenReturn("data");
// Never called getData()

// Cause 2: Calling method on real object instead of mock
@InjectMocks
MyService myService;
@Mock
ExternalService externalService;

// Cause 3: Mocking final class
final class FinalClass { }
// Mockito cannot mock final classes by default
```

## How to Fix

### Fix 1: Remove unnecessary stubs or use lenient mode

```java
lenient().when(mockService.getData()).thenReturn("data");
```

### Fix 2: Use @ExtendWith properly

```java
@ExtendWith(MockitoExtension.class)
class MyServiceTest {

    @Mock
    private ExternalService externalService;

    @InjectMocks
    private MyService myService;

    @Test
    void testSomething() {
        when(externalService.getData()).thenReturn("data");
        String result = myService.process();
        assertEquals("data", result);
    }
}
```

### Fix 3: Verify correctly

```java
verify(mockService, times(1)).save(expectedEntity);
```

### Fix 4: Enable mockito-inline for final classes

```xml
<dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-inline</artifactId>
    <scope>test</scope>
</dependency>
```

## Related Errors

- {{< relref "junit5" >}} — JUnit platform launcher error
- {{< relref "testcontainers" >}} — Testcontainers startup failure
- {{< relref "assertionerror" >}} — General assertion error

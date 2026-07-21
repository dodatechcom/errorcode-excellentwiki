---
title: "[Solution] Spring Test Context Cache Error"
description: "Fix Spring test context cache errors when tests fail due to stale or shared application context."
frameworks: ["spring"]
error-types: ["test-error"]
severities: ["error"]
---

Test context cache errors occur when Spring caches an application context that has stale beans or configuration from a previous test class.

## Common Causes

- Different test classes share cached context with wrong configuration
- `@DirtiesContext` not used when needed
- Test configuration changes not reflected
- Context loaded with different profiles than expected
- Memory exhaustion from too many cached contexts

## How to Fix

### Use @DirtiesContext

```java
@SpringBootTest
@DirtiesContext(classMode = ClassMode.AFTER_CLASS)
class MyTest {
    // Application context is recreated after this test class
}
```

### Use Distinct Context Configurations

```java
@SpringBootTest(classes = TestConfig1.class)
class Test1 {}

@SpringBootTest(classes = TestConfig2.class)
class Test2 {}
// Different configurations = different contexts
```

### Reset Context Between Tests

```java
@SpringBootTest
@ActiveProfiles("test")
@DirtiesContext(classMode = ClassMode.BEFORE_EACH_TEST_METHOD)
class MyTest {
    // Fresh context for each test method
}
```

### Monitor Context Cache

```java
// application-test.yml
logging:
  level:
    org.springframework.test.context: DEBUG
```

## Examples

```java
// Bug -- stale context
@SpringBootTest
class Test1 {
    @Autowired
    private Config config;
    // Config value: "production"
}

@SpringBootTest
class Test2 {
    @Autowired
    private Config config;
    // May still have "production" from Test1's context
}

// Fix -- use @DirtiesContext
@SpringBootTest
@DirtiesContext(classMode = ClassMode.AFTER_CLASS)
class Test1 {}

@SpringBootTest
class Test2 {
    // Fresh context loaded
}
```

---
title: "[Solution] Spring Batch Retry Error"
description: "Fix Spring batch retry errors when failed items are not retried or retry policy causes infinite loops."
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
---

Batch retry errors occur when the retry policy is not configured, causing items to fail immediately or retry indefinitely.

## Common Causes

- Retry policy not configured on chunk operations
- Retry limit exceeded without skip policy
- Exception not included in retryable exceptions
- Skip limit not set, causing job to fail on first error
- Backoff policy not configured

## How to Fix

### Configure Retry Policy

```java
@Bean
public Step importStep(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
    return new StepBuilder("importStep", jobRepository)
        .<User, User>chunk(100, transactionManager)
        .reader(userReader())
        .processor(userProcessor())
        .writer(userWriter())
        .faultTolerant()
        .retryLimit(3)
        .retry(FlatFileParseException.class)
        .retry(DataIntegrityViolationException.class)
        .skipLimit(10)
        .skip(ValidationException.class)
        .build();
}
```

### Configure Backoff Policy

```java
@Bean
public Step importStep(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
    return new StepBuilder("importStep", jobRepository)
        .<User, User>chunk(100, transactionManager)
        .reader(userReader())
        .processor(userProcessor())
        .writer(userWriter())
        .faultTolerant()
        .retryLimit(3)
        .retry(TransientDataAccessException.class)
        .backoffOptions(1000, 2.0, 10000)  // initial, multiplier, max
        .build();
}
```

### Handle Skip

```java
.faultTolerant()
.skipLimit(5)
.skip(ValidationException.class)
.skipPolicy(new AlwaysSkipItemSkipPolicy())
```

## Examples

```java
// Bug -- no retry or skip
@Bean
public Step importStep(...) {
    return new StepBuilder("importStep", ...)
        .<User, User>chunk(100, transactionManager)
        .reader(reader())
        .writer(writer())
        .build();  // Fails on first error
}

// Fix -- add retry and skip
.faultTolerant()
.retryLimit(3)
.retry(DatabaseAccessException.class)
.skipLimit(10)
.skip(ValidationException.class)
```

---
title: "JobExecutionException - Spring Batch"
description: "Spring Batch throws JobExecutionException when a batch job fails during execution"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a Spring Batch job fails during any phase of execution (reader, processor, writer). It throws `JobExecutionException` with details about the failed step.

## Common Causes

- Database connection lost during chunk processing
- Reader reads data that processor cannot handle
- Writer fails due to constraint violations
- Job repository cannot persist job state
- Item size exceeds configured limits

## How to Fix

1. Configure skip and retry policies:

```java
@Bean
public Job importUsersJob(JobRepository jobRepository, Step importStep) {
    return new JobBuilder("importUsers", jobRepository)
        .start(importStep)
        .build();
}

@Bean
public Step importStep(JobRepository jobRepository, PlatformTransactionManager txManager) {
    return new StepBuilder("importStep", jobRepository)
        .<User, User>chunk(100, txManager)
        .reader(userReader(null))
        .processor(userProcessor())
        .writer(userWriter())
        .faultTolerant()
        .skipLimit(10)
        .skip(FlatFileParseException.class)
        .retryLimit(3)
        .retry(DataAccessException.class)
        .build();
}
```

2. Implement skip listener for failed items:

```java
@Component
public class SkipListenerImpl implements SkipListener<User, User> {

    @Override
    public void onSkipInRead(Throwable t) {
        log.error("Skip in read: {}", t.getMessage());
    }

    @Override
    public void onSkipInWrite(User item, Throwable t) {
        log.error("Skip in write for user {}: {}", item.getId(), t.getMessage());
        failedItemsRepository.save(item);
    }
}
```

3. Configure job repository health checks:

```java
@Bean
public JobExplorer jobExplorer(DataSource dataSource) {
    return new JobExplorerFactoryBean(dataSource).getObject();
}
```

## Examples

```java
// Reader throws exception on 500th record
// JobExecutionException: Step importStep failed
// Job: importUsers failed with status FAILED
```

## Related Errors

- [Integration error]({{< relref "/frameworks/spring/spring-integration-error" >}})
- [GraphQL error]({{< relref "/frameworks/spring/spring-graphql-error" >}})

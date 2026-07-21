---
title: "[Solution] Spring Scheduling or Async Error -- How to Fix"
description: "Fix Spring scheduling and async errors. Resolve task scheduling failures, thread pool, and async processing issues."
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Spring scheduling or async error occurs when `@Scheduled` tasks fail, `@Async` methods don't execute, or thread pool configuration is incorrect. These features rely on proper configuration and thread management.

## Why It Happens

Spring scheduling uses a task scheduler, and async processing uses a task executor. Errors occur when `@EnableScheduling` or `@EnableAsync` is missing, when the default thread pool is too small, when async methods return non-void types without `Future`, when exceptions in scheduled tasks crash the scheduler, or when transaction boundaries are incorrect in async methods.

## Common Error Messages

```
org.springframework.scheduling.SchedulingException: Could not schedule task
```

```
java.lang.IllegalStateException: @EnableAsync annotation not found
```

```
java.util.concurrent.RejectedExecutionException: Task rejected from ThreadPoolExecutor
```

```
org.springframework.aop.AopInvocationException: Null return value from advice does not match
```

## How to Fix It

### 1. Enable Scheduling and Async

Add the required annotations to the configuration:

```java
@Configuration
@EnableScheduling
@EnableAsync
public class AsyncConfig {

    @Bean
    public TaskScheduler taskScheduler() {
        ThreadPoolTaskScheduler scheduler = new ThreadPoolTaskScheduler();
        scheduler.setPoolSize(10);
        scheduler.setThreadNamePrefix("scheduler-");
        scheduler.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());
        return scheduler;
    }

    @Bean
    public TaskExecutor asyncExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);
        executor.setMaxPoolSize(20);
        executor.setQueueCapacity(100);
        executor.setThreadNamePrefix("async-");
        executor.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());
        executor.initialize();
        return executor;
    }
}
```

### 2. Implement Scheduled Tasks

Create reliable scheduled tasks:

```java
@Component
public class ScheduledTasks {

    private static final Logger log = LoggerFactory.getLogger(ScheduledTasks.class);

    // Fixed rate (every 5 seconds)
    @Scheduled(fixedRate = 5000)
    public void pollData() {
        try {
            dataService.fetchUpdates();
        } catch (Exception e) {
            log.error("Error polling data: ", e);
            // Don't let exceptions kill the scheduler
        }
    }

    // Fixed delay (5 seconds after previous completion)
    @Scheduled(fixedDelay = 5000)
    public void cleanupExpiredSessions() {
        sessionService.cleanupExpired();
    }

    // Cron expression (every hour at :00)
    @Scheduled(cron = "0 0 * * * *")
    public void generateReport() {
        reportService.generateDailyReport();
    }

    // With initial delay
    @Scheduled(fixedRate = 60000, initialDelay = 5000)
    public void syncData() {
        syncService.synchronize();
    }
}
```

### 3. Configure Async Methods

Implement async processing correctly:

```java
@Service
public class NotificationService {

    // Fire-and-forget async method
    @Async
    public void sendEmailAsync(String to, String subject, String body) {
        try {
            emailClient.send(to, subject, body);
        } catch (Exception e) {
            log.error("Failed to send email to {}: {}", to, e.getMessage());
        }
    }

    // Async with result
    @Async("asyncExecutor")
    public CompletableFuture<String> processLargeDataset(Long datasetId) {
        try {
            String result = dataProcessor.process(datasetId);
            return CompletableFuture.completedFuture(result);
        } catch (Exception e) {
            return CompletableFuture.failedFuture(e);
        }
    }

    // Async with exception handling
    @Async
    @Transactional
    public void asyncTransaction(DataUpdate update) {
        try {
            dataRepository.save(update);
            auditService.log(update);
        } catch (Exception e) {
            log.error("Async transaction failed: ", e);
            throw new AsyncException("Transaction failed", e);
        }
    }
}
```

### 4. Handle Async Exceptions

Configure async exception handling:

```java
@Component
public class AsyncExceptionHandler implements AsyncUncaughtExceptionHandler {

    private static final Logger log = LoggerFactory.getLogger(AsyncExceptionHandler.class);

    @Override
    public void handleUncaughtException(Throwable ex, Method method, Object... params) {
        log.error("Async method {} threw exception: {}",
            method.getName(), ex.getMessage(), ex);

        // Optionally notify admin
        adminService.notifyAsyncFailure(method.getName(), ex);
    }
}

// Register in config
@Configuration
@EnableAsync
public class AsyncConfig implements AsyncConfigurer {

    @Override
    public AsyncUncaughtExceptionHandler getAsyncUncaughtExceptionHandler() {
        return new AsyncExceptionHandler();
    }

    @Override
    public Executor getAsyncExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);
        executor.setMaxPoolSize(10);
        executor.setQueueCapacity(25);
        executor.initialize();
        return executor;
    }
}
```

## Common Scenarios

**Scenario 1: `@Async` method runs synchronously.**
This happens when `@EnableAsync` is missing from the configuration class. The method still executes but not asynchronously.

**Scenario 2: Scheduled task stops after an exception.**
Uncaught exceptions can terminate the scheduler thread. Always wrap scheduled task logic in try-catch blocks.

**Scenario 3: Thread pool exhaustion.**
When too many async tasks are submitted, the queue fills up and tasks are rejected. Increase pool size or use appropriate rejection policies.

## Prevent It

1. **Always configure thread pool sizes** explicitly instead of relying on defaults.

2. **Wrap scheduled tasks in try-catch** to prevent exceptions from stopping the scheduler.

3. **Use `@Async` with `@Transactional` carefully** -- the transaction runs in a separate thread and may not behave as expected.

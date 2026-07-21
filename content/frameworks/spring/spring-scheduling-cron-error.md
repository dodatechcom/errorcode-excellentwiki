---
title: "[Solution] Spring Scheduling Cron Error"
description: "Fix Spring scheduling cron expression errors when tasks run at unexpected times or fail to trigger."
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
---

Cron expression errors occur when the cron syntax is invalid, the timezone is wrong, or the task does not execute as expected.

## Common Causes

- Invalid cron expression syntax
- Timezone not specified, causing UTC default
- Task runs once instead of repeatedly
- Cron expression matches wrong times
- `@Scheduled` on private method (Spring proxy issue)

## How to Fix

### Write Correct Cron Expressions

```java
@Component
public class ScheduledTasks {
    // Every minute
    @Scheduled(cron = "0 * * * * *")
    public void everyMinute() {}

    // Every day at 2:30 AM
    @Scheduled(cron = "0 30 2 * * *")
    public void dailyAt230() {}

    // Every weekday at 9 AM
    @Scheduled(cron = "0 0 9 * * MON-FRI")
    public void weekdayMorning() {}

    // Every 15 minutes between 8 AM and 6 PM
    @Scheduled(cron = "0 0/15 8-18 * * *")
    public void businessHours() {}
}
```

### Specify Timezone

```java
@Scheduled(cron = "0 0 2 * * *", zone = "America/New_York")
public void dailyTask() {
    // Runs at 2 AM Eastern Time
}
```

### Use Fixed Rate Instead

```java
@Scheduled(fixedRate = 60000)  // Every 60 seconds
public void runEveryMinute() {}

@Scheduled(fixedDelay = 60000)  // 60 seconds after previous completes
public void runAfterDelay() {}
```

## Examples

```java
// Bug -- missing seconds field
@Scheduled(cron = "* * * * *")  // 5 fields, Spring needs 6

// Fix -- add seconds
@Scheduled(cron = "0 * * * * *")  // 6 fields

// Bug -- private method
@Scheduled(fixedRate = 60000)
private void privateTask() {}  // Not proxied by Spring

// Fix -- make public
@Scheduled(fixedRate = 60000)
public void publicTask() {}
```

Cron format: `second minute hour day-of-month month day-of-week`

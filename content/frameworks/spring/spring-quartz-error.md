---
title: "[Solution] Spring Quartz Scheduler Error"
description: "Fix Spring Quartz scheduler errors when jobs fail to execute, misfire, or cause database errors."
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
---

Quartz errors occur when job configuration is wrong, trigger misfires, or the job store fails to persist job data.

## Common Causes

- Job class not implementing `Job` interface
- Trigger misfire instruction not configured
- Job store not properly configured for clustering
- Concurrent execution not allowed for job
- Job data map not properly serialized

## How to Fix

### Configure Quartz

```yaml
# application.yml
spring:
  quartz:
    job-store-type: jdbc
    jdbc:
      initialize-schema: always
    properties:
      org.quartz.scheduler.instanceName: MyScheduler
      org.quartz.scheduler.instanceId: AUTO
      org.quartz.jobStore.class: org.quartz.impl.jdbcjobstore.JobStoreTX
      org.quartz.jobStore.driverDelegateClass: org.quartz.impl.jdbcjobstore.PostgreSQLDelegate
      org.quartz.jobStore.tablePrefix: QRTZ_
      org.quartz.jobStore.isClustered: true
      org.quartz.threadPool.threadCount: 10
```

### Define Quartz Job

```java
@Component
public class SampleJob implements Job {
    @Override
    public void execute(JobExecutionContext context) {
        JobDataMap dataMap = context.getMergedJobDataMap();
        String message = dataMap.getString("message");
        log.info("Executing job with message: {}", message);
    }
}
```

### Schedule Jobs Programmatically

```java
@Service
public class JobScheduler {
    @Autowired
    private Scheduler scheduler;

    public void scheduleJob(String name, String message, Date startTime) throws SchedulerException {
        JobDetail job = JobBuilder.newJob(SampleJob.class)
            .withIdentity(name)
            .usingJobData("message", message)
            .build();

        Trigger trigger = TriggerBuilder.newTrigger()
            .withIdentity(name + "_trigger")
            .startAt(startTime)
            .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                .withIntervalInMinutes(5)
                .repeatForever())
            .build();

        scheduler.scheduleJob(job, trigger);
    }
}
```

## Examples

```java
// Bug -- job does not implement Job interface
public class BrokenJob {
    public void execute() {}  // Not called by Quartz
}

// Fix -- implement Job interface
public class WorkingJob implements Job {
    @Override
    public void execute(JobExecutionContext context) {
        // Called by Quartz
    }
}
```

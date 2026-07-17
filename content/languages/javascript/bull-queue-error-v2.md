---
title: "[Solution] Bull: Job Processing Failed Fix"
description: "Fix Bull queue job processing failures. Handle stalled jobs, retry strategies, and worker error handling."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["bull", "redis", "queue", "job", "worker", "background"]
weight: 5
---

# Bull: Job Processing Failed

This error occurs when a Bull queue job fails during processing. Bull tracks job status and moves failed jobs to a failed set, optionally retrying them based on configured strategies.

## What This Error Means

Common error messages:

- `Error: Job failed with status "failed"`
- `Uncaught error in processor: Error: Connection refused`
- ` stalled interval: job stalled`
- `Missing script: process.nextTick`
- `Job ${jobId} failed: ${error.message}`

Bull uses Redis to store job data. When a processor (worker) throws an error or doesn't complete within the stalled interval, the job is marked as failed.

## Common Causes

```javascript
// Cause 1: Processor throws an error
const emailQueue = new Bull('emails');

emailQueue.process(async (job) => {
  await sendEmail(job.data.to); // throws if SMTP fails
});

// Cause 2: Job data is malformed
emailQueue.add({ /* missing required fields */ });

// Cause 3: Redis connection lost during processing
// Redis server restarts while job is running

// Cause 4: Stalled job (took too long)
// Default stalledInterval is 30 seconds
// Long-running job appears stalled to Bull

// Cause 5: Concurrency exceeded
emailQueue.process(5, async (job) => {
  await heavyOperation(job.data); // 5 concurrent jobs, all may fail
});
```

## How to Fix

### Fix 1: Add proper error handling in processors

```javascript
const emailQueue = new Bull('emails');

emailQueue.process(async (job) => {
  try {
    await sendEmail(job.data.to);
    return { success: true };
  } catch (err) {
    job.log(`Failed to send email: ${err.message}`);
    throw err; // let Bull handle retry
  }
});

emailQueue.on('failed', (job, err) => {
  console.error(`Job ${job.id} failed: ${err.message}`);
});

emailQueue.on('completed', (job) => {
  console.log(`Job ${job.id} completed`);
});
```

### Fix 2: Configure retry strategies

```javascript
const emailQueue = new Bull('emails', {
  defaultJobOptions: {
    removeOnComplete: 100,
    removeOnFail: 50,
    attempts: 3,
    backoff: {
      type: 'exponential',
      delay: 2000,
    },
  },
});
```

### Fix 3: Increase stalled interval for long jobs

```javascript
const queue = new Bull('heavy-tasks', {
  settings: {
    stalledInterval: 120000, // 2 minutes
    maxStalledCount: 3,
  },
});
```

### Fix 4: Handle specific error types for retry decisions

```javascript
emailQueue.process(async (job) => {
  try {
    await sendEmail(job.data.to);
  } catch (err) {
    if (err.code === 'ECONNRESET' || err.code === 'ETIMEDOUT') {
      throw err; // retryable
    }
    // Non-retryable error — don't throw, mark as failed
    await job.log('Non-retryable error: ' + err.message);
    return false;
  }
});
```

### Fix 5: Use global error handler

```javascript
const queueEvents = new QueueEvents('emails');

queueEvents.on('failed', ({ jobId, failedReason }) => {
  console.error(`Job ${jobId} failed: ${failedReason}`);
  // Send alert to monitoring system
});

queueEvents.on('stalled', ({ jobId }) => {
  console.warn(`Job ${jobId} stalled`);
});
```

## Examples

```
Job 42 failed: connect ECONNREFUSED 127.0.0.1:6379
Error: stalled interval job stalled
```

```javascript
// Fix: add dead letter queue for permanently failed jobs
const dlq = new Bull('emails-dlq');

emailQueue.on('failed', async (job, err) => {
  if (job.attemptsMade >= job.opts.attempts) {
    await dlq.add(job.data, {
      failedReason: err.message,
      originalJobId: job.id,
    });
  }
});
```

## Related Errors

- [Bull Queue Error]({{< relref "/languages/javascript/bull-queue-error" >}}) — basic queue error
- [Redis Error V2]({{< relref "/languages/javascript/go-redis-error-v2" >}}) — Redis connection error
- [Socket.IO Error V2]({{< relref "/languages/javascript/socket-io-error-v2" >}}) — connection error

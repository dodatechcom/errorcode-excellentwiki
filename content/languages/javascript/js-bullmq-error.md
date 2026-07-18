---
title: "Solved JavaScript BullMQ Error — How to Fix"
date: 2026-03-20T14:10:00+00:00
description: "Learn how to resolve JavaScript BullMQ job queue, worker, and Redis connection errors."
categories: ["javascript"]
keywords: ["bullmq error", "bullmq queue", "job queue", "bullmq worker", "queue error"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

BullMQ errors occur when the Redis-based job queue encounters connection issues, job processing failures, or worker configuration problems. The library requires stable Redis connections for reliable job processing.

Common causes include:
- Redis connection lost during job processing
- Job data exceeding Redis memory limits
- Worker concurrency causing race conditions
- Job retry configuration not properly set
- Stalled job detection triggering premature failures

## Common Error Messages

```
Error: Missing Redis client
```

```
Error: Job data is not serializable
```

```
Error: Stalled job detected
```

## How to Fix It

### 1. Configure BullMQ with Redis

Set up queue and worker with proper Redis options.

```javascript
import { Queue, Worker, QueueEvents } from "bullmq";
import Redis from "ioredis";

// Redis connection
const connection = new Redis({
  host: process.env.REDIS_HOST || "localhost",
  port: parseInt(process.env.REDIS_PORT) || 6379,
  password: process.env.REDIS_PASSWORD,
  maxRetriesPerRequest: null,
  enableReadyCheck: false
});

// Create queue
const emailQueue = new Queue("emails", {
  connection,
  defaultJobOptions: {
    removeOnComplete: 100,
    removeOnFail: 50,
    attempts: 3,
    backoff: {
      type: "exponential",
      delay: 2000
    }
  }
});

// Create worker
const worker = new Worker(
  "emails",
  async (job) => {
    console.log(`Processing job ${job.id}: ${job.data.email}`);
    
    // Simulate email sending
    await sendEmail(job.data);
    
    return { success: true, messageId: "123" };
  },
  {
    connection,
    concurrency: 5,
    limiter: {
      max: 10,
      duration: 1000
    }
  }
);

// Handle worker events
worker.on("completed", (job) => {
  console.log(`Job ${job.id} completed`);
});

worker.on("failed", (job, err) => {
  console.error(`Job ${job.id} failed:`, err.message);
});

worker.on("stalled", (jobId) => {
  console.warn(`Job ${jobId} stalled`);
});
```

### 2. Add Jobs with Options

Queue jobs with proper configuration.

```javascript
// Add single job
async function queueEmail(to, subject, body) {
  return emailQueue.add(
    "send-email",
    { to, subject, body },
    {
      priority: 1,
      delay: 0,
      removeOnComplete: true,
      removeOnFail: false
    }
  );
}

// Add bulk jobs
async function queueBulkEmails(emails) {
  const jobs = emails.map((email, i) => ({
    name: "send-email",
    data: email,
    opts: {
      priority: email.urgent ? 1 : 10,
      delay: i * 100 // Stagger sends
    }
  }));
  
  return emailQueue.addBulk(jobs);
}

// Delayed job
async function queueDelayedEmail(to, subject, body, delayMs) {
  return emailQueue.add(
    "send-email",
    { to, subject, body },
    { delay: delayMs }
  );
}

// Repeatable job
async function queueRecurringReport() {
  return emailQueue.add(
    "daily-report",
    { type: "daily" },
    {
      repeat: {
        pattern: "0 8 * * *" // Every day at 8am
      }
    }
  );
}
```

### 3. Monitor Queue Health

Track queue metrics and handle failures.

```javascript
import { QueueEvents } from "bullmq";

// Monitor queue events
const queueEvents = new QueueEvents("emails", { connection });

queueEvents.on("completed", ({ jobId }) => {
  console.log(`Job ${jobId} completed`);
});

queueEvents.on("failed", ({ jobId, failedReason }) => {
  console.error(`Job ${jobId} failed: ${failedReason}`);
});

queueEvents.on("stalled", ({ jobId }) => {
  console.warn(`Job ${jobId} stalled`);
});

// Get queue statistics
async function getQueueStats() {
  const counts = await emailQueue.getJobCounts(
    "wait",
    "active",
    "completed",
    "failed",
    "delayed"
  );
  
  return counts;
}

// Clean old jobs
async function cleanQueue() {
  await emailQueue.clean(1000, 100, "completed");
  await emailQueue.clean(1000, 100, "failed");
}

// Pause/resume queue
async function pauseQueue() {
  await emailQueue.pause();
}

async function resumeQueue() {
  await emailQueue.resume();
}
```

## Common Scenarios

### Scenario 1: Image Processing Queue

Process images asynchronously:

```javascript
const imageQueue = new Queue("image-processing", { connection });

const imageWorker = new Worker(
  "image-processing",
  async (job) => {
    const { imagePath, operations } = job.data;
    
    // Update progress
    await job.updateProgress(10);
    
    const result = await processImage(imagePath, operations);
    
    await job.updateProgress(100);
    
    return { outputPath: result.path };
  },
  { connection, concurrency: 3 }
);

// Queue image processing
async function processUploadedImages(imagePaths) {
  const jobs = imagePaths.map(path => ({
    name: "process",
    data: { imagePath: path, operations: ["resize", "optimize"] }
  }));
  
  return imageQueue.addBulk(jobs);
}
```

### Scenario 2: Email Queue with Rate Limiting

Send emails with rate limiting:

```javascript
const emailQueue = new Queue("emails", {
  connection,
  defaultJobOptions: {
    attempts: 3,
    backoff: { type: "exponential", delay: 5000 }
  }
});

const emailWorker = new Worker(
  "emails",
  async (job) => {
    const { to, subject, body, from } = job.data;
    
    try {
      await sendEmail({ to, subject, body, from });
      return { success: true };
    } catch (error) {
      if (error.code === "RATE_LIMITED") {
        throw new Error("Rate limited - retry later");
      }
      throw error;
    }
  },
  {
    connection,
    limiter: {
      max: 50,
      duration: 60000 // 50 emails per minute
    }
  }
);
```

## Prevent It

- Set `maxRetriesPerRequest: null` in Redis connection for BullMQ
- Use `removeOnComplete` and `removeOnFail` to prevent memory leaks
- Configure `stalledInterval` appropriately for your job duration
- Monitor queue counts to detect processing backlogs
- Use rate limiting (`limiter`) for external API calls
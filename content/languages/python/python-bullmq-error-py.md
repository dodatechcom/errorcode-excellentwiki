---
title: "[Solution] Python BullMQ Error — How to Fix"
description: "Fix Python BullMQ errors. Resolve worker, job, and Redis connection issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python BullMQ Error

A `bullmq.exceptions` or `redis.exceptions.ConnectionError` occurs when BullMQ fails to connect to Redis, encounters job execution errors, or when worker configuration is invalid.

## Why It Happens

BullMQ is a Redis-based job queue. Errors arise when Redis is unreachable, when job functions raise exceptions, when concurrency limits are exceeded, or when job options are invalid.

## Common Error Messages

- `ConnectionError: Error connecting to Redis`
- `bullmq.exceptions.JobError: Job failed`
- `bullmq.exceptions.WorkerError: Worker crashed`
- `redis.exceptions.TimeoutError: Command timed out`

## How to Fix It

### Fix 1: Configure worker properly

```python
from bullmq import Worker, Queue
import redis.asyncio as redis

# Wrong — no error handling
# worker = Worker("my-queue", process_job)

# Correct — configure with error handling
async def process_job(job):
    try:
        result = await do_work(job.data)
        return result
    except Exception as e:
        print(f"Job {job.id} failed: {e}")
        raise

worker = Worker(
    "my-queue",
    process_job,
    connection=redis.from_url("redis://localhost:6379"),
    concurrency=10,
)
```

### Fix 2: Add jobs to queue

```python
from bullmq import Queue
import redis.asyncio as redis

queue = Queue("my-queue", connection=redis.from_url("redis://localhost:6379"))

# Add job
job = await queue.add(
    "process",
    data={"key": "value"},
    opts={
        "attempts": 3,
        "backoff": {"type": "exponential", "delay": 1000},
    },
)

# Wait for result
result = await job.waitUntilCompleted(queue.events)
```

### Fix 3: Handle events

```python
from bullmq import Queue, Worker
import redis.asyncio as redis

queue = Queue("my-queue", connection=redis.from_url("redis://localhost:6379"))

# Listen to events
await queue.on("completed", lambda job, result: print(f"Job {job.id} completed"))
await queue.on("failed", lambda job, error: print(f"Job {job.id} failed: {error}"))
```

## Common Scenarios

- **Redis connection lost** — Worker loses connection during job execution.
- **Job timeout** — Job exceeds configured timeout limit.
- **Concurrency limit** — Too many concurrent jobs for the worker.

## Prevent It

- Always set `attempts` and `backoff` for automatic retry on transient failures.
- Use `concurrency` to limit parallel job execution.
- Handle job failures with `on("failed", ...)` events.

## Related Errors

- [ConnectionError](/languages/python/connectionerror/) — Redis connection failed
- [JobError](/languages/python/job-error/) — job execution failed
- [WorkerError](/languages/python/worker-error/) — worker crashed

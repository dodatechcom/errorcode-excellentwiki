---
title: "[Solution] Python arq Redis Queue Error — How to Fix"
description: "Fix Python arq Redis queue errors. Resolve worker, job, and cron issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python arq Redis Queue Error

An `arq.exceptions.JobError` or `ConnectionError` occurs when arq fails to enqueue jobs, when the Redis connection drops, or when scheduled cron tasks fail.

## Why It Happens

arq is an async Redis-based job queue. Errors arise when Redis is unreachable, when job functions raise exceptions, when cron schedules are invalid, or when job results expire.

## Common Error Messages

- `ConnectionError: Error connecting to Redis`
- `JobError: job function raised an exception`
- `DeadlineExceeded: job exceeded deadline`
- `FinishedJob: job already finished`

## How to Fix It

### Fix 1: Configure worker properly

```python
from arq import create_pool
from arq.connections import RedisSettings
from arq.worker import Worker

redis_settings = RedisSettings(host="localhost", port=6379, database=0)

async def create_worker():
    pool = await create_pool(redis_settings)
    worker = Worker(
        functions=[my_task, process_data],
        broker=pool,
        max_jobs=10,
        job_timeout=300,
        max_tries=3,
    )
    await worker.run()
```

### Fix 2: Handle job errors

```python
from arq import cron
from arq.connections import RedisSettings

redis_settings = RedisSettings(host="localhost")

@cron(hour=9, minute=0, run_at_startup=True)
async def daily_report(ctx):
    try:
        report = await generate_report()
        await send_report(report)
    except Exception as e:
        print(f"Report failed: {e}")
```

### Fix 3: Enqueue jobs

```python
from arq import create_pool
from arq.connections import RedisSettings

async def main():
    pool = await create_pool(RedisSettings(host="localhost"))
    job = await pool.enqueue_job(
        "process_job",
        data={"key": "value"},
        _job_id="custom-id",
        _timeout=300,
    )
    if job:
        result = await job.result(timeout=60)
        print(f"Job result: {result}")
    await pool.close()
```

## Common Scenarios

- **Redis connection lost** — Worker loses connection during job execution.
- **Job timeout** — Async job exceeds configured deadline.
- **Cron not running** — Worker process not running during scheduled time.

## Prevent It

- Always set `job_timeout` to prevent infinite-running jobs.
- Use `max_tries` for automatic retry on transient failures.
- Run workers as background services with process managers.

## Related Errors

- [ConnectionError](/languages/python/connectionerror/) — Redis connection failed
- [JobError](/languages/python/job-error/) — job function raised exception
- [DeadlineExceeded](/languages/python/deadline-exceeded/) — job timeout

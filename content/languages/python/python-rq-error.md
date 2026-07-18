---
title: "[Solution] Python RQ Redis Queue Error — How to Fix"
description: "Fix Python RQ Redis queue errors. Resolve worker, job, and connection issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python RQ Redis Queue Error

A `rq.exceptions.ConnectionError` or `rq.exceptions.NoSuchJobError` occurs when RQ fails to connect to Redis, when jobs are not found, or when workers encounter errors.

## Why It Happens

RQ (Redis Queue) is a simple job queue. Errors arise when Redis is unreachable, when jobs expire before processing, when workers crash, or when job results are not stored.

## Common Error Messages

- `ConnectionError: Error connecting to localhost:6379`
- `NoSuchJobError: No such job`
- `WorkerDeathException: Worker died`
- `TimeoutError: Operation timed out`

## How to Fix It

### Fix 1: Configure queue

```python
import redis
from rq import Queue

conn = redis.Redis(host="localhost", port=6379, db=0)
q = Queue(connection=conn, is_async=True, timeout=600)

job = q.enqueue(process_data, "arg1", "arg2")
print(f"Job ID: {job.id}")
```

### Fix 2: Handle job results

```python
from rq import Queue
import redis

conn = redis.Redis(host="localhost", port=6379)
q = Queue(connection=conn)

job = q.enqueue(process, data)

try:
    result = job.wait(timeout=60)
    print(f"Result: {result}")
except Exception as e:
    print(f"Job failed: {e}")

print(f"Status: {job.get_status()}")
```

### Fix 3: Configure workers

```bash
# Start worker
rq worker --url redis://localhost:6379 --timeout 600 --max-jobs 100
```

### Fix 4: Handle failures

```python
from rq import Queue
from rq.retry import Retry

conn = redis.Redis(host="localhost", port=6379)
q = Queue(connection=conn)

job = q.enqueue(
    risky_task,
    data,
    retry=Retry(max=3, interval=[10, 30, 60]),
)

if job.is_failed:
    print(f"Job failed: {job.exc_info}")

failed_jobs = q.failed_job_registry.get_job_ids()
print(f"Failed jobs: {len(failed_jobs)}")
```

## Common Scenarios

- **Job expired** — Job TTL expires before worker processes it.
- **Worker crashed** — Worker process terminated during execution.
- **Result lost** — Job result not stored due to Redis eviction.

## Prevent It

- Set appropriate `timeout` values on both queue and individual jobs.
- Use `retry` parameter for automatic retry on transient failures.
- Configure Redis `maxmemory-policy` to prevent key eviction.

## Related Errors

- [ConnectionError](/languages/python/connectionerror/) — Redis connection failed
- [NoSuchJobError](/languages/python/no-such-job/) — job not found
- [WorkerDeathException](/languages/python/worker-death/) — worker crashed

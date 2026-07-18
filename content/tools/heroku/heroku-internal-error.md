---
title: "[Solution] Heroku Internal Error - Fix R13 Attach Error R14 Memory Quota Exceeded"
description: "Fix Heroku R13 and R14 errors including attach failures and memory quota exceeded. Resolve dyno memory, swap, and resource limits."
tools: ["heroku"]
error-types: ["internal-error"]
severities: ["critical"]
weight: 5
---

This error means your Heroku dyno encountered an internal runtime error. R13 indicates an attach error while R14 means the dyno exceeded its memory quota.

## What This Error Means

Heroku assigns error codes to runtime issues. Common internal errors include:

```
R13 - Attach error: could not attach to dyno
R14 - Memory quota exceeded: 512MB (1.5GB)
```

R13 means the logging system could not attach to the dyno. R14 means the application used more memory than the dyno plan allows, causing the kernel to kill processes.

## Why It Happens

- R13: The dyno crashed before the logging system could attach
- R13: A configuration error prevents the dyno from starting
- R14: The application has a memory leak causing gradual growth
- R14: The dyno plan has insufficient memory for the workload
- R14: Java, Ruby, or Node.js applications need explicit memory tuning
- R14: Large dataset loading into memory exceeds available resources

## How to Fix It

### Check dyno logs

```bash
heroku logs --tail -a my-app
```

Review logs for the specific error code and surrounding context.

### Upgrade the dyno plan for more memory

```bash
heroku ps:resize web=standard-2x -a my-app
```

Available plans:
- `eco`: 512MB
- `basic`: 512MB
- `standard-1x`: 512MB
- `standard-2x`: 1GB
- `performance-m`: 2.5GB
- `performance-l`: 14GB

### Fix R13 attach errors

```bash
heroku ps -a my-app
```

Restart the dyno if it is in a crashed state:

```bash
heroku restart -a my-app
```

### Monitor memory usage

```bash
heroku metrics:memory -a my-app
```

Check memory trends to identify leaks or spikes.

### Enable swap for graceful degradation

```bash
heroku config:set WEB_CONCURRENCY=2 -a my-app
```

Reducing worker count lowers memory usage.

### Optimize application memory

```python
# For Python/Django
import gc
gc.collect()
```

```javascript
// For Node.js
--max-old-space-size=400
```

### Set memory-efficient configuration

```bash
heroku config:set NJS_MEMORY_LIMIT=350M -a my-app
heroku config:set WEB_CONCURRENCY=1 -a my-app
```

### Use multiple smaller dynos

```bash
heroku ps:scale web=2 -a my-app
```

Running two smaller dynos may use less memory than one large one.

## Common Mistakes

- Not monitoring memory metrics before hitting the quota
- Running more workers than the dyno memory can support
- Not enabling swap on Heroku which can prevent R14 kills
- Ignoring R13 errors which often indicate configuration problems
- Not setting JAVA_OPTS or NODE_OPTIONS to limit memory

## Related Pages

- [Heroku Build Error]({{< relref "/tools/heroku/heroku-build-error" >}}) -- build failures
- [Heroku Dyno Error]({{< relref "/tools/heroku/heroku-dyno-error" >}}) -- dyno issues
- [Heroku Runtimes Error]({{< relref "/tools/heroku/heroku-runtimes-error" >}}) -- runtime problems
